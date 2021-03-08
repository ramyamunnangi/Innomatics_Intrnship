import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
img_loc ="data/feedback.jpg"
img_feedback= Image.open(img_loc)
st.image(img_feedback,use_column_width=True)
st.markdown("<h1 style='text-align: center; color: red;'> DATA PREDICTION</h1>", unsafe_allow_html=True)

col1= st.number_input("col1")
col2= st.number_input("col2")
column_names = ['col1', 'col2']
df = pd.DataFrame(columns = column_names)


def standardization (df):
    from sklearn.preprocessing import StandardScaler
    standardized_data = StandardScaler().fit_transform(df)
    df2 = pd.DataFrame(standardized_data,columns = features)
def predict(df2):
    from pickle import dump,load
    classifier=load(open('pickle/dump.pkl','rb'))
    prediction = classifier.predict(df2)
click = st.button('SUBMIT')
if click:
    def main():
        clean_df(df)
        standardization(df)
        predict(df2)
    if predict==0:
        st.write('you are output iscorrect')
    else:
        st.write('you are  output is not correct')









#if(__name__ == '__main__'):
    #main()
