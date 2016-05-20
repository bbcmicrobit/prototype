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

"""

Watch the system load. If the load goes over a maximum load average then
this script stops and restarts the apache processes, logging the result.

"""

import os
import time

LOGFILE = "/tmp/server_restartlogs"
def log(*args):
    f = open(LOGFILE, "a")
    f.write(time.asctime())
    f.write(" : ")
    f.write( " ".join([ str(x) for x in args ])+"\n" )
    f.flush()
    f.close()
    print " ".join([repr(x) for x in args])

max_load_average = 30
way_too_high = 80

log("Starting up, max load average:", max_load_average)
log("current load average:", open("/proc/loadavg").read())
while True:
    uptime = open("/proc/loadavg").read()
    uptime = uptime.strip()

    info = uptime.split()

    one_min_R = info[0]
    five_min_R = info[1]
    fifteen_min_R = info[2]

    five_min = float(five_min_R)
    one_min = float(one_min_R)

#    if (five_min > max_load_average) or (one_min > way_too_high):
    if (one_min > way_too_high):
        log("Above max load average :" + str(uptime) )
        
        p = os.popen("ps aux").readlines()
        apachelines = [x for x in p if "apache" in x ]
        log("number of processes " + str(len(apachelines) ))

        result = os.popen("apachectl stop").read()

        c = 0
        while (len(apachelines) > 0) and c < 60: # WHile there's apache processes still opening after at most 3 minutes, don't move on to next step.
            log("Waiting for apache to stop this many processes"+ str(c))
            c += 1
            if (c % 3) == 0:
                p = os.popen("ps aux").readlines()
            time.sleep(5)
            p = os.popen("ps aux").readlines()
            apachelines = [x for x in p if "apache" in x ]


        while len(apachelines) > 0:
            # Manually kill all the apache processes
            log("Manually kill remaining apacheline lines num:" +str(len(apachelines)))
            for line in apachelines:
               x = line.strip()
               x = line.split()
               pid = int(x[1])
               #
               os.kill(pid, 9)
            #
            time.sleep(10)
            p = os.popen("ps aux").readlines()
            apachelines = [x for x in p if "apache" in x ]

        p = os.popen("ps aux").readlines()
        apachelines = [x for x in p if "apache" in x ]
        if len(apachelines) == 0:
            result = os.popen("apachectl start").read()
            log("Restarted apache")
        else:
             log("Apache is still running despite best efforts to prevent it taking down the system")
 
    time.sleep(5)
 
 
 