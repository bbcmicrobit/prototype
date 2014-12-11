from django.core.management.templates import TemplateCommand
import os
from microbug.models import Tutorial
from markdown import markdown
#from hoedown import Markdown, HtmlRenderer
import re
from django.template.defaultfilters import slugify
from django.template import Context, Template
import microbug.settings as settings
import shutil
import uuid

class Command(TemplateCommand):
    help = "Imports all of the tutorial .md files from a directory"
    post_replacements = {}

    def handle(self, tutorial_directory=None, **options):
        if tutorial_directory is None:
            print"Usage: python manage.md import_tutorials <tutorial source directory>"
            return

        self._delete_all_tutorials();
        print("Importing tutorials from '{0}'".format(tutorial_directory))

        for md_filename in self._full_md_filenames_from(tutorial_directory):
            self._import_md_file(md_filename)
            pass

        self._copy_tutorial_assets(os.path.abspath(tutorial_directory)+'/static/bug/tutorial_assets')

    def _render_as_django_template(self, template_content, context_hash={}):
        template = Template(template_content)
        context = Context(context_hash)
        return template.render(context)

    def _delete_all_tutorials(self):
        print("Deleting all tutorials")
        Tutorial.objects.all().delete()

    def _full_md_filenames_from(self, dir):
        return [
            os.path.join(dir, filename)
            for filename in os.listdir(dir)
            if filename.endswith('.md')
        ]

    def _import_md_file(self, filename):
        print("  Processing '{0}'".format(filename))
        tutorial_name = self._tutorial_name_from_filename(filename)

        # Read in the raw content, process the '!page' command, then treat as
        # Django template, and then treat the result as Markdown.

        content = self._slurp(filename)
        content = self._fix_static_links(content)
        content = self._process_pling_page(content)
        #print("CONTENT: {}".format(content))
        content = self._render_as_django_template(content)
        content = self._process_pling_loadcode(content)
        content = markdown(content, ['markdown.extensions.extra'])
        content = self._apply_post_replacements(content)
        # print("CONTENT: {}".format(content))
        new_tut = Tutorial(name=tutorial_name, content=content)
        new_tut.save()

    def _apply_post_replacements(self, content):
        for key in self.post_replacements:
            replacement = self.post_replacements[key]
            content = content.replace(key, replacement)
        return content

    def _fix_static_links(self, content):
        return content.replace(
            'static/bug/tutorial_assets',
            '/static/bug/tutorial_assets'
        )

    def _process_pling_page(self, content):
        seenPreviousPage = False
        while True:
            # Find the next match
            match = re.search('^!page:(.*?)$', content, re.MULTILINE | re.IGNORECASE)
            if not match:
                break
            content = content[:match.start()] + self._section_marker(match.group(1), seenPreviousPage) + content[match.end():]
            seenPreviousPage = True

        if seenPreviousPage:
            content += "</section>"

        return content

    def _process_pling_loadcode(self, content):
        while True:
            # Find the next match
            match = re.search('!LoadCode:\"(.*?)\"$', content, re.MULTILINE | re.IGNORECASE)
            if not match:
                break
            content = content[:match.start()] + self._loadcode_button(match.group(1)) + content[match.end():]
        return content

    # Builds a button to load code.
    def _loadcode_button(self, xml_content):
        # return "!!LC!!"
        unique_id = "<<{}>>".format(uuid.uuid1())
        base_str = """
            <br/>
            <button class='btn btn-primary load-code-btn' data-blockly-xml='{}'>
                <i class='fa fa-cogs'></i>&nbsp;Load Code
            </button>
            <br/>
        """
        self.post_replacements[unique_id] = base_str.format(xml_content)
        return unique_id

    # Builds the section marker for pages.
    def _section_marker(self, template_name=None, seenPrevious=False):
        replacement = ''
        if seenPrevious:
            replacement += "</section>\n"
        replacement += "<section markdown='1'>\n"
        if template_name is not None:
            replacement += '{% include "microbug/partials/blockly_toolboxes/'+template_name+'.html" %}'
        return replacement

    def _tutorial_name_from_filename(self, filename):
        return slugify(re.sub('\.(.*?)$', '', os.path.basename(filename)))

    def _slurp(self, filename):
        file = open(filename,"r")
        content = file.read()
        file.close()
        return content

    def _copy_tutorial_assets(self, source_dir):
        target_dir = settings.TUTORIAL_ASSETS_STATIC_DIRECTORY
        print("Deploying tutorial assets")
        print("  from: '{0}'".format(source_dir))
        print("  to  : '{0}'".format(target_dir))
        shutil.rmtree(target_dir)
        #os.mkdir(target_dir)
        shutil.copytree(source_dir, target_dir)