import time
class logs():
    def __init__(self):
        self._level = {
            0:"ERROR",
            1:"WORRY",
            2:"NOTE",
            3:"INFO",
            4:"DEBUG",
            5:"|"
        }
        self._log_save_file = "\\"
        self._log_file = ""

    def __del__(self):
        self._log_file.close()
    def setLogSaveFile(self, file_path):
        self._log_file = open(file_path,"a+")
        self._log_save_file = file_path

    def writeLog(self, level, info):
        self._log_file.write("".join(("[", "/".join((str(time.localtime()[0]),
                                                     str(time.localtime()[1]),
                                                     str(time.localtime()[2]),)),
                                                     " ",
                                           ":".join((str(time.localtime()[3]),
                                                     str(time.localtime()[4]),
                                                     str(time.localtime()[6]))), "][",
                                      self._level[level], "]", info,"\n")))
