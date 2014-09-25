#!/usr/bin/python

import cgitb
cgitb.enable()

import json
import sys
import cgi,time
import os
form = cgi.FieldStorage()

program_id = form.getvalue('id', '')

if program_id != '':

    # TODO: Validate/verify tainted values
    z = open("../upload/%s.json" % program_id)
    rj = z.read()
    j = json.loads(rj)
    z.close()
    record = j["myjson"]
    record = json.loads(record)
    program_xml= record["repr"]

    print "Content-type: application/json"
    print
    print json.dumps(program_xml)

else:
    env  = dict(os.environ)
    if env.get("PATH_INFO", None) != None:
        page = open("../docs/blockly_reload.html").read()
        print "Content-type: text/html"
        print
        print page

    else:
        print "Status: 500"
        print "Content-type: application/json"
        print
        print json.dumps({"error": "missing id", "env": env}, indent = 4)
