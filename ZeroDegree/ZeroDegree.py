# -*- coding: utf-8
# need to charge the </core.py/zerodegree.showOptions()>!
# need to edit the </lib/setting.help>!
import time
import core
import traceback
import threading
import keyboard
import os
import readline
from cheak import initFramework
from modules import output
from modules import public
from modules import record
initFramework()
HISTORY             = []
ROOT_PATH           = __file__[:-13]
ATTACK_MODULES_PATH = "".join((ROOT_PATH,"attack/"))
LOGS_SAVE_PATH      = "".join((ROOT_PATH,"logs/"))
SUBFRAME_PATH       = "".join((ROOT_PATH,"subframe/"))
SCRIPT_PATH         = "".join((ROOT_PATH,"scripts/"))
NOW_DATE            = "-".join((str(time.localtime()[0]),str(time.localtime()[1]),str(time.localtime()[2])))

def takeCommandHistory():
    tmp_index = len(HISTORY) - 1
    def processingKeybroadEvent(event):
        try:
            global tmp_index
            if event.event_type == "down":
                if event.name == "up":
                    print(HISTORY[tmp_index])
                    tmp_index -= 1
                if event.name == "down":
                    if tmp_index == len(HISTORY):
                        print(HISTORY[tmp_index])
                    else:
                        tmp_index += 1
                        print(HISTORY[tmp_index])
        except:
            pass
    keyboard.hook(processingKeybroadEvent)

def main(zerodegree,logs):
    while True:
        info = public.format(input("\033[97m[\033[94mmain\033[97m\033[94m \033[97mmodule(\033[94m" + zerodegree.ModName + "\033[97m)]\033[94m#\033[97m"))
        HISTORY.append(info)
        if info == [""]:
            pass
        elif info == ["exit"]:
            logs.writeLog(3, "The ZeroDegree Framework Is Exit!")
            os.system("clear")
            exit()
        else:
            i = zerodegree.processingAttackCommand(info)
            i = zerodegree.processingFrameCommand(info, i)
            i = zerodegree.processingSubframeCommand(info, i)
            i = zerodegree.processingScriptCommand(info, i)
            if i == 1:
                output.error("There is no command!,Input \"help\" to get help")

def set_and_run():
    zerodegree = core.ZeroDegree()
    commandhistory = threading.Thread(target=takeCommandHistory)
    runlogs = record.logs()
    sublogs = record.logs()
    attlogs = record.logs()
    runlogs.setLogSaveFile("".join((LOGS_SAVE_PATH,"runlogs.log")))
    sublogs.setLogSaveFile("".join((LOGS_SAVE_PATH, "sublogs.log")))
    attlogs.setLogSaveFile("".join((LOGS_SAVE_PATH, "attlogs.log")))
    zerodegree.setLogs(runlogs,sublogs,attlogs)
    zerodegree.setPath(ROOT_PATH,ATTACK_MODULES_PATH,LOGS_SAVE_PATH,SUBFRAME_PATH,SCRIPT_PATH)
    commandhistory.start()
    runlogs.writeLog(3, "The ZeroDegree Framework Is Run!")
    try:
        main(zerodegree,runlogs)
    except Exception as e:
        os.system("clear")
        output.error("FOUND A FATAL ERROR,QUITING!")
        temp = traceback.format_exc().split("\n")
        runlogs.writeLog(4, "Debug Infomation:")
        for i in temp:
            runlogs.writeLog(5,i)
    except:
        runlogs.writeLog(3, "The ZeroDegree Framework Is Exit!")
        os.system("clear")
        output.info("Goodbye~")

if __name__ == "__main__":
    set_and_run()