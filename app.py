
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

 # load model
model = pickle.load(open('model_gb.pkl', 'rb'))

# title
st.title('Insurance Premium Price Prediction App')

Age = st.number_input('Age', min_value=1, max_value=100, value=25)
Gender = st.selectbox('Gender', ('male', 'female'))
Bmi = st.number_input('Bmi', min_value=10.0, max_value=100.0, value=20.0)
Smoker = st.selectbox('Smoker', ('yes', 'no'))
Children = st.number_input('Children', min_value=0, max_value=10, value=2)
Region = st.selectbox('Region', ('southwest', 'southeast', 'northwest', 'northeast'))

# encoding

# smoker
smoker_val = 1 if Smoker == 'yes' else 0

# gender
sex_female = 1 if Gender == 'female' else 0
sex_male = 1 if Gender == 'male' else 0

# region
region_dict = {'southwest': 1, 'southeast': 2, 'northwest': 3, 'northeast': 4}
region_val = region_dict[Region]

# dataframe
input_features = pd.DataFrame({
    'age': [Age],
    'bmi': [Bmi],
    'children': [Children],
    'Smoker': [smoker_val],
    'sex_female': [sex_female],
    'sex_male': [sex_male],
    'Region': [region_val]
})

# prediction
if st.button('Predict'):
    prediction=model.predict(input_features)
    output=round(np.exp(prediction[0]),2)
    st.success(f'The insurance premium price is {output}')
    
