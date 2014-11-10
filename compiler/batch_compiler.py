#!/usr/bin/python

from guild.actor import Actor, actor_method, process_method, late_bind, pipe, start, stop, wait_for
import os, time

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
    @actor_method
    def reprocess_directory(self):
        print "Processing directory"



dw = DirectoryWatcher("tests/progs")
cc = Compiler()

pipe(dw, "directory_change", cc, "reprocess_directory")

start(dw, cc)

while True:
    time.sleep(6)

stop(dw, cc)
wait_for(dw, cc)
