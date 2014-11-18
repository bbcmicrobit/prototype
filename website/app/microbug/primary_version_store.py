from filelock import FileLock, Timeout
import os
import settings
import uuid


class PrimaryVersionStore:
    def __init__(self, root_directory):
        self._root_directory = root_directory
        if not os.path.isdir(root_directory):
            raise Exception("Primary version store cannot find directory '%s'" % root_directory)

    # Retrieves the item with the specified base filename (not including .json suffix
    def retrieve(self, base_filename):
        filename = os.path.join(self._root_directory, "{0}.json".format(base_filename))
        with open(filename, 'r') as file:
            return file.read()

    # Prepares a new version, reserving the ID and UUID
    def reserve_new_id(self):
        # Create new numeric IDs and UUIDs
        numeric_id = self._allocate_next_free_integer()
        random_uuid = uuid.uuid1()

        return (numeric_id, random_uuid)

    # Writes a new version file out, returns a tuple containing the
    # numeric ID and the UUID.
    def write_new_version(self, data, numeric_id, random_uuid):
        # Build the output filename from all of the details we now have
        base_filename = "{0}_{1}.json".format(numeric_id, random_uuid)
        output_filename = os.path.join(self._root_directory, base_filename)

        # Write the actual file.
        f = open(output_filename, "w")
        f.write(str(data))
        f.flush()
        f.close()

        return numeric_id, random_uuid

    # Return the next free ID for saving version files
    def _allocate_next_free_integer(self):
        highest_file_name = os.path.join(self._root_directory, 'highest.txt')
        lock_file_name = os.path.join(self._root_directory, 'highest.lock')

        # Obtain the file lock
        try:
            lock = FileLock(lock_file_name)
            with lock.acquire(timeout=settings.FILELOCK_TIMEOUT):
                # Read the existing version
                f = open(highest_file_name)
                r = f.read()
                r = r.strip()
                top_id = int(r)
                f.close()

                # Increment the counter and write the file
                top_id += 1
                f = open(highest_file_name,"w")
                f.write(str(top_id))
                f.close()
        except Timeout:
            raise "Could not aquire filelock on '%s'" % lock_file_name

        return top_id
