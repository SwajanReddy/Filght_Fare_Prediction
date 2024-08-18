# Flight Fare Prediction

This project is a web application that predicts flight fares based on user inputs such as departure time, arrival time, source, destination, airline, and the number of stops. The prediction is made using a trained machine learning model.

## Overview

This Flask-based web application allows users to input flight details and receive a predicted fare. The prediction is made using a machine learning model that has been trained on historical flight data. 

## Features

- Predict flight fares based on user inputs
- User-friendly web interface built with Flask
- Integration with a pre-trained machine learning model

## Installation

### Prerequisites

- Python 3.10
- Flask
- Flask-CORS
- scikit-learn
- Pandas
- Numpy

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/swajanreddy/flight-fare-prediction.git
   cd flight-fare-prediction
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Place the trained model:**

   Ensure that you have the `flight_rf.pkl` file (the trained model) in the root directory of the project.

## Usage

1. **Run the Flask application:**

   ```bash
   python app.py
   ```

2. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. **Use the app:**

   Fill in the form with the required flight details and click "Predict" to see the estimated flight fare.

## Project Structure

```plaintext
├── app.py                  # Main application file
├── flight_rf.pkl           # Trained machine learning model
├── templates/
│   └── home.html           # HTML template for the home page
├── static/                 # Static files like CSS, JS, images (if any)
├── README.md               # Project documentation
├── requirements.txt        # Python packages required
└── venv/                   # Virtual environment (not included in the repo)
```

## Technologies Used

- **Flask**: For creating the web application.
- **Flask-CORS**: To handle cross-origin requests.
- **scikit-learn**: For loading and using the pre-trained machine learning model.
- **Pandas & Numpy**: For data manipulation and preprocessing.

## Model Information

The machine learning model used in this project is a Random Forest Regressor trained on historical flight data. The model considers features like the number of stops, departure and arrival times, source, destination, and the airline to predict the flight fare.

## Credits
Project replicated from https://www.youtube.com/watch?v=y4EMEpEnElQ


