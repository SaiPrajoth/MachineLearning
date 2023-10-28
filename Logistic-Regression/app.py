from flask import Flask, render_template, request
import sklearn 
import pickle

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__,template_folder='templates')


@app.route('/')
def hello_name():
    return render_template('frontend.html')

@app.route('/predict',methods=['POST'])
def predict():
        sepal_length = request.form.get('sepal-length') 
        sepal_width = request.form.get('sepal-width')
        petal_length = request.form.get('petal-length')
        petal_width = request.form.get('petal-width')
        output = model.predict([[float(sepal_length),float(sepal_width),float(petal_length),float(petal_width)]])

        return render_template('frontend.html',prediction=f"The model prediction for the data given is {output[0]}.")



if __name__ == '__main__':
    app.run()
