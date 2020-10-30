#!/usr/bin/env python3
import pickle
from flask import Flask, request
import numpy as np
import pandas as pd
from flasgger import Swagger


with open("./data/rcf_model.pkl", "rb") as f:
    rfc = pickle.load(f)


app = Flask(__name__)
swagger = Swagger(app)
@app.route('/predict')
def predict():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    """
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")

    instance = np.array([[s_length, s_width, p_length, p_width]])
    prediction = rfc.predict(instance)
    print("Predicted Class: {}".format(str(prediction) ))
    return str(prediction)


@app.route('/predict_from_file', methods = ["POST"])
def predict_from_file():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    input_data = pd.read_csv(request.files.get("input_file"), header = None)
    print(input_data)
    predictions = rfc.predict(input_data)

    print(predictions)

    return str(list(predictions))


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000) 

