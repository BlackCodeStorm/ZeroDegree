def format(info):
    tempstate = False
    tempcount = 0
    tempstring = []
    if info == "":
        return [""]
    for i in info:
        tempstring.append(i)
    while True:
        if tempstring[tempcount] == " ":
            if tempstate == False:
                tempstate = True
                tempcount += 1
            else:
                tempstring.pop(tempcount)
        else:
            tempcount += 1
            tempstate = False
        if tempcount == len(tempstring):
            break
    if "".join(tempstring) == " ":
        return [""]
    templen = len(tempstring)
    while True:
        if "".join(tempstring) == " ":
            break
        templen -= 1
        if tempstring[templen] == " ":
            tempstring.pop(templen)
            templen -= 1
        else:
            break
    return "".join(tempstring).split(" ")

def parse(FileName):
    result = {}
    tp_r = []
    f = open(FileName,"r")
    l = len(f.readlines()) - 1
    f = open(FileName,"r")
    tp_item = f.readline().split(" ")
    for i in tp_item:
        result[i] = ()
        tp_r.append([])
    result[list(result.keys())[-1][:-1]] = ()
    del result[list(result.keys())[-2]]
    for i in range(l):
        t = f.readline().split(" ")
        for a in range(len(t)):
            tp_r[a].append(t[a])
    for i in range(len(tp_r[-1])):
        if [tp_r[-1][i][-1]] == ["\n"]:
            tp_r[-1][i] = tp_r[-1][i][:-1]
        else:
            tp_r[-1][i] = tp_r[-1][i]
    t = list(result.keys())
    for i in range(len(t)):
        result[t[i]] = tuple(tp_r[i])
    return result

def funshow(struct): #<---need to edit!!!
    for type in list(struct.keys()):
        for title in list(struct[type].keys()):
            if struct[type][title]["flag"] == 0:
                numbers = []
                for number in list(struct[type][title]["info"].keys()):
                    numbers.append(len(number))
                maxlen = max(numbers)+1
                numbers = []
                for item in list(struct[type][title]["info"].keys()):
                    numbers.append(len(list(struct[type][title]["info"][item])))
                maxlen2 = max(numbers)+1
                print("The %s %s:" % (title, type))
                print("\033[94m=\033[97m"*(len("The %s %s:" % (title, type))-1))
                for item in list(struct[type][title]["info"].keys()):
                    print("\t\033[97m%s%s \033[94m= \033[97m[\033[94m%s\033[97m%s]"%(item," "*(maxlen - len(item) - 1),struct[type][title]["info"][item]," "*(maxlen2 - len(struct[type][title]["info"][item]))))
                print("\n")
            else:
                print("The %s %s:" % (title, type))
                print("\033[94m=\033[97m"*(len("The %s %s:" % (title, type))-1))
                for subitem in list(struct[type][title]["info"].keys()):
                    numbers = []
                    for number in list(struct[type][title]["info"][subitem].keys()):
                        numbers.append(len(number))
                    maxlen = max(numbers) + 1
                    numbers = []
                    for item in list(struct[type][title]["info"][subitem].keys()):
                        numbers.append(len(list(struct[type][title]["info"][subitem][item])))
                    maxlen2 = max(numbers) + 1
                    print("\tThe %s:" % subitem)
                    print("\t"+"\033[94m=\033[97m"*(len("The %s:" % subitem)-1))
                    for item in list(struct[type][title]["info"][subitem].keys()):
                        print("\t\t\033[97m%s%s \033[94m= \033[97m[\033[94m%s\033[97m%s]" % (
                            item, " " * (maxlen - len(item)), struct[type][title]["info"][subitem][item],
                            " " * (maxlen2 - len(struct[type][title]["info"][subitem][item]))))
                    print("")
                print("")