#!/usr/bin/python

import pprint
import os
import shutil

# local import
from codegenerator import CodeGenerator, gen_code

#from lexer_parser import configure_lexer, configure_parser, do_parse
from lexer_parser import configure_lexer, parse

lexer = configure_lexer()

def main(files):
    global os
    #
    # Build the example test programs, compile them and run them
    #
    if len(files) == 0:
        files = os.listdir("tests/progs")
        files = [ x for x in files if "skip" not in x ]
        files.sort()

    ditch = os.listdir("tests/genprogs")
    for filename in ditch:
        os.system("rm -rf tests/genprogs/"+ filename)
        # os.unlink("tests/genprogs/"+ filename)


    for filename in files:
        print
        print "PARSING", filename
        source = open("tests/progs/"+filename).read()

        x = parse(source, lexer)

        pprint.pprint(x,width=120)
        print "-"*120
        y  = gen_code(x)
        basedir = "tests/genprogs/"+filename
        os.mkdir(basedir)
        f = open(basedir+"/user_code.ino", "w")
        f.write(y)
        f.close()

        shutil.copyfile("../dal/dal.h", basedir+"/dal.h")
        shutil.copyfile("../dal/Makefile", basedir+"/Makefile")
        shutil.copyfile("../dal/Makefile_arduino", basedir+"/Makefile_arduino")
        shutil.copyfile("../dal/spark_font.h", basedir+"/spark_font.h")
        shutil.copyfile("../dal/atmel_bootloader.h", basedir+"/atmel_bootloader.h")
        here = os.getcwd()
        os.chdir(basedir)
        os.system("make")
        print "READY TO UPLOAD"
        print "PRESS RETURN TO ERASE"
        raw_input(">")
        os.system("make erase")
        print "PRESS RETURN TO FLASH DEVICE"
        raw_input(">")
        os.system("make flash_device")
        os.chdir(here)

        #trimmed = filename[:filename.find(".p")]
        #os.system("g++ " + "tests/genprogs/"+filename+".cpp" + " -o " + "tests/genprogs/gen-"+trimmed )

        #if "no_run" not in trimmed:
            #print "Compiled program output:"
            #os.system("tests/genprogs/gen-"+trimmed)

        print "#"*120

if __name__ == "__main__":
    main()
