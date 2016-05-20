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

import os
import re
import logging

# Recompile a regex to extract the leading digits
leading_spaces_regex = re.compile('^(\d+)')

# Get the logger for these views
logger = logging.getLogger(__name__)

class PendingVersionStore:
    def __init__(self, root_directory):
        self._root_directory = root_directory
        if not os.path.isdir(root_directory):
            raise Exception("Pending version store cannot find directory '%s'" % root_directory)

    # Writes a new version file out, this requires the numeric ID and random UUID
    # to already be created.
    def write_new_version(self, data, numeric_id, random_uuid):
        # Build the output filename from all of the details we now have
        base_filename = "{0}_{1}.py".format(numeric_id, random_uuid)
        output_filename = os.path.join(self._root_directory, base_filename)

        # Write the actual file.
        f = open(output_filename, "w")
        f.write(str(data))
        f.flush()
        f.close()

    # Returns a list of items which will be processed before the item provided.
    # Note: This does not check the item itself is in the list!
    def items_before(self, item):
        item_index = self._leading_integer(item)
        return [
                   filename
                   for filename in os.listdir(self._root_directory)
                   if (filename != "README")   and (self._leading_integer(filename) < item_index)
        ]

    # If a string has leading digits return them as integer, if not throw an error
    def _leading_integer(self, string):
        match = leading_spaces_regex.match(string)
        if match:
            return int(match.group())
        else:
            raise Exception("Cannot find leading integer for '%s'" % string)