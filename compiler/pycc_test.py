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

# ./pycc_test.py noflash true testdir user_compiled
# ./pycc_test.py testdir user_compiled
# ./pycc_test.py
# ./pycc_test.py
# (P=58; ./pycc_test.py $P.p ; cat tests/genprogs/$P.p/user_code.ino 2>&1)
# (P=999_fcbaa760-9745-11e4-ab48-02f2a2e5afe5.py; ./pycc_test.py testdir user_compiled $P ; cat tests/genprogs/$P/user_code.ino 2>&1)


import sys
from py2cc.main import main_test

noflash = False
testdir = "progs"
argv = list(sys.argv)
found_opt = True

while found_opt and len(argv) >= 3:
    found_opt = False
    option, optarg = argv[1:3]
    if option == "noflash" and optarg.lower() == "true":
        noflash = True
        found_opt = True
    if option == "testdir":
        testdir = optarg
        found_opt = True
    if found_opt:
        del argv[1]
        del argv[1]

print "main_test(noflash, testdir, argv[1:])"
print "main_test(",noflash, ",", testdir,",", argv[1:],")"

main_test(noflash, testdir, argv[1:])
