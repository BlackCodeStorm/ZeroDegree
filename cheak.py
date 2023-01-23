def initFramework():
    import os
    import sys
    from modules import output
    if os.geteuid() != 0:
        output.error("You must run Alpha ZeroDegree Framework in root power!")
        output.error("But we found you are not in root power!")
        output.error("QUITTIING!")
        sys.exit()
    else:
        os.system("clear")
        import start