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