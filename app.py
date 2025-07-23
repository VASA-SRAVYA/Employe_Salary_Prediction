from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('salary_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_form')
def predict_form():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    years = float(request.form['experience'])
    age = int(request.form['age'])
    gender = request.form['gender']
    education = request.form['education']
    job = request.form['job']

    input_df = pd.DataFrame({
        'YearsExperience': [years],
        'Age': [age],
        f'Gender_{gender}': [1],
        f'Education_{education}': [1],
        f'JobTitle_{job}': [1]
    })

    model_features = model.feature_names_in_
    for col in model_features:
        if col not in input_df:
            input_df[col] = 0

    input_df = input_df[model_features]
    salary = model.predict(input_df)[0]

    return render_template('predict.html', salary=round(salary, 2))

if __name__ == "__main__":
    app.run(debug=True)
