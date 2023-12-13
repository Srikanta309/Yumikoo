import os
from os import getenv


API_ID = int(getenv("API_ID", "26004787"))
API_HASH = getenv("API_HASH", "962b5b15f88fd421fc17a483618216fc")
BOT_USERNAME = getenv("BOT_USERNAME", "Zexxop_bot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6433640374:AAFuliBBXEUd5hM7MyMOTnGmKLwOcBqNnsg")
OWNER_ID = int(getenv("OWNER_ID", "6715373877"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5560295791").split(I_am_srikanta)))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Srikanta:srikanta@cluster0.xzbil3m.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQGMzTMAl4uYC9i5CQLG4NSAqpyUWQHQSia_9VEU4bMbsqAy9gkbnKW9wjzl6KVfKVY0nGqXERs36uapoHp9EUQyRgjlahWcr7m7Mi0UzN7_5jwLqJ4z7OzgijDgzwCdYXOHLjRzVlc6Zm_3HM4A1h3FYcoZaEJC-6wR2x_y6lK5ilJx9RgmtOlh75_5hRQozxFnIdxfNLE-5rdDYLNJBPYNasU6XqDPcG_oWfaErDnuRfNHJ1OmimlRCTmGtfIbwQFTKXaPIG6mK6GZArjkq8O5kaMk1BbW5ar9waEhc6QrcC9qgeej6gfUWibX3lUVONPVViR3nThv6-W_7ZFElv-5p3vfCAAAAAGCECk3AA")
