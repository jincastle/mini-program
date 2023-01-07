import platform
import os
import platform, psutil

def printOsinfo():
    print('OS : ', platform.system())
    print('version : ', platform.version())
    info = platform.uname()



def printSystemInfor():
    print('Process information  :\t', platform.processor())
    print('Process Architecture :\t', platform.machine())
    print('CPU Cores          :\t', os.cpu_count())
    print('RAM Size             :\t', str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + "(GB)")









if __name__ == "__main__":
    printSystemInfor()