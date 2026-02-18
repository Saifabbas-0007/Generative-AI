import streamlit as st
import pandas as pd 

st.title("Text Input")

name = st.text_input("Enter Your Name:")

age = st.slider("Select Your Age:",0,100,18)

#st.write(f"your age is {age}.") 

option =  ["Python","Java","C++","SQL"]
choice = st.selectbox("Choose Your Favourite Language:",option)


if name:
    st.write(f"Hello {name}!!")
    
st.write(f"your age is {age}.")
    
st.write(f"You Selected {choice}.")

data = {
    "Name":["saif","Abbas","Haider","Faiz"],
    "Age":[23,22,24,23],
    "City":["Akbarpur","Noida","Akbarpur","Delhi"]
    
}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

## Upload files

uploaded_files = st.file_uploader("Choose a csv file",type= 'csv')
if uploaded_files is not None:
    df=pd.read_csv(uploaded_files)
    st.write(df) #display
