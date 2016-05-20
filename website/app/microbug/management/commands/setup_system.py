#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from django.core.management.templates import TemplateCommand
import microbug.settings as settings
from django.contrib.auth.models import User, Group

class Command(TemplateCommand):

    help = "Sets up the system for basic use"

    def handle(self, user_count_str="1", **options):
        print("Setting up system ready for use")
        self._ensure_facilitators_exists()

    def _ensure_facilitators_exists(self):
        created, facilitators = Group.objects.get_or_create(name='facilitators')
        if created:
            print "Group 'Facilitators' has been created"
        else:
            print "Group 'Facilitators' already exists"
