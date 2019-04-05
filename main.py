from ctypes import *
import element
import request
import time

def main():
    programs = {}
    mylib = windll.LoadLibrary("c_win32/main.dll")
    mylib.getProcessName.restype = c_char_p
    while True:
        name = mylib.getProcessName()
        if programs.get(name) != None:
            programs[name] = programs[name] + 5
            print(time.strftime('%H:%M:%S', time.gmtime(programs[name])))
            time.sleep(5)
        else:
            programs[name] = 5
            time.sleep(5)
        
    

    

if __name__ == "__main__":
    main()