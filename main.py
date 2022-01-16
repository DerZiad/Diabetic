import os, sys
from Writer import Writer
wr = Writer()#Console writer
wr.writeStep("[ + ] - Scanning system file")

from CommandLiner import CommandLiner
from AIModels import DeepLerner as Lerner
import GraphiqueInterface as interface
models = Lerner(wr)


if __name__ == '__main__':
    args = sys.argv
    commandOk = False
    commandImport = False
    graphiqueOK = False
    for argument in args:
        if argument == "-c":
            commandOk = True
        elif argument == "-g":
            graphiqueOK = True
            commandOk = False
        elif argument == "--import":
            commandImport = True
        elif commandImport and argument == "-d":
            commandOk = True
        elif commandImport and argument == "-m":
            commandOk = True
    if commandOk:
        if commandImport:
            pass
        else:
            commandRunner = CommandLiner(models,wr)
            commandRunner.run()
    elif graphiqueOK:
        interface.launch(models)
    else:
        os.system("cls")
        wr.writeError("python " + args[0] + "-c ou -g")
        wr.writeError("[Options] = -c for command liner and -g for graphique launch")
        wr.writeError("python " + args[0] + " --import [file.xlsx] -d ou -m")
        wr.writeError("[Options] = -d for deep learning and -m for machine learning")
        exit(2)
