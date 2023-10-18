import numpy as np
import pickle
import streamlit as st

st.title("Diabetes Predictor System")
model=pickle.load(open("diabetespredictor.pkl","rb"))

def disease(input_data):
    ar=np.asarray(input_data)
    input_reshape=ar.reshape(1,-1)
    result=model.predict(input_reshape)
    if(result[0]==1):
        return st.success("You have diabtetes")
    else:
        return st.error("You Don't have diabetes")
def main():
    st.write("Prediction Model")
    Pregnancies=st.number_input("Enter number of Pregnancies")
    Glucose=st.number_input("Enter Glucose")
    BloodPressure=st.number_input("Enter Blood pressure")
    skt=st.number_input("Enter Skin Thickness")
    Insulin=st.number_input("Enter Inslin")
    BMI=st.number_input("Enter BMI")
    dpf=st.number_input("Enter Diabetes Pedigree Function")
    age=st.number_input("Enter age")
    diagonosis=''

    if st.button("PREDICT"):
        diagonosis=disease([Pregnancies,Glucose,BloodPressure,skt,Insulin,BMI,dpf,age])
if __name__=='__main__':
    main()

