import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1858870769:AAEJNQHDn2P7NKcJESEFGDwwyGO-iZwxjfY")

    APP_ID = int(os.environ.get("APP_ID", 3413890))

    API_HASH = os.environ.get("API_HASH", "4d309f9bb03ed141f5528b32f7866ad3")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "https://telegra.ph/file/d2372fe42ccf8c9273088.jpg")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "https://telegra.ph/file/d2372fe42ccf8c9273088.jpg")
