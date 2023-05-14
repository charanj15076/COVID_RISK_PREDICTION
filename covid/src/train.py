import joblib

class Classifier:
    def __init__(self):
        pass

    def load_and_test(self, data):


        model = joblib.load(open("models/modelgb.pkl", "rb"))

        prediction = model.predict(data)

        return prediction
