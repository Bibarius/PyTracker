from ctypes import *

def main():
    mylib = windll.LoadLibrary("c_win32/main.dll")
    mylib.getProcessName.restype = c_char_p
    while(True):
        name = mylib.getProcessName()
        print(name)
    

    

if __name__ == "__main__":
    main()