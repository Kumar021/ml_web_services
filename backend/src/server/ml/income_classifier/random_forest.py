import joblib
import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder #

class MultiColumnLabelEncoder:
    """retun obejct"""
    def __init__(self,columns = None):
        self.columns = columns # array of column names to encode

    def fit(self,X,y=None):
        return self # not relevant here

    def transform(self,X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                output[col] = LabelEncoder().fit_transform(output[col])
        else:
            for colname,col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)
        return output

    def fit_transform(self,X,y=None):
        return self.fit(X,y).transform(X)


class RandomForestClassifier:
    def __init__(self):
        path_to_artifacts = "E:/JavaProgra/ML_and_DC/Project - Machine Learning/research/"
        #self.values_fill_missing =  joblib.load(path_to_artifacts + "train_mode.joblib")
        #self.encoders = joblib.load(path_to_artifacts + "encoders.joblib")
        self.model = joblib.load(path_to_artifacts + "random_forest.joblib")

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        new_dataset = pd.DataFrame(input_data, index=[0])
        # fill missing values
        #input_data.fillna(self.values_fill_missing)
        new_dataset = new_dataset.fillna(method='ffill', axis=0)
        # convert categoricals
        cate_columns = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex','native-country']
        new_input = MultiColumnLabelEncoder(columns = cate_columns).fit_transform(new_dataset.iloc[:, :])

        new_input_values = new_input.values
        print("new_input_values :", new_input)

        return new_input

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






