#!/usr/bin/python

import cgitb
cgitb.enable()

import json
import cgi,time
from filelock.filelock import FileLock

form = cgi.FieldStorage()
results = {}
cmd = form.getvalue('repr', '')

cmd = repr(cmd)
cmd = cmd.replace("&", "&amp;")
cmd = cmd.replace(">", "&lt;")
cmd = cmd.replace("<", "&gt;")

if cmd != "''":
    with FileLock("../upload/highest.lock", timeout=2) as lock:
        f = open("../upload/highest")
        r = f.read()
        r = r.strip()
        top_id = int(r)
        f.close()
        top_id += 1
        f = open("../upload/highest","w")
        f.write(str(top_id))
        f.close()
        f = open("../upload/" + str(top_id) + ".json", "w")
        data = { "cmd": cmd, "id": top_id }
        f.write(json.dumps(data))
        f.flush()
        f.close()
else:
    cmd = "No data uploaded"
    top_id = ""

print "Content-type: text/html"
print
print """\
<html>
<head>
<script src="/jquery.min.js" type="text/javascript"></script>
</head>
<body>
<h1>%s</h1>

Uploaded Data: %s

<form action="reflect.py" method="post">
<textarea style="width: 99%%" name="repr" id="repr">
Mary had a little lamb, its fleece as white as snow.
</textarea>
<button type="submit">Submit</button>
</form>
</body>
</html>""" % (repr(top_id), repr(cmd))

