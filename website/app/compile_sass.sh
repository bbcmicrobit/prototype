#!/usr/bin/env bash
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

# This is a simple little script which compiles the
# SASS files for the application into CSS in the right place.

echo "Compiling Bootstrap"
sass ./sass_src/_bootstrap.scss:microbug/static/bug/css/bootstrap.css

echo "Compiling Font Awesome"
sass ./sass_src/font-awesome.scss:microbug/static/bug/css/font-awesome.css

echo "All sass compiled"
terminal-notifier -title "Microbug Sass" -message "Finished build of SASS"