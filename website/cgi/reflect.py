#!/usr/bin/python
#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

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

