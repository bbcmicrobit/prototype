#!/usr/bin/python

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
