import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd
import datetime
import os
from catboost import CatBoostRegressor
from haversine import haversine

app = Flask(__name__)

# Load models
puca_model = pickle.load(open('models/puca.pkl', 'rb'))
doca_model = pickle.load(open('models/doca.pkl', 'rb'))
fare_model = pickle.load(open('models/fare_model.pkl', 'rb'))

company_mapping = {'Flash Cab': 1, 'Taxicab Insurance Agency Llc': 2, 'City Service': 3, 'Chicago Independents': 4, 'Taxi Affiliation Services': 5, 'Sun Taxi': 6, '5 Star Taxi': 7, 'Globe Taxi': 8, 'Blue Ribbon Taxi Association': 9, 'Medallion Leasin': 10}
payment_type_mapping = {'Credit Card': 1, 'Mobile': 2, 'Cash': 3, 'Prcard': 4, 'Coupon': 5}

#API
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', 'AIzaSyBOZyTU9HXrof3UvDFDzFsADJyP0YpY8Sc')

@app.route('/')
def home():
    return render_template('index.html', api_key=GOOGLE_MAPS_API_KEY)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    pickup_lat = data['pickup_lat']
    pickup_lon = data['pickup_lon']
    dropoff_lat = data['dropoff_lat']
    dropoff_lon = data['dropoff_lon']
    company = data.get('company')
    payment_type = data.get('payment_type')

    trip_miles = haversine((pickup_lat, pickup_lon), (dropoff_lat, dropoff_lon))
    pickup_community_area = puca_model.predict([[pickup_lat, pickup_lon]])[0]
    dropoff_community_area = doca_model.predict([[dropoff_lat, dropoff_lon]])[0]
    trip_minutes = trip_miles / 0.512
    trip_start_hour = datetime.datetime.now().hour
    trip_start_day = datetime.datetime.now().weekday()

    def predict_fare(c, p):
        input_features = [[
            trip_miles, pickup_community_area, dropoff_community_area,
            trip_minutes, trip_start_hour, trip_start_day,
            company_mapping[c], 0, 0, 0, payment_type_mapping[p]
        ]]
        fare = fare_model.predict(input_features)[0]
        return fare

    # If company/payment are not sent → calculate best combo
    if not company or not payment_type:
        best_fare = float("inf")
        best_combo = None
        for c in company_mapping.keys():
            for p in ["Credit Card", "Mobile", "Cash"]:
                fare = predict_fare(c, p)
                if fare < best_fare:
                    best_fare = fare
                    best_combo = (c, p)

        return jsonify({
            'fare': round(best_fare, 2),
            'travel_time': round(trip_minutes, 2),
            'best_company': best_combo[0],
            'best_payment': best_combo[1]
        })

    # Otherwise → calculate for given choice
    fare = predict_fare(company, payment_type)
    return jsonify({
        'fare': round(fare, 2),
        'travel_time': round(trip_minutes, 2)
    })


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
