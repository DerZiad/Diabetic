import os
from FileDeepLerner import GoDeepInFile
class CommandLiner:
    def __init__(self,models,writer):
        self.models = models
        self.writer = writer
    def run(self):
        os.system("cls")
        chaine = ""
        while chaine != "N":
            Pregnancies = float(input("Entrer Pregnancies:"))
            Glucose = float(input("Entrer Glucose:"))
            BloodPressure = float(input("Entrer BloodPressure:"))
            SkinThickness = float(input("Entrer SkinThickness:"))
            Insulin = float(input("Entrer Insulin:"))
            BMI = float(input("Entrer BMI:"))
            DiabetesPedigreeFunction = float(input("Entrer DiabetesPedigreeFunction:"))
            Age = float(input("Entrer Age:"))
            x = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]

            predictionMachileLearning = self.models.predictMachineLearning(x)
            predictionDeepLearning = self.models.predictDeepLearning(x)

            if predictionMachileLearning == 0:
                self.writer.writeError("Prediction logistic Non diabetique")
            else:
                self.writer.writeSuccess("Prediction logistic diabetique")

            if predictionDeepLearning == 0:
                self.writer.writeError("Prediction tensorflow Non diabetique")
            else:
                self.writer.writeSuccess("Prediction tensorflow diabetique")
            chaine = str(input("Voulez vous ressayer encore [O\\N]:"))
        def run(self,filName):
            os.system("cls")
            deep = GoDeepInFile(filName)