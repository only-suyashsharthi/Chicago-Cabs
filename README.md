# Chicago Cabs

Welcome to **Chicago Cabs**! 🚕  
A Flask web app that predicts **cab fare** and **travel time** in Chicago and includes an **interactive Tableau dashboard**.

## Demo

https://github.com/user-attachments/assets/515c1d4b-25fa-42c2-b3cb-b30be59170cc

---

## Table of Contents
- Project Overview
- Features
- Installation
- File Structure
- Functions Explained
- API
- Dependencies
- Contributing

---

## Project Overview

Chicago Cabs lets users:
- Enter pickup and dropoff locations to get fare and travel time estimates.
- See a **Tableau** dashboard of trip insights.

---

## Features

- **Auto-select Cheapest Option (NEW):**  
  After the user enters **pickup** and **dropoff**, the app computes fares across **all companies** and **3 payment modes**.  
  It **auto-selects and displays the minimum fare** and corresponding **company** and **payment mode**. The user can then change the dropdowns to compare other combinations.

- **Fare Prediction:** Based on trip distance + model features.
- **Travel Time Estimation:** Distance-based time estimate.
- **Interactive Dashboard:** Embedded Tableau analytics.

---

## Installation

```bash
git clone https://github.com/yourusername/chicago-cabs.git
cd chicago-cabs

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
````

Prepare models:

* Place `puca.pkl`, `doca.pkl`, `fare_model.pkl` into `models/`.

Run the app:

```bash
flask run
```

---

## File Structure

```text
Chicago-Cabs/
├── main.py                 
├── requirements.txt       # Dependencies
├── templates/
│   ├── index.html         # Homepage
│   └── dashboard.html     # Tableau embed page
├── static/
│   ├── css/
│   │   └── styles.css     # Styles (includes background image, etc.)
│   └── js/
│       └── script.js      # Map + autocomplete + prediction logic
├── models/
│   ├── puca.pkl           # Pickup community area model
│   ├── doca.pkl           # Dropoff community area model
│   └── fare_model.pkl     # Fare regression model
└── config.py              # Config (e.g., keys, settings)
```

---

## Functions Explained (What was added today)

1. **Auto-Select Cheapest Fare**

   * When both **pickup** and **dropoff** are set, the frontend calls `/predict` **without** specifying `company`/`payment_type`.
   * The backend evaluates **all companies** × **(Credit Card, Mobile, Cash)** and returns the **minimum fare** with `best_company` and `best_payment`.
   * The UI **sets the dropdowns** to those best values and **renders fare/time** automatically.
   * Users can still **change** company/payment and **recalculate**.

2. **Dashboard Centering**

   * Minor HTML style change to **center the Tableau dashboard horizontally**, preserving the original layout and sizing logic.

---

## API

### `POST /predict`

* **Purpose**

  * If `company` and `payment_type` are **omitted** → returns **cheapest** fare across all combinations, plus which company/payment achieved it.
  * If `company` and `payment_type` are **provided** → returns fare/time for that specific combo.

* **Request (cheapest mode)**

  ```json
  {
    "pickup_lat": 41.8781,
    "pickup_lon": -87.6298,
    "dropoff_lat": 41.8818,
    "dropoff_lon": -87.6231
  }
  ```

* **Response (cheapest mode)**

  ```json
  {
    "fare": 12.34,
    "travel_time": 18.75,
    "best_company": "Flash Cab",
    "best_payment": "Credit Card"
  }
  ```

* **Request (specific combo)**

  ```json
  {
    "pickup_lat": 41.8781,
    "pickup_lon": -87.6298,
    "dropoff_lat": 41.8818,
    "dropoff_lon": -87.6231,
    "company": "Sun Taxi",
    "payment_type": "Cash"
  }
  ```

* **Response (specific combo)**

  ```json
  {
    "fare": 13.21,
    "travel_time": 18.75
  }
  ```

* **Notes**

  * **Payment modes** considered for cheapest: `Credit Card`, `Mobile`, `Cash`.
  * **Companies**: uses the full list as in the dropdown (Flash Cab, Taxicab Insurance Agency Llc, City Service, Chicago Independents, Taxi Affiliation Services, Sun Taxi, 5 Star Taxi, Globe Taxi, Blue Ribbon Taxi Association, Medallion Leasin).

---

## Dependencies

* Flask
* Pandas
* NumPy
* CatBoost
* Haversine
* scikit-learn
* Jinja2
* Bootstrap

---

## Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature-branch`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature-branch`
5. Open a PR
