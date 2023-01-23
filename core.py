import sys
import netifaces
from modules import output
from modules import public
from lib import library
from lib import setting
class ZeroDegree:
    def __init__(self):
        self.ModState      = False                               #Show the module if load
        self.ModName       = "no module"                         #Storage the module's name
        self.Module        = ""                                  #Storage the module's object
        self.ModInf        = public.parse("info/module.zf")      #A dictionary object to storage the module's infomation: name - path
        self.SubframeInf   = public.parse("info/subframework.zf")#A dictionary object to storage the subframework's infomation: name - path
        self.ScriptInf     = public.parse("info/script.zf")      #A dictionary object to storage the script's infomation: name - path
        self.ModPath       = "/"                                 #Storage the module storage path
        self.LogPath       = "/"                                 #Storage the Logs storage path
        self.RootPath      = "/"                                 #Storage the root path for ZeroDegree path
        self.ScriptPath    = "/"                                 #Storage the script's path
        self.RunLogs       = ""                                  #Storage the runing log's object
        self.SubLogs       = ""                                  #Storage the Subframe log's object
        self.AttLogs       = ""                                  #Storage the Attack log's object
        self.ModIndexCache = []                                  #Used to the command"use" with index
        self.ShowList = {
            "options":self.__showOptions,
            "modules":self.__showModules,
            "scripts":self.__showScripts,
            "subframes":self.__showSubframes,
            "framework":self.__showFramework,
        }
        self.AttackCommand = {
            "set": self._set,
            "show": self._show,
            "open": self._open,
            "close": self._close,
            "use": self._use,
            "run": self._run,
        }
        self.FrameCommand = {
            "help": self._help,
            "info":self._info,
        }

    def setLogs(self,runlogs,sublogs,attlogs):
        self.RunLogs = runlogs
        self.SubLogs = sublogs
        self.AttLogs = attlogs
    def setPath(self,root,attack,logs,subframe,script):
        self.RootPath = root
        self.ModPath = attack
        self.LogPath = logs
        self.SubframePath = subframe
        self.ScriptPath = script

    def __showOptions(self):
        pass
    def __showFramework(self):
        print("")
        print("Version\033[94m:\033[97m1.0.00                                 ")
        print("Writer\033[94m:\033[97mAlpha                                   ")
        print("Repository\033[94m:\033[97mgithub.com/BlackCodeStorm/ZeroDegree")
        print("This is an open-source penetration framework                   ")
        print("")
    def __showScripts(self):
        if len(self.ScriptInf["name"]) == 0:
            print(library.NoThing)
            output.worry("That doesn't seem like anything!")
            print("")
        else:
            t = []
            for tp in self.ScriptInf["name"]:
                t.append(len(tp))
            print("\nThere are %s scripts in framework!" % len(self.ScriptInf["name"]))
            print("Scripts:\n\033[94m=======\033[97m")
            print("\t# name%swriter"%(" "* (max(t) -3 )))
            print("\t\033[94m- ----%s------\033[97m"%(" " * (max(t) - 3)))
            for i in range(len(self.ScriptInf["name"])):
                print("\t> %s%s%s"%(self.ScriptInf["name"][i],
                                    " "*(max(t) - len(self.ScriptInf["name"][i]) + 1),
                                    self.ScriptInf["writer"][i]))
            print("")
    def __showSubframes(self):
        if len(self.SubframeInf["name"]) == 0:
            print(library.NoThing)
            output.worry("That doesn't seem like anything!")
            print("")
        else:
            t = []
            for tp in self.SubframeInf["name"]:
                t.append(len(tp))
            print("\nThere are %s subframes in framework!" % len(self.SubframeInf["name"]))
            print("Subframes:\n\033[94m=========\033[97m")
            print("\t# name%swriter" % (" " * (max(t) - 3)))
            print("\t\033[94m- ----%s------\033[97m" % (" " * (max(t) - 3)))
            for i in range(len(self.SubframeInf["name"])):
                print("\t> %s%s%s" % (self.SubframeInf["name"][i],
                                      " " * (max(t) - len(self.SubframeInf["name"][i]) + 1),
                                      self.SubframeInf["writer"][i]))
            print("")
    def __showModules(self):
        if len(self.ModInf["name"]) == 0:
            print(library.NoThing)
            output.worry("That doesn't seem like anything!")
            print("")
        else:
            self.ModIndexCache = self.ModInf["name"]
            t = []
            for tp in self.ModInf["name"]:
                t.append(len(tp))
            print("\nThere are %s modules in framework!" % len(self.ModInf["name"]))
            print("Modules:\n\033[94m=======\033[97m")
            print("\t# name%swriter" % (" " * (max(t) - 3)))
            print("\t\033[94m- ----%s------\033[97m" % (" " * (max(t) - 3)))
            for i in range(len(self.ModInf["name"])):
                print("\t> %s%s%s" % (self.ModInf["name"][i],
                                      " " * (max(t) - len(self.ModInf["name"][i]) + 1),
                                      self.ModInf["writer"][i]))
            print("")
    def _show(self, command):      #<---need to edit or charge!!!
        if len(command) != 2:
            output.info("\nSyntax: show \"options\"")
            output.info("You also can use: show \"index\"\n")
            print("Available options:")
            print("\033[94m=================\033[97m")
            for i in list(self.ShowList.keys()):
                print("\033[94m\t> \033[97m" + i)
            print("")
        else:
            if command[1] in self.ShowList:
                self.ShowList[command[1]]()
            else:
                output.error("The item was not found!")
    def _set(self, command):
        if len(command) == 1:
            if self.ModState == False:
                output.error("\nThe module is no load!")
                output.info("Syntax: set \"options\" \"value\"\n")
                return
            output.info("\nSyntax: set \"options\" \"value\"\n")
            print("Available options:")
            print("\033[94m=================\033[97m")
            for i in list(self.Module.project.keys()):
                for a in list(self.Module.project[i].keys()):
                    print("\033[96m\t> \033[97m" + a)
            print("")
        else:
            if self.ModState == False:
                output.error("\nThe module is no load!")
                output.info("Syntax: set \"options\" \"value\"\n")
                return
            self.Module.setTheOption(command[1], command[2])
    def _open(self, command):
        if self.ModState == False:
            output.error("\nThe module in no load!")
            output.info("Syntax: open \"options\"\n")
            return
        if len(command) != 2:
            output.error("\nSyntax error!")
            output.info("Syntax: open \"options\"\n")
        else:
            self.Module.openTheOption(command[1])
    def _close(self, command):
        if self.ModState == False:
            output.error("\nThe module in no load!")
            output.info("Syntax: close \"options\"\n")
            return
        if len(command) != 2:
            output.error("\nSyntax error!")
            output.info("Syntax: close \"options\"\n")
        else:
            self.Module.closeTheOption(command[1])
    def _use(self, command):
        if len(command) != 2:
            output.info("\nSyntax: use \"options\"")
            output.info("You also can use: use \"index\"\n")
        else:
            data = command[1]
            if data in self.ModInf["name"]:
                tp = list(self.ModInf["name"])
                t = self.ModInf["file"][tp.index(command[1])].split("/")
                del t[0]
                name = t.pop(-1)[0:-3]
                sys.path.append("".join((self.ModPath,"/".join(t))))
                temp = __import__(name)
                self.Module = temp.Entrance(self.AttLogs)
                self.ModName = command[1]
                self.ModState = True
                del sys.path[-1]
                output.info("The module is loaded successfully!")
            else:
                try:
                    index = int(command[1])
                    data = self.ModIndexCache[index]
                    if data in self.ModInf["name"]:
                        tp = list(self.ModInf["name"])
                        t = self.ModInf["file"][tp.index(data)].split("/")
                        del t[0]
                        name = t.pop(-1)[0:-3]
                        sys.path.append("".join((self.ModPath, "/".join(t))))
                        temp = __import__(name)
                        self.Module = temp.Entrance(self.AttLogs)
                        self.ModName = data
                        self.ModState = True
                        del sys.path[-1]
                        output.info("The module is loaded successfully!")
                    else:
                        output.error("The module is no find,please check the input!")
                except:
                    output.error("The module is no find,please check the input!")
    def _run(self, command):
        if self.ModState == False:
            output.error("The module in no load!")
            return
        output.info("\nStart attack!")
        self.Module.run_the_attack()
        output.info("The attack is finish.\n")
    def _help(self):
        print("\033[97m")
        print(setting.help)
        print("")
    def _info(self):
        show = {
            "Infomation":{
                "Module":{
                    "flag":0,
                    "info":{},
                },
                "Network":{
                    "flag":1,
                    "info":{},
                },
            },
            "setting":{
                "Frame Path":{
                    "flag":0,
                    "info":{
                        "ROOT PATH":self.RootPath,
                        "ATTACK MODULE PATH":self.ModPath,
                        "LOG PATH":self.LogPath,
                        "SUBFRAME PATH": self.SubframePath,
                        "SCRIPTS PATH": self.ScriptPath,
                    },
                },
            },
        }
        if self.ModState:
            show["Infomation"]["Module"]["info"] = {}
        else:
            show["Infomation"]["Module"]["info"] = {"NAME":"no load!"}
        faces = netifaces.interfaces()
        for face in faces:
            info = netifaces.ifaddresses(face)
            show["Infomation"]["Network"]["info"][face] = {
                "IPv4 ADDRES": info[2][0]["addr"],
                "IPv6 ADDRES": info[10][0]["addr"],
                "MAC ADDRES" : info[17][0]["addr"],
                "IPv4 NETMASK": info[2][0]["netmask"],
                "IPv6 NETMASK": info[10][0]["netmask"],
            }
        print("")
        public.funshow(show)

    def processingAttackCommand(self, command):
        if command[0] in list(self.AttackCommand.keys()):
            self.AttackCommand[command[0]](command)
        else:
            return 1
        return 0
    def processingFrameCommand(self, command, i):
        if i == 1:
            if command[0] in list(self.FrameCommand.keys()):
                self.FrameCommand[command[0]]()
            else:
                return 1
        else:
            return i
        return 0
    def processingScriptCommand(self, command, i):
        if i == 1:
            if command[0][1:] in self.ScriptInf["name"] and command[0][0] == "#":
                tp = list(self.ScriptInf["name"])
                t = self.ScriptInf["file"][tp.index(command[0][1:])].split("/")
                del t[0]
                name = t.pop(-1)[0:-3]
                sys.path.append("".join((self.ScriptPath, "/".join(t))))
                script = __import__(self.ScriptInf["file"][tp.index(command[0][1:])].split("/")[-1][:-3])
                script.start()
                del sys.path[-1]
            else:
                if command[0][0] == "#":
                    output.error("There is no script!")
                    output.error("Input \"show scripts\" to get scripts list!")
                    return 0
                else:
                    return 1
        else:
            return i
        return 0
    def processingSubframeCommand(self, command, i):
        if i == 1:
            if command[0] in self.SubframeInf["name"]:
                tp = list(self.SubframeInf["name"])
                t = self.SubframeInf["file"][tp.index(command[0])].split("/")
                del t[0]
                name = t.pop(-1)[0:-3]
                sys.path.append("".join((self.SubframePath, "/".join(t))))
                subframe = __import__(self.SubframeInf["file"][tp.index(command[0])].split("/")[-1][:-3])
                output.info("The subframe is loaded successfully!")
                subframe.start(self,self.SubLogs)
                del sys.path[-1]
            else:
                return 1
        else:
            return i
        return 0