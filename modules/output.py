_bg = {
    "black"    :"\033[40m",
    "red"      :"\033[41m",
    "green"    :"\033[42m",
    "orange"   :"\033[43m",
    "blue"     :"\033[44m",
    "purple"   :"\033[45m",
    "cyan"     :"\033[46m",
    "lightgrey":"\033[47m"
}
_fg = {
    "black"     :"\033[30m",
    "red"       :"\033[31m",
    "green"     :"\033[32m",
    "orange"    :"\033[33m",
    "blue"      :"\033[34m",
    "purple"    :"\033[35m",
    "cyan"      :"\033[36m",
    "lightgrey" :"\033[37m",
    "darkgrey"  :"\033[90m",
    "lightred"  :"\033[91m",
    "lightgreen":"\033[92m",
    "yellow"    :"\033[93m",
    "lightblue" :"\033[94m",
    "pink"      :"\033[95m",
    "lightcyan" :"\033[96m",
    "white"     :"\033[97m"
}
_styles = {
    "disable"      :"\033[02m",
    "reverse"      :"\033[07m",
    "strikethrough":"\033[09m",
    "invisible"    :"\033[08m",
    "reset"        :"\033[0m",
    "bold"         :"\033[01m",
    "underline"    :"\033[04m"
}

def error(string):
    str = []
    t = [""]
    for s in string:
        str.append(s)
    for s in str:
        if s == "\n":
            if "".join(t) != "":
                print("\033[91m[-] \033[97m" + "".join(t))
            t = [""]
            print("")
        else:
            t.append(s)
    if "".join(t) != "":
        print("\033[91m[-] \033[97m" + "".join(t))

def worry(string):
    str = []
    t = [""]
    for s in string:
        str.append(s)
    for s in str:
        if s == "\n":
            if "".join(t) != "":
                print("\033[93m[!] \033[97m" + "".join(t))
            t = [""]
            print("")
        else:
            t.append(s)
    if "".join(t) != "":
        print("\033[93m[!] \033[97m" + "".join(t))

def info(string):
    str = []
    t = [""]
    for s in string:
        str.append(s)
    for s in str:
        if s == "\n":
            if "".join(t) != "":
                print("\033[34m[*] \033[97m" + "".join(t))
            t = [""]
            print("")
        else:
            t.append(s)
    if "".join(t) != "":
        print("\033[34m[*] \033[97m" + "".join(t))

def find(string):
    str = []
    t = [""]
    for s in string:
        str.append(s)
    for s in str:
        if s == "\n":
            if "".join(t) != "":
                print("\033[94m[+] \033[97m"+"".join(t))
            t = [""]
            print("")
        else:
            t.append(s)
    if "".join(t) != "":
        print("\033[96m[+] \033[97m" + "".join(t))