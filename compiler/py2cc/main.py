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

def strip_comments(source_file):
    """ FIXME: This cannot handle comments inside strings yet, or after code on a line"""
    source_lines = source_file.split("\n")
    result = []
    for source_line in source_lines:
        seen_comment = False
        in_string = False
        string_char = None
        # Strip comments from line
        for char in source_line:
            if not in_string:
                if char == "#":
                    seen_comment = True
                    break
        if not(seen_comment):
            result.append(source_line)
    return "\n".join(result)


def main_test(noflash, testdir, files):
    #
    #default noflash is False
    #default testdir is "progs"
    #
    """Mainly used during testing"""
    global os
    #
    # Build the example test programs, compile them and run them
    #

    progs_dir = "tests/"+testdir
    if len(files) == 0:
#        files = os.listdir("tests/progs")
#        files = os.listdir("tests/user_compiled")
        files = os.listdir(progs_dir)
        files = [ x for x in files if "skip" not in x ]
        files.sort()

    ditch = [x for x in os.listdir("tests/genprogs") if x != "README"]
    for filename in ditch:
        os.system("rm -rf tests/genprogs/"+ filename)


    root_dir = os.getcwd()
    for filename in files:
        os.chdir(root_dir)
        print
        print "PARSING", filename
        #source = open("tests/progs/"+filename).read()
        # source = open("tests/user_compiled/"+filename).read()
        source = open(progs_dir + "/" + filename).read()

        source = strip_comments(source)
        print source

        x = parse(source, lexer)

        pprint.pprint(x,width=120)
        print "-"*120

        if 1:
            basedir = "tests/genprogs/"+filename
            os.mkdir(basedir)
            f = open(basedir + "/" + filename,"w")
            f.write(source)
            f.flush()
            f.close()
            os.system("rsync -avz ../dal/ "+ basedir+"/")
            os.system("rsync -avz ../dal/ "+ basedir+"/")
            os.system("rm -rf " + basedir+"/001/")
            os.system("rm -rf " + basedir+"/002/")
            os.system("rm -rf " + basedir+"/003/")
            os.system("rm -rf " + basedir+"/*.hex")
            os.system("rm -rf " + basedir+"/build-leonardo/*.hex")
            os.system("rm " + basedir+"/MicroFont.odt")
            os.system("rm " + basedir+"/spark_font.json")
            os.system("rm " + basedir+"/user_code.ino")

        if 1:
            y  = gen_code(x)
            f = open(basedir+"/user_code.ino", "w")
            f.write(y)
            f.close()

#            shutil.copyfile("../dal/dal.h", basedir+"/dal.h")
#            shutil.copyfile("../dal/Makefile", basedir+"/Makefile")
#            shutil.copyfile("../dal/Makefile_arduino", basedir+"/Makefile_arduino")
#            shutil.copyfile("../dal/spark_font.h", basedir+"/spark_font.h")
#            shutil.copyfile("../dal/atmel_bootloader.h", basedir+"/atmel_bootloader.h")

        if 1:
            here = os.getcwd()
            os.chdir(basedir)
            os.system("make")

        if not noflash:
            print "READY TO UPLOAD"
            print "PRESS RETURN TO ERASE"
            # raw_input(">")
            # os.system("make erase")
            print "PRESS RETURN TO FLASH DEVICE"
            # raw_input(">")
            # os.system("make flash_device")
            os.chdir(here)

            print "#"*120
            print "#"*120
            print "#"*120
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
    source = strip_comments(source)
    x = parse(source, lexer)
    y  = gen_code(x)



    basedir = os.path.join(tmp_directory, basefile)
    os.mkdir(basedir)

    f = open(basedir + "/" + basefile,"w")
    f.write(source)
    f.flush()
    f.close()

    os.system("rsync >/dev/null -az ../dal/ "+ basedir+"/")
    os.system("rm -rf " + basedir+"/001/")
    os.system("rm -rf " + basedir+"/002/")
    os.system("rm -rf " + basedir+"/003/")
    os.system("rm -rf " + basedir+"/*.hex")
    os.system("rm -rf " + basedir+"/build-leonardo/*.hex")
    os.system("rm " + basedir+"/MicroFont.odt")
    os.system("rm " + basedir+"/spark_font.json")
    os.system("rm " + basedir+"/user_code.ino")

    f = open(basedir+"/user_code.ino", "w")
    f.write(y)
    f.close()

#   These are the only files that are technically needed:
#    shutil.copyfile(DAL_DIR + "dal.h", basedir+"/dal.h")
#    shutil.copyfile(DAL_DIR + "Makefile", basedir+"/Makefile")
#    shutil.copyfile(DAL_DIR + "Makefile_arduino", basedir+"/Makefile_arduino")
#    shutil.copyfile(DAL_DIR + "spark_font.h", basedir+"/spark_font.h")
#    shutil.copyfile(DAL_DIR + "atmel_bootloader.h", basedir+"/atmel_bootloader.h")
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
