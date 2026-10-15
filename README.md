# 🚕 Uber Fare Prediction

A machine learning regression project that predicts Uber fare amounts before a trip, using trip distance, coordinates, and time-based features.

---

## Overview

- **Goal:** Estimate `fare_amount` from historical ride data
- **Models:** Linear Regression vs. Random Forest
- **Dataset:** `uber_trips_dataset_50k.csv` (~10k cleaned trips)
- **Best Model:** Linear Regression — RMSE 3.07, R² 0.74

---

## Dataset

| Column | Description |
|---|---|
| `pickup_lat`, `pickup_lng` | Pickup coordinates |
| `drop_lat`, `drop_lng` | Drop-off coordinates |
| `distance_km` | Provided trip distance |
| `fare_amount` | Target variable |
| `pickup_time`, `drop_time` | Trip timestamps |
| `status` | Trip status (Completed / Cancelled / No-Show) |

**Note:** `passenger_count` is not present in this dataset, though the original brief listed it as a feature.

---

## Workflow

1. **Data Understanding** — shape, dtypes, missing values, duplicates
2. **Data Cleaning** — removed cancelled/no-show trips, invalid coordinates, non-positive fares, and fare outliers
3. **Feature Engineering** — extracted hour, day of week, month, year; computed Haversine `trip_distance`
4. **EDA** — distributions, correlations, fare vs distance, fare by time
5. **Modeling** — 80/20 split; Linear Regression and Random Forest
6. **Evaluation** — MAE, MSE, RMSE, R²

---

## Results

| Model | MAE | MSE | RMSE | R² |
|---|---|---|---|---|
| Linear Regression | 2.4654 | 9.4143 | **3.0683** | **0.7428** |
| Random Forest | 2.5127 | 9.9500 | 3.1544 | 0.7281 |

Linear Regression performed slightly better. `distance_km` was the dominant feature (~79% importance). Average prediction error is ~$2.47.

---

## Business Takeaways

- **Distance is everything.** `distance_km` drives ~79% of the model's decisions.
- **Simple beat complex.** Linear Regression outperformed Random Forest on this dataset.
- **Time barely matters.** Average fare varies by only ~$0.50 across all hours of the day.
- **Passenger count unknown.** Not present in this dataset, so its impact can't be assessed.

Full answers to the seven business questions are in the [notebook](notebooks/Uber_Fare_Prediction.ipynb).

---

## Project Structure

```
Uber_Fare_Prediction/
├── app/
│   └── app.py                    # Streamlit fare predictor
├── charts/                       # 9 EDA and evaluation charts
├── dataset/
│   └── uber_trips_dataset_50k.csv
├── models/
│   └── uber_fare_model.pkl       # Trained model
├── notebooks/
│   └── Uber_Fare_Prediction.ipynb
├── outputs/
│   ├── business_answers.json
│   └── model_comparison.csv
├── requirements.txt
└── README.md
```

---

## How to Run

### Google Colab

1. Open [Colab](https://colab.research.google.com) → **Upload notebook** → select `notebooks/Uber_Fare_Prediction.ipynb`
2. Upload `dataset/uber_trips_dataset_50k.csv` to `/content/`
3. **Runtime → Run all**

### Locally

```bash
git clone https://github.com/darshanmljain/Uber_Fare_Prediction.git
cd Uber_Fare_Prediction
pip install -r requirements.txt
streamlit run app/app.py
```

Open `http://localhost:8501` in your browser.

### Deploy the App (Free)

1. Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub
2. Create app → repo `darshanmljain/Uber_Fare_Prediction` → branch `main` → main file `app/app.py`
3. Deploy

---

## Tech Stack

Python · Pandas · NumPy · Matplotlib · Seaborn · Scikit-learn · Joblib · Streamlit

---

## Author

**Darshan Jain** — [GitHub](https://github.com/darshanmljain)
