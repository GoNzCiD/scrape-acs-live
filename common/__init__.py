import os

# General
TIMER = int(os.getenv("TIMER", "30"))
OUTPUT_METHOD = "dropbox"  # values: dropbox, file_system

# Scrapper
SERVER_URL = os.getenv("SERVER_URL")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
MULTISERVER_ID = os.getenv("MULTISERVER_ID")
WINDOWS_CHROME_DRIVER_PATH = os.getenv("WINDOWS_CHROME_DRIVER_PATH", "./lib/chromedriver.exe")

# Output
FILE_SYSTEM_TO_PATH = os.getenv("OUTPUT_PATH")
DROPBOX_TOKEN = os.getenv("DROPBOX_TOKEN")
DROPBOX_TO_PATH = os.getenv("DROPBOX_TO_PATH")
