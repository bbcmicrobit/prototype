#!/usr/bin/python

from guild.actor import Actor, actor_method, process_method, late_bind, pipe, start, stop, wait_for
import os, time

from py2cc.main import main_single
import logging

logging.basicConfig()

try:
    # Are we running on the shared dev server?
    import sparkslabs

    INCOMING_DIRECTORY = "/srv/Websites/minimicro.iotoy.org/website/microbug_store/pending/"
    OUTGOING_DIRECTORY = "/srv/Websites/minimicro.iotoy.org/website/microbug_store/compiled/"
    BUILD_DIRECTORY = "/srv/Websites/minimicro.iotoy.org/website/tmp/"

except ImportError:
    # If not, assume we're running on michael's dev machine

    INCOMING_DIRECTORY = "/home/michael/Work/CodeBug/MiniMicro/website/compiler/../website/python_pending/"
    OUTGOING_DIRECTORY = "/home/michael/Work/CodeBug/MiniMicro/website/compiler/../website/docs/compiled/"
    BUILD_DIRECTORY = "/home/michael/Work/CodeBug/MiniMicro/website/compiler/../website/tmp/"

class DirectoryWatcher(Actor):
    def __init__(self, directory):
        super(DirectoryWatcher, self).__init__()
        self.directory = directory
        self.directory_stat = os.stat(self.directory)

    @late_bind       # Output
    def directory_change(self):
        pass

    @process_method
    def process(self):
        time.sleep(0.1)
        stat = os.stat(self.directory)
        if stat.st_ctime != self.directory_stat.st_ctime:
            self.directory_stat = stat
            self.directory_change()

class Compiler(Actor):
    """This assumes that INCOMING_DIRECTORY and OUTGOING_DIRECTORY above are defined for this class"""
    @actor_method
    def reprocess_directory(self):
        print "Processing directory"
        filenames = os.listdir(INCOMING_DIRECTORY)
        filenames = [ x for x in filenames if x != "README" ] # Ignore README

        # filenames.sort()
        try:
            # Sort filenames as per Pauls new naming scheme
            filenames = [y for z,y in sorted([(int(a.split("_")[0]),a ) for a in filenames])]
        except ValueError:
            # Sort filenames as per current new naming scheme
            filenames = [y for z,y in sorted([(int(a.replace(".py","")),a ) for a in filenames])]

        for source_filename in filenames:
            dest_filename = source_filename.replace(".py", ".hex")
            print "Compiling", source_filename
            source_file = os.path.join(INCOMING_DIRECTORY, source_filename)
            dest_file = os.path.join(OUTGOING_DIRECTORY, dest_filename)
            main_single(source_file, dest_file, BUILD_DIRECTORY)
            print "Moving compiled program"
            os.rename(source_file, os.path.join(OUTGOING_DIRECTORY, source_filename))


dw = DirectoryWatcher(INCOMING_DIRECTORY)
cc = Compiler()

pipe(dw, "directory_change", cc, "reprocess_directory")

start(dw, cc)

time.sleep(1)

cc.reprocess_directory() # Prod the compilation directory at startup

while True:
    time.sleep(6)

stop(dw, cc)
wait_for(dw, cc)
