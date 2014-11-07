#!/usr/bin/python

import json

f = open("../upload/highest")
x = f.read()
x = x.strip()
f.close()
x = int(x)

print "Content-type: application/json"
print

uploads = []

for i in range(1, x +1):
    uploads.append( {"id": str(i), "href": "/blockly_reload.html?id=%d"%i})


result = { "status": 200, "description": "list of uploads", "data": uploads}
print json.dumps(result ,indent=2)
