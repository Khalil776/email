from flask import Flask,render_template, request,jsonify

import pickle

app =Flask(__name__)


@app.route('/analyse',methods=['POST', 'GET'])
def analyse():
    
    text=request.get_json()
    print(text)
    with open('model','rb') as file:
        model = pickle.load(file)
    
    predictions = model.predict([text["rawtext"]])
    print(predictions[0])
    result = {"message":"Negative"}
    if predictions[0] == 'neg':
        result = {"message":"Negative"}
    else:
        result = {"message":"Positive"}    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)