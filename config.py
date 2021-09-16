import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1858870769:AAEJNQHDn2P7NKcJESEFGDwwyGO-iZwxjfY")

    APP_ID = int(os.environ.get("APP_ID", 2987477))

    API_HASH = os.environ.get("API_HASH", "fab0ac420d45ae0aea6be644017b5c4e")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "https://telegra.ph/file/d2372fe42ccf8c9273088.jpg")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "https://telegra.ph/file/d2372fe42ccf8c9273088.jpg")
