#!/usr/bin/python

import json
import sys

print "Content-type: application/json"
print
raw_stdin = sys.stdin.read()
myjson = json.loads(raw_stdin)
file_tag = str(myjson["repr"]["id"])

z = open("../upload/%s.json" % file_tag)
rj = z.read()
j = json.loads(rj)
z.close()
record = j["myjson"]
record = json.loads(record)
program_xml= record["repr"]

print json.dumps(program_xml)
