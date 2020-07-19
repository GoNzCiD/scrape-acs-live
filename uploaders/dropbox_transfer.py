import logging

import dropbox


class DropBoxTransfer:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_content, upload_to):
        """upload a file to Dropbox using API v2"""
        logging.debug("Uploading data to Dropbox: {}".format(upload_to))
        dbx = dropbox.Dropbox(self.access_token)
        dbx.files_upload(file_content, upload_to, mode=dropbox.files.WriteMode.overwrite)
        dbx.close()
