#!/usr/bin/python

import pprint
import os
import os.path
import shutil

# local import
from codegenerator import CodeGenerator, gen_code

import lexer_parser
from lexer_parser import configure_lexer, parse

lexer = configure_lexer()

DAL_DIR = "../dal/"

def main_test(files):
    """Mainly used during testing"""
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

    for filename in files:
        print
        print "PARSING", filename
        source = open("tests/progs/"+filename).read()
        print source

        x = parse(source, lexer)

        pprint.pprint(x,width=120)
        print "-"*120
        if 1:
            y  = gen_code(x)
            basedir = "tests/genprogs/"+filename
            os.mkdir(basedir)
            f = open(basedir+"/user_code.ino", "w")
            f.write(y)
            f.close()

        if 1:
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

            print "#"*120

def main_single(source_file, dest_file, tmp_directory, cleanup=False):
    """
    Compiles a single source file.
    Creates a dest_file - which is a .hex file.
    May work inside tmp_directoy
    Must cleanup if cleanup is True
    """
    global os
    lexer_parser.quiet_mode = True

    basefile = os.path.basename(source_file)

    source = open(source_file).read()
    x = parse(source, lexer)
    y  = gen_code(x)

    basedir = os.path.join(tmp_directory, basefile)
    os.mkdir(basedir)
    f = open(basedir+"/user_code.ino", "w")
    f.write(y)
    f.close()

    shutil.copyfile(DAL_DIR + "dal.h", basedir+"/dal.h")
    shutil.copyfile(DAL_DIR + "Makefile", basedir+"/Makefile")
    shutil.copyfile(DAL_DIR + "Makefile_arduino", basedir+"/Makefile_arduino")
    shutil.copyfile(DAL_DIR + "spark_font.h", basedir+"/spark_font.h")
    shutil.copyfile(DAL_DIR + "atmel_bootloader.h", basedir+"/atmel_bootloader.h")
    here = os.getcwd()
    os.chdir(basedir)
    os.system("make quiet >build_outer_log 2>&1")

    os.chdir(here)

    hexfile = basedir + "/build-leonardo/" + basefile + ".hex"
    if os.path.exists(hexfile):
        shutil.copyfile(hexfile, dest_file)
    else:
       raise RuntimeError("Cannot compile %s" % source_file)

if __name__ == "__main__":
    main()
