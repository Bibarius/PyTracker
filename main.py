import os, os.path
import datetime
from ctypes import *
import time
import serialize
import deserialize


def main():

    workingtime = 0
    programs = deserialize.deserialize()
    mylib = windll.LoadLibrary("main.dll")
    mylib.getProcessName.restype = c_char_p
    while True:
        if workingtime % 600 == 0:
            serialize.serialize(programs)
        response = mylib.getProcessName()
        name = response.decode('utf-8')
        if name == "error":
            continue
        if programs.get(name) != None:
            programs[name] = programs[name] + 5
            time.sleep(5)
            workingtime += 5
        else:
            programs[name] = 5
            time.sleep(5)
            workingtime += 5
        
    

    

if __name__ == "__main__":
    main()