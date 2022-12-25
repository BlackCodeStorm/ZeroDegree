from modules import output
from lib import attack
from lib import data
from lib import frameinfo
import traceback
import subprocess
class ZeroDegree:
    def __init__(self):
        self.ModuleState = False           #THIS USE TO THE MODULE!#
        self.ModuleList = attack.mlist     #THIS USE TO THE MODULE!#
        self.ModuleName = "no module"      #THIS USE TO THE MODULE!#
        self.Module = ""                   #THIS USE TO THE MODULE!#
        self.Logs = ""
        self.DebugData = {
            "history":[],
        }
        self.show_list = {
            "OPTIONS":None,
            "MODULES":attack.mlist,
            "USER-AGENTS":data.ua,
        }
        self.attack_command = {
            "set": self._set,
            "show": self._show,
            "open": self._open,
            "close": self._close,
            "use": self._use,
            "run": self._run,
        }
        self.frame_command = {
            "help": self._help,
            "updata": self._updata,
            "setting":self._setting,
        }

    def __del__(self):
        self.Logs.writeLog(4,"COMMAND HISTORY")
        for i in self.DebugData["history"]:
            self.Logs.writeLog(5," ".join(i))

    def setLogs(self,logs):
        self.Logs = logs

    def inDebugData(self,item,data):
        self.DebugData[item] = data

    def _show(self, command):
        if len(command) == 1:
            output.info("\nSyntax: show \"options\"")
            output.info("You also can use: show \"index\"\n")
            print("Available options:\n")
            for i in list(self.show_list.keys()):
                print("\033[94m\t> \033[97m" + i)
            print("")
        elif len(command) == 2:
            if command[1].upper() == "OPTIONS":
                if self.ModuleState == False:
                    output.error("The module in no load!")
                    return
                for classify in list(self.Module.project.keys()):
                    print("\033[97m")
                    print(classify.upper() + ":")
                    print("\033[94m=" * len(classify))
                    print(
                        "\033[97m\t# name               state value                                              description")
                    print(
                        "\t\033[94m- ----               ----- -----                                              -----------\033[97m")
                    for options in self.Module.project[classify].keys():
                        print("\t> " + options.upper() + " " * (19 - len(options)) +
                              self.Module.project[classify][options][1] + " " * (
                                          6 - len(self.Module.project[classify][options][1])), end="")
                        a = "".join((self.Module.project[classify][options][0],
                                     " " * (50 - len(self.Module.project[classify][options][0]) % 50)))
                        b = "".join((self.Module.project[classify][options][2],
                                     " " * (50 - len(self.Module.project[classify][options][2]) % 50)))
                        aa = []
                        bb = []
                        for i in range(int(len(a) / 50)):
                            aa.append(a[(i * 50):50 * (i + 1)])
                        for i in range(int(len(b) / 50)):
                            bb.append(b[(i * 50):50 * (i + 1)])
                        aaa = len(a)
                        bbb = len(b)
                        if aaa > bbb:
                            for i in range(int((aaa - bbb) / 50)):
                                bb.append(" " * 50)
                        elif bbb > aaa:
                            for i in range(int((bbb - aaa) / 50)):
                                aa.append(" " * 50)
                        else:
                            pass
                        print(aa[0] + " " + bb[0])
                        for i in range(len(aa)):
                            if i == 0:
                                continue
                            print(" " * 31 + aa[i] + " " + bb[i])
                        print("")
                    
            elif command[1].upper() in list(self.show_list.keys()):
                print("")
                print("\033[97mThe %s list:\n=========="%command[1].upper()+"="*len(command[1].upper()))
                print("")
                print("\t# NAME\n\t\033[94m- ----\033[97m")
                for i in self.show_list[command[1].upper()]:
                    print("\t> "+i)
                
            else:
                output.error("The item was not found!")
        else:
            output.error("Syntax error, please check the syntax!")
    def _set(self, command):
        if len(command) == 1:
            if self.ModuleState == False:
                output.error("\nThe module is no load!")
                output.info("Syntax: set \"options\" \"value\"\n")
                return
            output.info("\nSyntax: set \"options\" \"value\"\n")
            print("Available options:")
            for i in list(self.Module.project.keys()):
                for a in list(self.Module.project[i].keys()):
                    print("\033[96m\t\t> \033[97m" + a)
            print("")
        else:
            if self.ModuleState == False:
                output.error("\nThe module is no load!")
                output.info("Syntax: set \"options\" \"value\"\n")
                return
            self.Module.set_the_option(command[1], command[2])
    def _open(self, command):
        if self.ModuleState == False:
            output.error("The module in no load!")
            return
        if len(command) == 2:
            self.Module.open_the_option(command[1])
        else:
            output.error("Syntax error, please check the syntax!")
    def _close(self, command):
        if self.ModuleState == False:
            output.error("The module in no load!")
            return
        if len(command) == 2:
            self.Module.close_the_option(command[1])
        else:
            output.error("Syntax error, please check the syntax!")
        pass
    def _use(self, command):
        if len(command) == 2:
            data = command[1]
            if data in self.ModuleList:
                temp = __import__("".join((data, ".main")))
                self.Module = temp.main.Entrance()
                self.ModuleName = command[1]
                self.ModuleState = True
                output.info("The module is loaded successfully!")
            else:
                output.error("The module is no find,please check the input!")
        else:
            output.error("Syntax error, please check the syntax!")
    def _run(self, command):
        if self.ModuleState == False:
            output.error("The module in no load!")
            return
        output.info("\nStart attack!")
        info = self.Module.run_the_attack()
        if info != 0:
            info = str(info)
            output.error("Attack Is Error!Error Code:%s\n" % info)
            return info
        output.info("The attack is successful.\n")
    def _help(self):
        print("\033[97m")
        print(frameinfo.help)
        print("")
        
    def _updata(self):
        pass
    def _setting(self):
        pass

    def processing_attack_command(self, command):
        if command[0] in list(self.attack_command.keys()):
            self.attack_command[command[0]](command)
        else:
            return 1
        return 0
    def processing_frame_command(self, command, i):
        if i == 1:
            if command[0] in list(self.frame_command.keys()):
                self.frame_command[command[0]]()
            else:
                return 1
        else:
            return i
        return 0
    def processing_subframe_command(self, command, i):
        if i == 1:
            if command[0] in list(self.frame_command.keys()):
                pass
            else:
                return 1
        else:
            return i
        return 0