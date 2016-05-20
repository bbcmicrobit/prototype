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
