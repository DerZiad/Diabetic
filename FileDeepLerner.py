import os
try:
    import pandas as pd
    import numpy as np
except:
    os.system("pip install pandas")
    os.system("pip install openpyxl")
    import pandas as pd
    import numpy as np

import pandas as pd
class GoDeepInFile:

    def __init__(self,fileName):
        self.fileName = fileName
        self.dataframe = pd.read_excel(self.fileName)
        self.x = self.dataframe.drop("Outcome", axis=1).dropna(axis=0)

    def predictData(self,predictFunction):
        y = []
        for i in range(self.x.shape[0]):
            prediction = predictFunction(np.array(self.x.iloc[i,:]).reshape(1,self.x.iloc[i, :].shape[0]))
            if prediction == 0:
                y.append("Non diabetique")
            else:
                y.append("Diabetique")
        data ={
            'Pregnancies':self.x['Pregnancies'],
            'Glucose': self.x['Glucose'],
            'Blood Presure': self.x['Blood Presure'],
            'Skin Thickness': self.x['Skin Thickness'],
            'Insulin': self.x['Insulin'],
            'BMI': self.x['BMI'],
            'Diabetes Predigree Function': self.x['Diabetes Predigree Function'],
            'Age': self.x['Age'],
            'Outcome':y
        }
        dataframe = pd.DataFrame(data)
        dataframe.to_excel("output.xlsx", sheet_name='Sheet1')