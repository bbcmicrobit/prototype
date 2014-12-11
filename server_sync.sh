#!/bin/bash

# This won't work on live server for practical reasons


while true; do
   if [ -e /tmp/sync_server ]; then
       echo "checking github"
       rm -f /tmp/sync_server
       cd /srv/Websites/minimicro.iotoy.org
       git fetch github
       git stash
       git rebase github/master master
       git stash pop
       chmod a+rwx /srv/Websites/minimicro.iotoy.org/website/app/
       chmod a+rwx /srv/Websites/minimicro.iotoy.org/website/app/db.sqlite3
   fi
   sleep 1
done

