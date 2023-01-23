import modules.output
class Frame:
    project = {}
    def processesingTheEvent(self):
        pass

    def openTheOption(self, option):
        if option in self.enable:
            for i in list(self.project.keys()):
                for l in list(self.project[i].keys()):
                    if l == option:
                        self.project[i][l]["state"] = "true"
                        self.processesingTheEvent()
            modules.output.info("Open the %s"%option )
        else:
            modules.output.error("This item was not found,or this item can not open!")

    def closeTheOption(self,option):
        if option in self.enable:
            for i in list(self.project.keys()):
                for l in list(self.project[i].keys()):
                    if l == option:
                        self.project[i][l]["state"] = "false"
                        self.processesingTheEvent()
            modules.output.info("Close the %s"%option )
        else:
            modules.output.error("The item was not found,or this item can not close!")

    def setTheOption(self,option,data):
        temp = 0
        for i in list(self.project.keys()):
            for l in list(self.project[i].keys()):
                if l == option:
                    self.project[i][l]["value"] = data
                    self.processesingTheEvent()
                    temp = 1
        if temp == 0:
            modules.output.error("The item was not found!")
            return
        else:
            print("")
            modules.output.info(option  + " ---> " + data)
            print("")

    def runTheAttack(self):
        pass