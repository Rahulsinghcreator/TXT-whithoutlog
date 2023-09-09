import os

API_ID = API_ID = 23539681

API_HASH = os.environ.get("API_HASH", "ae1430184ae21aa81b4b030d1bd75885")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6579050638:AAGMNgM15JFQKxCTrxJYID-f48ELUCa0a3c")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5007135395))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5007135395").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


