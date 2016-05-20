#!/bin/bash
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

# This clears out all of the store for the Microbug app, and creates a nice
# new empty store.
mv db.sqlite3 _db.sqlite3
rm ./microbug/migrations/0*
/usr/bin/python2.7 manage.py makemigrations
/usr/bin/python2.7 manage.py migrate
#/usr/bin/python2.7 manage.py flush

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

/usr/bin/python2.7 manage.py setup_system
/usr/bin/python2.7 manage.py import_tutorials tutorial_source/
/usr/bin/python2.7 manage.py create_users 5 > /tmp/usernames_and_passwords.txt
/usr/bin/python2.7 manage.py create_users 5 >> /tmp/usernames_and_passwords.txt
cat /tmp/usernames_and_passwords.txt



