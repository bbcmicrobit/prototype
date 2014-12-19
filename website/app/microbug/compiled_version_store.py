import os


class CompiledVersionStore:
    def __init__(self, root_directory):
        self._root_directory = root_directory
        if not os.path.isdir(root_directory):
            raise Exception("Pending version store cannot find directory '%s'" % root_directory)

    # Returns a boolean indicating whether the provided item is in the store or not.
    def contains(self, base_filename):
        # Build the output filename from all of the details we now have
        return os.path.exists(self._full_filename(base_filename))

    # Returns the full .hex contents, or None if the file doesn't exist
    def hex(self, base_filename):
        full_filename = self._full_filename(base_filename)
        if not os.path.exists(full_filename):
            return None
        # Read the existing version
        file = open(full_filename)
        contents = file.read()
        file.close()
        return contents

    # Returns the full filename for a base filename
    def _full_filename(self, base_filename):
        base_filename = "{0}.hex".format(base_filename)
        return os.path.join(self._root_directory, base_filename)


class FailedCompiledVersionStore:
    def __init__(self, root_directory):
        self._root_directory = root_directory
        if not os.path.isdir(root_directory):
            raise Exception("Pending version store cannot find directory '%s'" % root_directory)

    # Returns a boolean indicating whether the provided item is in the store or not.
    def contains(self, base_filename):
        # Build the output filename from all of the details we now have
        return os.path.exists(self._full_filename(base_filename))

    # Returns the full filename for a base filename
    def _full_filename(self, base_filename):
        base_filename = "{0}.py".format(base_filename)
        return os.path.join(self._root_directory, base_filename)
