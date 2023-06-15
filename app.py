from flask import Flask, render_template, request
import pickle
import xgboost
import numpy as np

model = pickle.load(open('XGBoost.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    day_of_month = int(request.form.get('day_of_month'))
    day_of_week = int(request.form.get('day_of_week'))
    month = int(request.form.get('month'))
    precipitation = float(request.form.get('precipitation'))
    wind_speed = float(request.form.get('wind_speed'))
    humidity = int(request.form.get('humidity'))
    hour = int(request.form.get('hour'))
    temperature = float(request.form.get('temperature'))

    input_array = np.array([hour, temperature, humidity, wind_speed, month, day_of_month, day_of_week, precipitation]).reshape(1,8)
    result = int(model.predict(input_array))
    res = f'Predicted Bike Demand: {result}'
    return render_template('index.html', result=res)

if __name__ == '__main__':
    app.run(debug=True)