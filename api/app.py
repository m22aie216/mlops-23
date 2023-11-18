from flask import Flask, request, jsonify
from joblib import load
import os
import numpy as np
import re
app = Flask(__name__)

@app.route('/hello/<name>')
def index(name):
    return "Hello, "+name+"!"

@app.route('/predict', methods=['POST'])
def pred_model():
    js = request.get_json()
    tt = js['image']
    jj = re.split('\,', tt)
    numbers = np.array(jj,dtype='i') 
    print("------------")
    print(type(numbers))
    print(numbers)
    num = numbers.reshape(1,-1)
    print(num)
    #Assuming this is the path of our best trained model
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../models/svm_gamma:0.001_C:0.1.joblib')
    model = load(filename)
    pred1 = model.predict(num)
    #reurn pred1 in json
    return jsonify(prediction=pred1.tolist())
    
if __name__ == '__main__':
    app.run(debug=True)
