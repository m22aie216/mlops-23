from flask import Flask, request, jsonify
from joblib import load
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

@app.route("/", methods=["POST"])
def hello_world_post():    
    return {"op" : "Hello, World POST " + request.json["suffix"]}

@app.route('/predict', methods=['POST'])
def pred_model():
    js = request.get_json()
    image1 = [js['image']]
    model = js['model']
    #Assuming this is the path of our best trained model
    dirname = os.path.dirname(__file__)
    if model == 'tree':	
    	filename = os.path.join(dirname, '../models/treemax_depth:100.joblib')
    elif model == 'svm':
    	filename = os.path.join(dirname, '../models/svmgamma:0.001_C:2.joblib')

    elif modle == 'lr':
    	filename = os.path.join(dirname, '../models/m22aie216_lr_lbfgs.joblib')
    else:
    	filename = os.path.join(dirname, '../models/m22aie216_lr_liblinear.joblib')

    model = load(filename)
    pred1 = model.predict(image1)
    #reurn pred1 in json
    return jsonify(prediction=pred1.tolist())
    
if __name__ == '__main__':
    app.run(debug=True)
