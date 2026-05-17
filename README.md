# 🔥 Calories Burnt Prediction Using Machine Learning & FastAPI

A Machine Learning project that predicts the number of calories burnt based on user activity and physical parameters. This project includes data preprocessing, feature engineering, regression model training, FastAPI deployment, and real-time prediction APIs.

---

# 🚀 Features

- ✅ Data Preprocessing & Cleaning
- ✅ Feature Engineering
- ✅ Regression Model Training
- ✅ Model Evaluation
- ✅ FastAPI Backend Deployment
- ✅ Real-time Prediction API
- ✅ Scalable ML API Structure
- ✅ Production Ready Project Structure

---

# 🛠️ Tech Stack

## Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn

## Backend
- FastAPI
- Uvicorn

## Model Deployment
- Joblib / Pickle

---



# 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Saving
7. FastAPI Deployment
8. Real-time Predictions

---

# 📌 API Endpoints

## Home Endpoint

```http
GET /
```

## Prediction Endpoint

```http
POST /predict
```

---

# 📥 Sample Input

```json
{
    "Gender": 1,
    "Age": 25,
    "Height": 175,
    "Weight": 70,
    "Duration": 30,
    "Heart_Rate": 120,
    "Body_Temp": 40
}
```

---

# 📤 Sample Output

```json
{
    "Predicted_Calories_Burnt": 245.67
}
```



