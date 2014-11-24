#!/usr/bin/python


import cgitb
cgitb.enable()


print "Content-type: text/plain"
print
print "Creating sync token"

f = open("/tmp/sync_server", "w")
f.write(".")
f.close()
