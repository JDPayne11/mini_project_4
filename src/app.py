# import Flask and jsonify
from flask import Flask, jsonify, request

# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import pickle
from sklearn.base import BaseEstimator, TransformerMixin

app = Flask(__name__)
api = Api(app)


class LogTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, column_names):

        self.column_names = column_names

    def fit(self, X, y=None):

        return self

    def transform(self, X, y=None):

        X = X.copy()  # Don't modify the original variable that was passed in
        X[self.column_names] = np.log(X[self.column_names])

        return X


model = pickle.load(
    open(
        r"C:\Users\JDPayne\Desktop\Mini_Project_4\mini_project_4\notebooks\Loan_prediction.p",
        "rb",
    )
)


class Approval(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        # getting predictions from our model.
        # it is much simpler because we used pipelines during development
        res = model.predict(df)
        # we cannot send numpt array as a result
        return res.tolist()


api.add_resource(Approval, "/Approval")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
