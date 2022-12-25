import modules.output
class Frame:
    def _processesing_event(self):
        pass

    def open_the_option(self,option):
        if option.lower() in self.enable:
            for i in list(self.project.keys()):
                for l in list(self.project[i].keys()):
                    if l == option.lower():
                        self.project[i][l][1] = "true"
                        self._processesing_event()
            modules.output.info("Open the %s"%option.upper())
        else:
            modules.output.error("This item was not found,or this item can not open!")

    def close_the_option(self,option):
        if option.lower() in self.enable:
            for i in list(self.project.keys()):
                for l in list(self.project[i].keys()):
                    if l == option.lower():
                        self.project[i][l][1] = "false"
                        self._processesing_event()
            modules.output.info("Close the %s"%option.upper())
        else:
            modules.output.error("The item was not found,or this item can not close!")

    def set_the_option(self,option,data):
        temp = 0
        for i in list(self.project.keys()):
            for l in list(self.project[i].keys()):
                if l == option.lower():
                    self.project[i][l][0] = data
                    self._processesing_event()
                    temp = 1
        if temp == 0:
            modules.output.error("The item was not found!")
            return
        else:
            print("")
            modules.output.info(option.upper() + " ---> " + data)
            print("")

    def run_the_attack(self):
        pass