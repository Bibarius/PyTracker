#define _WIN32_WINNT 0x0600 
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <Psapi.h>
#include <string.h>

HWND ForeGroundWindow;      //  HANDLE  окна, на котором в данный момент фокус
DWORD ProcessId;            //  id процесса, которому принадлежит данное окно
HANDLE hOpenProcess;        //  HANDLE этого процесса

DWORD size = MAX_PATH;
DWORD Error;  
LPTSTR path;   
    

//для времени
FILETIME CreationTime;
FILETIME ExitTime;
FILETIME KernelTime;
FILETIME UserTime;

SYSTEMTIME ProcessTime;
SYSTEMTIME CurrentTime;

//для строк
char *Slash;
const char *Path;

char* getProcessName()
{
    path = malloc(sizeof(WCHAR[MAX_PATH]));      //  выделяем память для строки с названием программы
    DWORD charsCarried = MAX_PATH;

    ForeGroundWindow = GetForegroundWindow();
    if(!(GetWindowThreadProcessId(ForeGroundWindow, &ProcessId)))       //получаем процесс, который запустил окно, на котором сейчас фокус
    {
        printf("error getting the process-ownre of the window\n");
        free(path);
    }    
    if(!(hOpenProcess = OpenProcess(PROCESS_ALL_ACCESS | PROCESS_QUERY_INFORMATION, FALSE, ProcessId)))     //получаем HANDLE этого процесса
    {
        printf("error oppening the process-owner\n");
        free(path);
    }
    if(!(QueryFullProcessImageNameA(hOpenProcess, 0, path, &charsCarried)))
    {
        printf("error querying process-owner name\n");
        free(path);
    }
    else
    {
        Path = path;
        Slash = strrchr(Path, 92); Slash++;            
        printf("\n\nCurrent working program is: %s\n", Slash);
        return Slash;
        free(path);
        }        
}

