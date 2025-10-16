import streamlit as st

st.title("Hello, World")
st.write(
  "I wrote this to learn python if it works. "
  "W's in the chat"
)

st.number_input("How happy are you?", min_value=0, max_value=10, value=5)
st.number_input("How sad are you?", min_value=0, max_value=10, value=5)
st.write(
  "Ts is so cool. "
)
st.write(
  "This should be below"
)
st.write(
  "attempting to make a BMI calculator"
)
weight=st.number_input("Weight (lbs)", min_value=0, max_value=1000, value=0)
height=st.number_input("Height (In)", min_value=0, max_value=100, value=0)
