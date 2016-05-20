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

import sys
from py2cc.main import main_single

def single_usage(prog):

    print "Usage:"
    print
    print prog, "source/filename.py dest/filename.hex build_directory"

if __name__ == "__main__":
    if len(sys.argv) <4:
        single_usage(prog)
        sys.exit(1)

    prog = sys.argv[0]
    source_file = sys.argv[1]
    dest_file = sys.argv[2]
    build_directory = sys.argv[3]

    main_single(source_file, dest_file, build_directory)