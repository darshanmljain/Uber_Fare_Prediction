# 🚕 Uber Fare Prediction Model

An end-to-end machine learning regression project that estimates **Uber fare amounts before a trip is completed**, using historical ride information such as trip distance, pickup/drop-off coordinates, and time-based features. The project follows the complete ML workflow — data understanding, cleaning, feature engineering, exploratory data analysis, model training, evaluation, and business interpretation — to support data-driven fare estimation and pricing transparency.

---

## 📌 Project Objectives

- **Estimate Pre-Trip Fares:** Build a regression model that predicts `fare_amount` before the trip ends.
- **Understand Key Drivers:** Investigate which features most strongly influence Uber fares.
- **Engineer Trip Distance:** Compute Haversine distance from pickup and drop-off coordinates.
- **Compare Models:** Benchmark Linear Regression against Random Forest Regressor.
- **Evaluate Accuracy:** Assess model performance using MAE, MSE, RMSE, and R².
- **Generate Business Insights:** Translate findings into practical fare-estimation and pricing observations.

---

## 📊 Key Areas of Analysis

- **Data Understanding:** Shape, dtypes, missing values, duplicates, and descriptive statistics.
- **Data Cleaning:** Removal of cancelled/no-show trips, invalid coordinates, non-positive fares, and extreme fare outliers.
- **Feature Engineering:** Time-based features (`pickup_year`, `pickup_month`, `pickup_day`, `pickup_hour`, `day_of_week`) and Haversine-derived `trip_distance`.
- **Exploratory Data Analysis:** Fare distribution, trip-distance distribution, fare vs. distance, fare by hour / day / month, and correlation matrix.
- **Modeling:** Linear Regression baseline vs. Random Forest Regressor.
- **Model Evaluation:** MAE, MSE, RMSE, and R² comparison.
- **Business Interpretation:** Answers to the seven business questions defined in the project brief.

---

## 🛠️ Tech Stack & Tools

- **Environment:** Google Colab / Jupyter Notebook
- **Programming Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn (Linear Regression, Random Forest Regressor)
- **Model Persistence:** Joblib
- **App / Deployment:** Streamlit
- **Dataset:** `uber_trips_dataset_50k.csv`

---

## 📈 Model Performance

Two regression models were trained on an 80/20 train-test split and evaluated on the same test set.

| Model | MAE | MSE | RMSE | R² |
|---|---|---|---|---|
| Linear Regression | 2.4654 | 9.4143 | **3.0683** | **0.7428** |
| Random Forest | 2.5127 | 9.9500 | 3.1544 | 0.7281 |

**Best model:** Linear Regression — RMSE 3.0683, R² 0.7428.

The model explains approximately **74%** of the variance in fare amounts, with an average prediction error of about **$2.47**.

---

## 💡 Business Questions & Answers

1. **What factors most strongly influence Uber fares?**
   `distance_km` dominates feature importance at ~79%, followed by `trip_distance` (~5%) and pickup latitude (~3%).

2. **How does trip distance affect fare?**
   Trip distance is the most heavily used feature in the model. However, the direct linear correlation between the Haversine-derived `trip_distance` and `fare_amount` is near zero (-0.0002), indicating that the relationship is non-linear and that the provided `distance_km` column captures the signal more effectively.

3. **Does passenger count significantly affect fare?**
   Cannot be assessed — `passenger_count` is not present in this dataset.

4. **Which hours have higher average fares?**
   Average fares range narrowly from ~$15.61 (00:00) to ~$16.13 (18:00). There is no strong hour-of-day signal in this dataset.

5. **Which model performs best?**
   Linear Regression, with RMSE 3.0683 and R² 0.7428.

6. **How accurate is the final model?**
   On average, predictions are off by ~$2.47 (MAE). R² of 0.743 means the model explains roughly 74% of fare variance.

7. **Can the model provide a reasonable fare estimate for a new trip?**
   Yes — the Streamlit app in `app/app.py` accepts trip inputs and returns a fare prediction using the saved model.

---

## 💡 Business Recommendations

The analysis can help inform the following strategies, subject to validation against the notebook's actual findings:

1. **Prioritize Trip Distance:** Since `distance_km` drives ~79% of the model's decisions, ensure accurate distance estimation at the point of booking.
2. **Keep Baseline Models in Production:** Linear Regression outperformed Random Forest here — simpler models can be both more accurate and easier to maintain.
3. **Investigate Non-Linearity:** The mismatch between feature importance and linear correlation suggests a non-linear fare formula; consider polynomial features or gradient boosting for future iterations.
4. **Expand Feature Set:** Adding passenger count, weather, traffic, and surge-pricing indicators would materially improve predictions.
5. **Deploy as a Fare Estimator:** The trained model is production-ready for a lightweight pre-trip fare estimation service.

---

## 📁 Repository Structure

```text
Uber_Fare_Prediction/
│
├── app/
│   └── app.py                          # Streamlit fare-prediction app
├── charts/
│   ├── actual_vs_predicted.png
│   ├── correlation_matrix.png
│   ├── fare_by_day_of_week.png
│   ├── fare_by_hour.png
│   ├── fare_by_month.png
│   ├── fare_distribution.png
│   ├── fare_vs_distance.png
│   ├── feature_importance.png
│   └── trip_distance_distribution.png
├── dataset/
│   └── uber_trips_dataset_50k.csv
├── models/
│   └── uber_fare_model.pkl
├── notebooks/
│   └── Uber_Fare_Prediction.ipynb
├── outputs/
│   ├── business_answers.json
│   └── model_comparison.csv
├── .gitignore
├── README.md
└── requirements.txt
🚀 How to Run the Project
You can run this project in three ways: on Google Colab (easiest), locally with Python, or by deploying the Streamlit app online.

Option 1 — Google Colab (Recommended)
Go to Google Colab.

Click File → Upload notebook and select notebooks/Uber_Fare_Prediction.ipynb from this repository.

In the left sidebar, click the folder icon and upload dataset/uber_trips_dataset_50k.csv to /content/.

In the Colab menu, click Runtime → Run all.

The notebook will:

Load and clean the dataset

Engineer features

Generate all EDA charts (saved to outputs/charts/)

Train Linear Regression and Random Forest models

Save the best model as uber_fare_model.pkl

Export model_comparison.csv and business_answers.json

The final cell downloads uber_fare_prediction_outputs.zip automatically.

Option 2 — Run Locally with Python
Prerequisites
Python 3.9 or higher installed (python.org)

pip available in your terminal

Git (to clone the repository)

Steps
Clone the repository

bash
git clone https://github.com/darshanmljain/Uber_Fare_Prediction.git
cd Uber_Fare_Prediction
Create a virtual environment (recommended)

Windows:

bash
python -m venv venv
venv\Scripts\activate
macOS / Linux:

bash
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Run the Jupyter notebook (optional — to reproduce the analysis)

bash
jupyter notebook notebooks/Uber_Fare_Prediction.ipynb
Or open the notebook in VS Code with the Jupyter extension.

Launch the Streamlit app

bash
streamlit run app/app.py
The terminal will print a local URL (typically http://localhost:8501). Open it in your browser, enter trip details, and click Predict Fare.

Option 3 — Deploy the Streamlit App Online (Free)
To get a public, shareable demo link:

Push this repository to your own GitHub account.

Sign in at share.streamlit.io with GitHub.

Click Create app.

Fill in:

Repository: darshanmljain/Uber_Fare_Prediction

Branch: main

Main file path: app/app.py

Click Deploy. Streamlit Cloud will install dependencies from requirements.txt and give you a public URL such as:

text
https://uber-fare-prediction-darshanmljain.streamlit.app
Add that URL to the top of this README as the live demo link.

Expected Outputs After Running
File	Description
outputs/model_comparison.csv	MAE, MSE, RMSE, R² for both models
outputs/business_answers.json	Structured answers to the 7 business questions
models/uber_fare_model.pkl	Saved best-performing model (used by the Streamlit app)
charts/*.png	9 EDA and evaluation charts
Troubleshooting
pip not recognized → Use python -m pip install -r requirements.txt instead.

streamlit not found → Activate your virtual environment first, or run python -m streamlit run app/app.py.

Model file not found in app → Make sure models/uber_fare_model.pkl exists. Re-run the notebook if missing.

CSV parse error → Ensure dataset/uber_trips_dataset_50k.csv was fully downloaded (the last row may be truncated in the original file; the notebook skips it automatically).

🎯 Project Outcome
This project demonstrates a complete machine learning regression workflow — from raw ride data through cleaning, feature engineering, EDA, model training, evaluation, and deployment — applied to a real-world pricing problem. Linear Regression emerged as the best performer on this dataset, and the trained model is packaged with a Streamlit app for interactive fare estimation.

Note: The dataset used here is a smaller custom dataset and does not match the Kaggle Uber Fares Dataset referenced in the original project brief. passenger_count is not present in this dataset. Results should be interpreted according to this dataset's characteristics and are not directly comparable to results on the Kaggle dataset.

👨‍💻 Author
Darshan Jain

GitHub: @darshanmljain

Repository: Uber_Fare_Prediction