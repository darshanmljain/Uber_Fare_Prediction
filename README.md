# Uber Fare Prediction

A machine-learning regression project that predicts Uber fare amounts before a trip, using trip distance, coordinates, and time-of-day features.

**Author:** Your Name
**GitHub:** https://github.com/YOUR_USERNAME
**Live Demo:** YOUR_WEBSITE_URL

---

## Problem

Riders and the platform only know the final fare after a trip ends. This project builds a regression model that estimates `fare_amount` upfront from historical ride data.

## Dataset

- File: `dataset/uber_trips_dataset_50k.csv`
- ~10,000 cleaned trips after filtering
- Columns: `trip_id`, `driver_id`, `rider_id`, `city`, `pickup_lat`, `pickup_lng`, `drop_lat`, `drop_lng`, `distance_km`, `fare_amount`, `status`, `payment_method`, `pickup_time`, `drop_time`

**Note:** The original brief referenced the Kaggle Uber Fares Dataset (~200k rows, with `passenger_count`). This project uses a smaller custom dataset that does not include passenger count. `distance_km` was already provided in the file; a separate `trip_distance` was engineered via the Haversine formula and both were used as features.

## Methodology

1. **Data Understanding** — shape, dtypes, missing values, duplicates, summary stats.
2. **Data Cleaning** — dropped duplicates, kept only `status == 'Completed'`, removed invalid coordinates, non-positive fares, and top 0.5% fare outliers.
3. **Feature Engineering** — extracted `pickup_year`, `pickup_month`, `pickup_day`, `pickup_hour`, `day_of_week`; computed `trip_distance` using Haversine.
4. **EDA** — fare distribution, trip distance distribution, fare vs distance, fare by hour/day/month, correlation matrix.
5. **Modeling** — 80/20 train/test split. Linear Regression vs Random Forest (n_estimators=100).
6. **Evaluation** — MAE, MSE, RMSE, R².

## Results

| Model | MAE | MSE | RMSE | R² |
|---|---|---|---|---|
| Linear Regression | 2.4654 | 9.4143 | 3.0683 | 0.7428 |
| Random Forest | 2.5127 | 9.9500 | 3.1544 | 0.7281 |

**Best model:** Linear Regression (RMSE 3.07, R² 0.743)

## Business Answers

1. **What factors most strongly influence Uber fares?**
   `distance_km` is by far the strongest — 79% feature importance in the Random Forest. `trip_distance`, pickup/dropoff latitude, and `pickup_hour` each contribute 2–5%.

2. **How does trip distance affect fare?**
   Distance is the dominant feature in the model. However, the direct linear correlation between `trip_distance` and `fare_amount` in this dataset is only -0.0002, which suggests the relationship is non-linear and that `distance_km` (the provided column) captures it better than the Haversine-derived distance.

3. **Does passenger count significantly affect fare?**
   Cannot be assessed — `passenger_count` is not present in this dataset.

4. **Which hours have higher average fares?**
   Averages range narrowly from $15.61 (hour 0) to $16.13 (hour 18). There is no strong hour-of-day signal in this data.

5. **Which model performs best?**
   Linear Regression, with RMSE 3.0683 and R² 0.7428.

6. **How accurate is the final model?**
   On average, predictions are off by ~$2.47 (MAE). R² of 0.743 means the model explains ~74% of the variance in fare.

7. **Can the model provide a reasonable fare estimate for a new trip?**
   Yes — the Streamlit app in `app/app.py` takes trip inputs and returns a fare estimate using the saved model.

## Project Structure
