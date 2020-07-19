import json
import logging


class FileSystem:
    @staticmethod
    def copy(data, copy_to):
        with open(copy_to, 'w') as file:
            logging.debug("Saving data to file system: {}".format(copy_to))
            json.dump(data, file)
