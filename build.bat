@echo off
cd c_win32
gcc -m32 -c main.c
gcc -m32 -shared -o main.dll main.o
COPY main.dll "../main.dll"
