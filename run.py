import json
import logging
import time
from datetime import datetime

from assetto_server_scrapper.assetto_server_browser import AssettoServerBrowser
from common import DROPBOX_TOKEN, FILE_SYSTEM_TO_PATH, DROPBOX_TO_PATH, OUTPUT_METHOD
from common import TIMER
from common.utils import trim_html
from uploaders.dropbox_transfer import DropBoxTransfer
from uploaders.file_system import FileSystem

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    with AssettoServerBrowser() as browser:
        try:
            while True:
                logging.debug("Scrapping data...")
                live, live_disconnected = browser.get_living_time()
                if len(live) < 1 and len(live_disconnected) < 1:
                    logging.error("Cannot read any registry!")
                else:
                    data = {"table": "{}<hr>{}<hr><p style='text-align:right'>Actualizado a: {}</p>".format(
                            trim_html(live),
                            trim_html(live_disconnected),
                            datetime.now().strftime("%d-%m-%Y %H:%M:%S"))}

                    if OUTPUT_METHOD == "file_system":
                        FileSystem.copy(data, FILE_SYSTEM_TO_PATH)
                    elif OUTPUT_METHOD == "dropbox":
                        dropbox = DropBoxTransfer(DROPBOX_TOKEN)
                        dropbox.upload_file(json.dumps(data).encode('utf-8'), DROPBOX_TO_PATH)
                time.sleep(TIMER)
        except KeyboardInterrupt:
            logging.info("Exiting...")
            exit()
