import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24605001"))
    API_HASH = os.environ.get("API_HASH", "87329f36a6c08d50c2b4285f221e0c95")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGakJSMLvJK2X9PeR1FkIjVPEplr3bH_1M")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzMBuylazK4IQjotjvS2_qAWXvMcy61jZJLtAFzA8kI3jQNwFbFPxJfGHRhLCtxYIUACVZMAwWd_d0Z1PVdw9oFjMlJQ9Aumw5BZ7W8ZvwrzEmmJJ-v5b0FvuEI51203bwaUrTsob90VLMLi2ZBt5M7kzlxcG3eJR_bDMiK7FFZtySSQxFTVAQEdVaiNaF3NyGlD0Sf8FGlc1eQz1x5T3Odr6lf2384r1SVsQIfjRHss3Z1LHCxhjQ7p1gmJ4mnKeymue_fAydq2zdpVLhfzu2ak8uIrieDKuCCJmUwVs25L1Zg9wcQn9jVubbtTUABbt-lPHs9Aj1Na6w1aMrX0tP8nIF8=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("Darshana_Music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Hrideyam_Chat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "About_Kailas") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("5779524475")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
