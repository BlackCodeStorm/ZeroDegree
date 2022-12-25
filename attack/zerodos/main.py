from lib import frame
from modules import output
class Entrance(frame.Frame):
    def __init__(self,):
        self.project = {
            "basic":{
                "rhost":["127.0.0.1","open","The Terget"]
            }
        }

    def run_the_attack(self):
        output.find("The Attack Is Running!")
        output.find("And We Fing A Target!")