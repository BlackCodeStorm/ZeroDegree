from modules import output
from lib import frame
class Entrance(frame.Frame):
    def __init__(self,logs):
        self.describe = "A module for denial-of-service attacks."
        self.writer   = "Alpha"
        self.os       = ["windows","linux","macos","ios","android"]
        self.Logs     = logs
        self.project = {
            "Basic":{
                "rhost":{
                    "value":"127.0.0.1",
                    "state":"open",
                    "describe":"",
                },
                "rport":{
                    "value":"80",
                    "state":"open",
                    "describe":""
                },
            },
        }

    def processesingTheEvent(self):
        pass

    def runTheAttack(self):
        pass