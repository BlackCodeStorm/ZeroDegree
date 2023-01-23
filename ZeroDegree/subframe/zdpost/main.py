from modules import output
from modules import public
def start(MainFrame,logs):
    main = ZdPost()
    while True:
        info = public.format(input("\033[97m[\033[94mzdpost\033[97m\033[94m \033[97mmodule(\033[94m" + "no module" + "\033[97m)]\033[94m#\033[97m"))
        if info == [""]:
            pass
        elif info == ["return"]:
            return
        elif info == ["exit"]:
            exit()

class ZdPost():
    pass