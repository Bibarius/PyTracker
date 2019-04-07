import datetime
import json

def serialize(programs):
    now = datetime.datetime.now()
    filename = str(now.year) + "." + str(now.month) + "." + str(now.day) + ".json"
    with open("database/" + filename, "w") as write:
        json.dump(dict(programs), write)
