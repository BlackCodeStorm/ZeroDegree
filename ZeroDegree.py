# -*- coding: utf-8
import time
import core
import os
import start
from sys import argv,path
from modules import output
from modules import public
from modules import record
from modules import updata
HISTORY             = []
ROOT_PATH           = __file__[:-13]
ATTACK_MODULES_PATH = "".join((ROOT_PATH,"attack\\"))
LOGS_SAVE_PATH      = "".join((ROOT_PATH,"logs\\"))
NOW_DATE            = "-".join((str(time.localtime()[0]),str(time.localtime()[1]),str(time.localtime()[2])))
path.append(ATTACK_MODULES_PATH)

def main(zerodegree,logs):
    while True:
        info = public.format(input("\033[97m[\033[94m#Z\033[97m]\033[94m-\033[97mmodule(\033[94m" + zerodegree.ModuleName + "\033[97m)>"))
        HISTORY.append(info)
        zerodegree.inDebugData("history",HISTORY)
        if info == [""]:
            pass
        elif info == ["exit"]:
            logs.writeLog(3, "The ZeroDegree Framework Is Exit!")
            exit()
        else:
            i = zerodegree.processing_attack_command(info)
            i = zerodegree.processing_frame_command(info, i)
            i = zerodegree.processing_subframe_command(info,i)
            if i == 1:
                output.error("There is no command!,Input \"help\" to get help")
            elif i != 0:
                logs.writeLog(0, "".join(("Attack Is Error!Error Code:", str(i))))

def set_and_run():
    os.system("reset")
    zerodegree = core.ZeroDegree()
    logs = record.logs()
    logs.setLogSaveFile("".join((LOGS_SAVE_PATH,"runlogs.log")))
    import traceback
    zerodegree.setLogs(logs)
    logs.writeLog(3, "The ZeroDegree Framework Is Run!")
    try:
        main(zerodegree,logs)
    except Exception as e:
        print("\nFOUND A FATAL ERROR,QUITING!")
        temp = traceback.format_exc().split("\n")
        logs.writeLog(4, "Debug Information:")
        for i in temp:
            logs.writeLog(5,i)

if __name__ == "__main__":
    set_and_run()