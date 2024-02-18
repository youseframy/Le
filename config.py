from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/79740d1eeb46b8a6e397d.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/J_wli")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Le_Yousef")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5811104893").split()))


FAILED = "https://telegra.ph/file/79740d1eeb46b8a6e397d.jpg"
