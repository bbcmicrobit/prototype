#!/usr/bin/python
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

from guild.actor import Actor, actor_method, process_method, late_bind, pipe, start, stop, wait_for
import os, time

from py2cc.main import main_single
import logging

logging.basicConfig()

# Default to assuming running on michael's machine

INCOMING_DIRECTORY = "/home/michael/Work/CodeBug/MiniMicro/website/website/microbug_store/pending/"
OUTGOING_DIRECTORY = "/home/michael/Work/CodeBug/MiniMicro/website/website/microbug_store/compiled/"
FAIL_DIRECTORY = "/home/michael/Work/CodeBug/MiniMicro/website/website/microbug_store/failed_compiles/"
BUILD_DIRECTORY = "/home/michael/Work/CodeBug/MiniMicro/website/website/tmp/"

LOGFILE = "/tmp/compiler_log"
def log(*args):
    f = open(LOGFILE, "a")
    f.write(time.asctime())
    f.write(" : ")
    f.write( " ".join([ str(x) for x in args ])+"\n" )
    f.flush()
    f.close()
    print " ".join([repr(x) for x in args])



try:
    # Are we running on the shared dev server?
    import sparkslabs

    INCOMING_DIRECTORY = "/srv/Websites/minimicro.iotoy.org/website/microbug_store/pending/"
    OUTGOING_DIRECTORY = "/srv/Websites/minimicro.iotoy.org/website/microbug_store/compiled/"
    FAIL_DIRECTORY = "/srv/Websites/minimicro.iotoy.org/website/microbug_store/failed_compiles/"
    BUILD_DIRECTORY = "/srv/Websites/minimicro.iotoy.org/website/tmp/"

except ImportError:
    pass

try:
    # Are we running on the shared dev server?
    import taster_machine

    INCOMING_DIRECTORY = "/srv/projects/microbug/website/microbug_store/pending/"
    OUTGOING_DIRECTORY = "/srv/projects/microbug/website/microbug_store/compiled/"
    FAIL_DIRECTORY = "/srv/projects/microbug/website/microbug_store/failed_compiles/"
    BUILD_DIRECTORY = "/srv/projects/microbug/website/tmp/"

except ImportError:
    pass



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
        log( "Processing directory" )
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
            log( "Compiling", source_filename )
            source_file = os.path.join(INCOMING_DIRECTORY, source_filename)
            dest_file = os.path.join(OUTGOING_DIRECTORY, dest_filename)
            try:
                main_single(source_file, dest_file, BUILD_DIRECTORY)
                log( "Moving compiled program" )
                os.rename(source_file, os.path.join(OUTGOING_DIRECTORY, source_filename))
            except Exception, e:
                os.rename(source_file, os.path.join(FAIL_DIRECTORY, source_filename))
                log( "OK, we failed, we've moved the failed program to the failed directory")
                log( "How to we report the fail?" )
                log( "repr(e)", repr(e) )

        log( "Finished processing directory" )
        log( "Number of programs compiled", len(filenames) )

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
