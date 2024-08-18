from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))

x = ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour', 'Dep_min',
       'Arrival_hour', 'Arrival_min', 'Duration_hours', 'Duration_mins',
       'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
       'Airline_Jet Airways', 'Airline_Jet Airways Business',
       'Airline_Multiple carriers',
       'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
       'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
       'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
       'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
       'Destination_Kolkata', 'Destination_New Delhi']

X = pd.DataFrame(columns=x)

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        source = request.form["Source"]
        destination = request.form["Destination"]
        airline = request.form["airline"]
        sou_column = 'Source_' + source
        des_column = 'Destination_' + destination
        air_column = 'Airline_' + airline


        if sou_column in X.columns:
            sou_index = np.where(X.columns == sou_column)[0][0]
        else:
            sou_index = -1
            
        if des_column in X.columns:
            des_index = np.where(X.columns == des_column)[0][0]
        else:
            des_index = -1

        if air_column in X.columns:
            air_index = np.where(X.columns == air_column)[0][0]
        else:
            air_index = -1

        x = np.zeros(len(X.columns))

        dept_date = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(dept_date, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(dept_date, format ="%Y-%m-%dT%H:%M").month)
        #print("Journey:",Journey_day,Journey_month)
        # Departure
        Dep_hour = int(pd.to_datetime(dept_date, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(dept_date, format ="%Y-%m-%dT%H:%M").minute)
        #print("dep time:",Dep_hour,Dep_min)
        arr_date = request.form["Arrival_Time"]
        # Arrival
        Arrival_hour = int(pd.to_datetime(arr_date, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(arr_date, format ="%Y-%m-%dT%H:%M").minute)
        #print("arrival:",Arrival_hour, Arrival_min)
        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        stops = int(request.form["stops"])
        x[0] = stops
        x[1] = Journey_day
        x[2] = Journey_month
        x[3] = Dep_hour
        x[4] = Dep_min
        x[5] = Arrival_hour
        x[6] = Arrival_min
        x[7] = dur_hour
        x[8] = dur_min

        if sou_index>=0:
            x[sou_index] = 1
        if des_index>=0:
            x[des_index] = 1
        if air_index>=0:
            x[air_index] = 1
        print(x)
        prediction = model.predict([x])[0]
        print("-----------prediction----------:",prediction)
        output=round(prediction,2)

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)