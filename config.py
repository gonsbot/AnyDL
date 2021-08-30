
import os
import time

class Config(object):


    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))
    
    API_HASH = os.environ.get("API_HASH")

    UPDATE_GROUP = "SPACEX_BOTS"

    TIME_GAP_STORE = {}

    DEFAULT_WATERMARK = ""

    TG_MAX_FILE_SIZE = 2097152000

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    TIME_GAP = int(os.environ.get("TIME_GAP"))

    DB_URI = os.environ.get("DATABASE_URL", "")

    USER_LOGS = int(os.environ.get("USER_LOGS"))

    FILES_TRACK = int(os.environ.get("FILES_TRACK"))

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DEFAULT_THUMBNAIL = os.environ.get("DEFAULT_THUMBNAIL", "https://placehold.it/90x90")
