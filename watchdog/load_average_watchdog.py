#!/usr/bin/python
"""

Watch the system load. If the load goes over a maximum load average then
this script stops and restarts the apache processes, logging the result.

"""

import os
import time

LOGFILE = "/tmp/server_restartlogs"
def log(*args):
    f = open(LOGFILE, "w")
    f.write(time.asctime())
    f.write(" : ")
    f.write( " ".join([ str(x) for x in args ])+"\n" )
    f.flush()
    f.close()

max_load_average = 50

while True:
    uptime = open("/proc/loadavg").read()
    uptime = uptime.strip()

    info = uptime.split()

    one_min_R = info[0]
    five_min_R = info[1]
    fifteen_min_R = info[2]

    five_min = float(five_min_R)

    if five_min > max_load_average:
        log("Above max load average")
        
        p = os.popen("ps aux").readlines()
        apachelines = [x for x in p if "apache" in x ]
        log("number of processes")
        log(len(apachelines)) 
        result = os.popen("apachectl stop").read()

        c = 0
        while (len(apachelines) > 0) and c < 60: # WHile there's apache processes still opening after at most 3 minutes, don't move on to next step.
            log("Waiting for apache to stop", c)
            c += 1
            if (c % 3) == 0:
                p = os.popen("ps aux").readlines()
            time.sleep(5)
            p = os.popen("ps aux").readlines()
            apachelines = [x for x in p if "apache" in x ]


        while len(apachelines) > 0:
            # Manually kill all the apache processes
            log("Manually kill remaining apacheline lines")
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
        else:
            print "Apache is still running despite best efforts to prevent it taking down the system"
        time.sleep(180)
 
 
 
 