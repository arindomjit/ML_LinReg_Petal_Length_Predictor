from flask import Flask, request, render_template
import json
from flask_cors import CORS, cross_origin
import traceback
import score

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/predict_petal_length": {"origins": "*"}})

@app.route('/predict_petal_length', methods=["POST"])
@cross_origin(origin='*',headers=['Content- Type'])
def predict_petal_length():
    try:
        if request.method == 'POST':
            #petal_width = request.args.get('petal_width')
            petal_width = request.form['petal_width']
            lst = score.predict_length(petal_width)
            resp = json.dumps(lst[0])
        #return resp
        return render_template('result.html', prediction=resp)
    except Exception:
        return traceback.format_exc()

@app.route('/')
def main():
    return render_template('home.html')
    #return 'Welcome!'
    
    
if __name__ == '__main__':
    app.run()