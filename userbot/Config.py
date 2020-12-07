import os

from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os

    class Config(object):
        LOGGER = True
        # Get this value from my.telegram.org! Please do not steal
        ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
        # For customizing there alive message
        CUSTOM_ALIVE_TEXT = os.environ.get("CUSTOM_ALIVE_TEXT", None)
        CUSTOM_ALIVE_EMOJI = os.environ.get("CUSTOM_ALIVE_EMOJI", None)
        # for profile default name
        AUTONAME = os.environ.get("AUTONAME", None)
        # Get this value from my.telegram.org! Please do not steal
        APP_ID = int(os.environ.get("APP_ID", 6))
        API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
        STRING_SESSION = os.environ.get("STRING_SESSION", None)
        # For Databases
        DB_URI = os.environ.get("DATABASE_URL", None)
        SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get(
            "SCREEN_SHOT_LAYER_ACCESS_KEY", None
        )
        # string session for running on Heroku
        PM_DATA = os.environ.get("PM_DATA", "ENABLE")
        # some people upload their session files on GitHub or other third party hosting
        # websites, this might prevent the un-authorized use of the
        # confidential session files
        # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
        OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        # Send .get_id in any group to fill this value.
        PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", None)
        if PRIVATE_GROUP_BOT_API_ID:
            PRIVATE_GROUP_BOT_API_ID = int(PRIVATE_GROUP_BOT_API_ID)
        # same as  PRIVATE_GROUP_BOT_API_ID but set only if you need pmpermit
        PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
        if PRIVATE_GROUP_ID:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        PLUGIN_CHANNEL = os.environ.get("PLUGIN_CHANNEL", None)
        if PLUGIN_CHANNEL:
            PLUGIN_CHANNEL = int(PLUGIN_CHANNEL)
        # Send .get_id in any channel to fill this value. ReQuired for @Manuel15
        # inspiration to work!
        PRIVATE_CHANNEL_BOT_API_ID = os.environ.get("PRIVATE_CHANNEL_BOT_API_ID", None)
        if PRIVATE_CHANNEL_BOT_API_ID:
            PRIVATE_CHANNEL_BOT_API_ID = int(PRIVATE_CHANNEL_BOT_API_ID)
        # This is required for the speech to text plugin. Get your USERNAME from
        # https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
        IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
        IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
        # This is required for the @telegraph functionality.
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "mrconfused")
        # Set False to stop deleting old welcome messages
        CLEAN_WELCOME = os.environ.get("CLEAN_WELCOME", True)
        # github vars
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        # Get a Free API Key from OCR.Space
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        # TG API limit. An album can have atmost 10 media!
        TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        # Telegram BOT Token from @BotFather
        TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
        TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
        NO_LOG_P_M_S = bool(os.environ.get("NO_LOG_P_M_S", True))
        THUMB_IMAGE = os.environ.get(
            "THUMB_IMAGE", "https://telegra.ph/file/ca95524e4734b0d5461b5.jpg"
        )
        # Genius lyrics get this value from https://genius.com/developers both has
        # same values
        GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)
        # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
        # TG API limit. A message can have maximum 4096 characters!
        MAX_MESSAGE_SIZE_LIMIT = 4095
        # set blacklist_chats where you do not want userbot's features
        UB_BLACK_LIST_CHAT = {
            int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
        }

        # specify LOAD and NO_LOAD
        LOAD = []
        # foloowing plugins won't work on Heroku,
        # because of their ephemeral file system
        MAX_ANTI_FLOOD_MESSAGES = 10
        # warn mode for anti flood
        ANTI_FLOOD_WARN_MODE = ChatBannedRights(
            until_date=None, view_messages=None, send_messages=True
        )
        CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        # specify LOAD and NO_LOAD
        NO_LOAD = [x for x in os.environ.get("NO_LOAD", "").split()]
        # in alive message pic
        ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
        # in pm permit pic
        PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
        CUSTOM_PMPERMIT_TEXT = os.environ.get("CUSTOM_PMPERMIT_TEXT", None)
        # Get your own API key from https://www.remove.bg/ or
        # feel free to use http://telegram.dog/Remove_BGBot
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        # For Databases
        # can be None in which case plugins requiring
        # DataBase would not work
        DB_URI = os.environ.get("DATABASE_URL", None)
        # number of rows of buttons to be displayed in .help command
        NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(
            os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 7)
        )
        # number of rows of buttons to be displayed in .helpme command
        NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(
            os.environ.get("NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 3)
        )
        # emoji to be displayed in .help
        EMOJI_TO_DISPLAY_IN_HELP = os.environ.get("EMOJI_TO_DISPLAY_IN_HELP", " ")
        # specify command handler that should be used for the plugins
        # this should be a valid "regex" pattern
        COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\.")
        SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\.")
        HELP_INLINETYPE = os.environ.get("HELP_INLINETYPE", None)
        # specify list of users allowed to use bot
        # WARNING: be careful who you grant access to your bot.
        # malicious users could do ".exec rm -rf /*"
        SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
        # Google Drive ()
        CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
        CHROME_DRIVER = os.environ.get(
            "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
        )
        # Google Drive plugin
        G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
        G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
        G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
        G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
        G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
        TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads")
        # for heroku plugin
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
        # For transfer channel
        TELE_GRAM_2FA_CODE = os.environ.get("TELE_GRAM_2FA_CODE", None)
        # for sed plugin
        GROUP_REG_SED_EX_BOT_S = os.environ.get(
            "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
        )
        # rapidleech plugins
        DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
        # Google Chrome Selenium Stuff
        # taken from
        # https://github.com/jaskaranSM/UniBorg/blob/9072e3580cc6c98d46f30e41edbe73ffc9d850d3/sample_config.py#L104-L106
        TEMP_DIR = os.environ.get("TEMP_DIR", "./temp/")
        # spotify stuff
        DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
        SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX", None)
        SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS", None)
        SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME", None)
        LYDIA_API = os.environ.get("LYDIA_API", None)
        DEFAULT_NAME = os.environ.get("DEFAULT_NAME", None)
        # define "spam" in PMs
        MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 5))
        # leave this blank, should be automatically filled for Heroku.com users
        PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
        if PM_LOGGR_BOT_API_ID:
            PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
        # to work manager.py
        DUAL_LOG = os.environ.get("DUAL_LOG", False)
        YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
        # MONGOCLIENT = pymongo.MongoClient(MONGO_DB_URI)
        # MONGO = MONGOCLIENT.userbot
        # JustWatch Country
        WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "IN")
        TZ = os.environ.get("TZ", None)
        # RSS_POST_MSG_GROUP_ID = map(int, os.environ.get("RSS_POST_MSG_GROUP_ID", None).split())
        RSS_POST_MSG_GROUP_ID = os.environ.get("RSS_POST_MSG_GROUP_ID", None)
        if RSS_POST_MSG_GROUP_ID:
            RSS_POST_MSG_GROUP_ID = int(RSS_POST_MSG_GROUP_ID)
        # SpamWatch API you can get it from get api from http://t.me/SpamWatchBot?start=token
        SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
        # SpamWatch, CAS, SpamProtection ban Needed or not
        ANTISPAMBOT_BAN = os.environ.get("ANTISPAMBOT_BAN", False)
        # Deepai value can get from https://deepai.org/
        DEEP_AI = os.environ.get("DEEP_AI", None)
        # For custom stickerpack names
        CUSTOM_STICKER_PACKNAME = os.environ.get("CUSTOM_STICKER_PACKNAME", None)
        # Owner id to show profile link of given id as owner
        OWNER_ID = os.environ.get("OWNER_ID", None)
        if OWNER_ID:
            OWNER_ID = int(OWNER_ID)
        # Last.fm plugin
        BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
        DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
        LASTFM_API = os.environ.get("LASTFM_API", None)
        LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
        LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
        LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
        # time.py
        COUNTRY = str(os.environ.get("COUNTRY", ""))
        TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
        #  for updater plugin
        UPSTREAM_REPO_URL = os.environ.get(
            "UPSTREAM_REPO_URL", "https://github.com/PerU-MoNsteR/Eliza.git"
        )
        UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "master")
        # can get from https://coffeehouse.intellivoid.net/
        LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
        CHANGE_TIME = int(os.environ.get("CHANGE_TIME", 60))


else:

    class Config(object):
        DB_URI = None
        # Add your UniBorg Vars Here
