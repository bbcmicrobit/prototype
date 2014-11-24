#!/bin/bash

# This clears out all of the store for the Microbug app, and creates a nice
# new empty store.

/usr/bin/python2.7 manage.py flush

if [ -e michaels_machine ] ; then 
    # "michaels machine"; 
   # Django 1.6 equivalent
    python manage.py syncdb
else 
    # "Not michaels machine"; 

# These next two ONLY WORK ON Django 1.7
    /usr/bin/python2.7 manage.py makemigrations
    /usr/bin/python2.7 manage.py migrate

    /usr/bin/python2.7 manage.py createsuperuser
    rm -rf ~/Documents/microbug_store
    cp -rvf ~/Documents/microbug_store_empty ~/Documents/microbug_store
fi


