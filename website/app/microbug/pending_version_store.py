import os


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
