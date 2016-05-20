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
