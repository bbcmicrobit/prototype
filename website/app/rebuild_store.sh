#!/bin/bash

# This clears out all of the store for the Microbug app, and creates a nice
# new empty store.

/usr/bin/python2.7 manage.py flush
/usr/bin/python2.7 manage.py makemigrations
/usr/bin/python2.7 manage.py migrate
/usr/bin/python2.7 manage.py createsuperuser
rm -rf ~/Documents/microbug_store
cp -rvf ~/Documents/microbug_store_empty ~/Documents/microbug_store
