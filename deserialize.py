import os, os.path
import datetime
import json

def deserialize():
    now = datetime.datetime.now()
    today = str(now.year) + "." + str(now.month) + "." + str(now.day) + ".json"

    for i in os.listdir("database"):
        if i == today:
            with open("database/" + today, "r") as read_file:
                programs = json.load(read_file)
                return programs
    return {}