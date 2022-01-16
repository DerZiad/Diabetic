import os
try:
    from tensorflow.keras import Sequential
    from tensorflow.keras.layers import Dense, Dropout
    from tensorflow.keras.optimizers import RMSprop, Adam
    from keras.wrappers.scikit_learn import KerasClassifier
    from keras.callbacks import EarlyStopping
    from tensorflow.keras.models import model_from_json
    import tensorflow.keras as keras
    import numpy as np
except:
    os.system("pip install tensorflow")
    from tensorflow.keras import Sequential
    from tensorflow.keras.layers import Dense, Dropout
    from tensorflow.keras.optimizers import RMSprop, Adam
    from keras.wrappers.scikit_learn import KerasClassifier
    from keras.callbacks import EarlyStopping
    from tensorflow.keras.models import model_from_json
    import numpy as np
try:
    import sklearn
    from sklearn.preprocessing import StandardScaler
except:
    os.system("pip install sklearn")
    import sklearn
try:
    import pickle
except:
    os.system("pip install pickle")
    import pickle


class DeepLerner:
    def __init__(self,wr):
        self.wr = wr
        machineLearning,deepLearning,scaler = self.loadModel()
        self.machineLearning = machineLearning
        self.deepLearning = deepLearning
        self.scaler = scaler
    def loadModel(self):
        self.wr.writeSuccess("[ + ] - Reading models")
        try:
            machineLearning = pickle.load(open("models/machileLearning.sav", 'rb'))
            scaler = pickle.load(open("models/myscaler", 'rb'))
            json_file = open('models/deeplearning.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            loaded_model = model_from_json(loaded_model_json)
            return machineLearning, loaded_model,scaler
        except:
            self.wr.writeError("Cannot read models")
            exit(2)
    def predictDeepLearning(self,x):
        x = self.scaler.transform(x)
        predictionOfDeepLearning = self.deepLearning.predict(x)
        return np.argmax(predictionOfDeepLearning)
    def predictMachineLearning(self,x):
        x = self.scaler.transform(x)
        pred = self.machineLearning.predict(x)
        return pred[0]

