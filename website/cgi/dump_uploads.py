#!/usr/bin/python

import json

f = open("../upload/highest")
x = f.read()
x = x.strip()
f.close()
x = int(x)

print "Content-type: text/html"
print
print "<html><body>"

for i in range(1, x +1):
    print "<p>", i
    print "<ul>"
    z = open("../upload/%d.json" % i)
    rj = z.read()
    j = json.loads(rj)
    z.close()
    program = j["myjson"]
    program = json.loads(program)
    program = program["repr"]["code"]

    try:
        program = json.loads(program)
    except ValueError:
        pass

    program = program.replace("&", "&amp;")
    program = program.replace(">", "&lt;")
    program = program.replace("<", "&gt;")

    print "<PRE>"
    print program
    print "</PRE>"
    print "</ul>"
    print

print "</body></html>"
