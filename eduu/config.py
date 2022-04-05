# (c) @MytProGuardBot
# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/EduuRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "11044555"  # integer value, dont use ""
    API_HASH = "f43cdf13b9fec8e3da3c3a50397bad68"
    TOKEN = "5221029810:AAFm9b84F_JUXBp9T4b0RmQKKz9FgvO7C0M"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "2028948832"  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "meyitzade47"
    MONGO_PORT = get_int_key("27017")
    MONGO_DB_URI = get_str_key("MONGO_DB_URI")
    MONGO_DB = "AnosVoldigoad"
    SUPPORT_CHAT = "HirasetTR"  # Your own group for support, do not add the @
    LOG_CHAT = (
        -1001530510247
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001530510247
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
