import os
try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama
class Writer:
    def __init__(self):
        colorama.init()

    def writeSuccess(self, msg):
        print(("{}" + msg + "{}").format(colorama.Fore.LIGHTGREEN_EX,colorama.Style.RESET_ALL))

    def writeError(self, msg):
        print(("{}" + msg + "{}").format(colorama.Fore.RED,colorama.Style.RESET_ALL))

    def writeWarning(self, msg):
        print(("{}" + msg + "{}").format(colorama.Fore.LIGHTYELLOW_EX,colorama.Style.RESET_ALL))

    def writeRequest(self, msg):
        print(("{}" + msg + "{}").format(colorama.Fore.BLUE,colorama.Style.RESET_ALL))

    def writeProposition(self, msg):
        print(("{}" + msg + "{}").format(colorama.Fore.LIGHTBLUE_EX,colorama.Style.RESET_ALL))

    def writeStep(self, msg):
        print(("{}" + msg + "{}").format(colorama.Fore.LIGHTCYAN_EX,colorama.Style.RESET_ALL))