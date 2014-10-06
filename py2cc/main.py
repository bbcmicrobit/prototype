#!/usr/bin/python

import pprint

# local import
from codegenerator import CodeGenerator, gen_code

from lexer_parser import configure_lexer, configure_parser, do_parse

configure_lexer()


def main():
    import os
    #
    # Build the example test programs, compile them and run them
    #

    files = os.listdir("tests/progs")
    files = [ x for x in files if "skip" not in x ]
    files.sort()

    ditch = os.listdir("tests/genprogs")
    for filename in ditch:
        os.unlink("tests/genprogs/"+ filename)


    for filename in files:
        print
        print "PARSING", filename
        source = open("tests/progs/"+filename).read()
        configure_parser()

        #yacc.yacc(module=Grammar())
        # x = yacc.parse(source)
        x = do_parse(source)
        pprint.pprint(x,width=120)
        print "-"*120
        y  = gen_code(x)
        f = open("tests/genprogs/"+filename+".cpp", "w")
        f.write(y)
        f.close()
        trimmed = filename[:filename.find(".p")]
        os.system("g++ " + "tests/genprogs/"+filename+".cpp" + " -o " + "tests/genprogs/gen-"+trimmed )

        if "no_run" not in trimmed:
            print "Compiled program output:"
            os.system("tests/genprogs/gen-"+trimmed)

        print "#"*120

    import os
    os.unlink("parser.out")
    os.unlink("parsetab.py")
    os.unlink("parsetab.pyc")

if __name__ == "__main__":
    main()
