# Chicago Cabs

Welcome to the Chicago Cabs project! This web application provides fare predictions and travel times for cab rides in Chicago, as well as a dashboard for visualizing trip data.

## Hosted Link

You can access the application at: http://34.131.199.221

## Table of Contents

- Project Overview
- Features
- Installation
- Usage
- File Structure
- Dependencies
- Contributing
- License

## Project Overview

Chicago Cabs is a web application built using Flask, a Python web framework. The application allows users to:
- Enter pickup and dropoff locations to get fare and travel time estimates.
- View a dashboard with visualizations of trip data.

## Features

- Fare Prediction: Calculates fare based on the distance between pickup and dropoff locations.
- Travel Time Estimation: Provides an estimated travel time for the trip.
- Interactive Dashboard: Displays various visualizations of trip data using Tableau.

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
    
    git clone https://github.com/only-suyashsharthi/chicago-cabs.git
    cd chicago-cabs
    

2. Set up a virtual environment:
    
    python3 -m venv venv
    source venv/bin/activate
    

3. Install the required dependencies:
    
    pip install -r requirements.txt
    

4. Set up the Flask application:
    - Ensure you have the necessary models in the models/ directory.
    - Update the config.py file with any necessary configuration.

5. Run the application:
    
    flask run
    

6. Set up Apache (if hosting on Apache):
    - Configure your virtual host as per the Apache configuration section below.
    - Restart Apache:
        
        sudo systemctl restart apache2
        

## Usage

### Web Interface

- Homepage: Enter the pickup and dropoff locations, select the company and payment type, and click "Show Fare and Travel Time" to get predictions.
- Dashboard: Click on the dashboard button to view the interactive visualizations of the trip data.

### API Endpoints

- /predict: Endpoint for getting fare and travel time predictions.
  - Method: POST
  - Payload: JSON with keys pickup_lat, pickup_lon, dropoff_lat, dropoff_lon, company, and payment_type.

## Dependencies

- Flask
- Pandas
- Numpy
- CatBoost
- Haversine
- scikit-learn
- Jinja2
- Bootstrap

## Contributing

We welcome contributions! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.

## License

This project is licensed under the Apache2 License.
