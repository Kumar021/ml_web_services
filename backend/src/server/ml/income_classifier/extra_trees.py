import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder #
from server.ml.income_classifier.random_forest import MultiColumnLabelEncoder

class ExtraTreesClassifier:
    def __init__(self):
        path_to_artifacts = "E:/JavaProgra/ML_and_DC/Project - Machine Learning/research/"

        self.model = joblib.load(path_to_artifacts + "extra_trees.joblib")

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        # JSON to pandas DataFrame
        new_dataset = pd.DataFrame(input_data, index=[0])
        # fill missing values
        #input_data.fillna(self.values_fill_missing)
        new_dataset = new_dataset.fillna(method='ffill', axis=0)
        # convert categoricals
        cate_columns = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex','native-country']
        new_input = MultiColumnLabelEncoder(columns = cate_columns).fit_transform(new_dataset.iloc[:, :])

        new_input_values = new_input.values

        return new_input_values

    def predict(self, input_data):
        return self.model.predict_proba(input_data)

    def postprocessing(self, input_data):
        label = "<=50K"
        if input_data[1] > 0.5:
            label = ">50K"
        return {"probability": input_data[1], "label": label, "status": "OK"}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0]  # only one sample
            prediction = self.postprocessing(prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction















