# Insurance Premium Prediction App

A Machine Learning web application built using Streamlit that predicts insurance premium based on user inputs such as age, BMI, smoking habits, and region.

---

## Features
- Predict insurance cost instantly
- User-friendly interface
- Real-time input handling
- Powered by a trained Machine Learning model

---

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Machine Learning Model
- Model Used: Gradient Boosting Regressor
- Trained on insurance dataset
- Features used:
  - Age
  - BMI
  - Children
  - Smoker (encoded: yes=1, no=0)
  - Gender (one-hot encoded)
  - Region (label encoded)

---

## Input Parameters
- Age
- Gender
- BMI
- Smoker
- Children
- Region

---

## How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
