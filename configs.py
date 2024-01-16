import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 20681593))
    API_HASH = os.environ.get("API_HASH", "379596c99399dffbf5cd00f1242ec60c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6733186557:AAEZ_fLnfT3N3Dq4Mxyl_FFs6S0kuTTSLyo")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Captcha-Bot")
    GROUP_CHAT_ID = int(os.environ.get("GROUP_CHAT_ID", -1001665155031))
