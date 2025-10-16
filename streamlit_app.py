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
weight=st.number_input("Weight (kg)", min_value=0, max_value=1000, value=0)
height=st.number_input("Height (cm)", min_value=0, max_value=100, value=0)

if st.button("Calculate BMI"):
  if weight>0 and height>0:
    calculated_bmi=weight/((height/100)**2)
    st.success(f"Your caluclated BMI is  **{calculated_bmi:.2f}**")
    bmi=calculated_bmi
  else:
      st.warning("Please enter both weight and height to calculate for BMI")

score=st.number("score", value=0)

if st.button("Click!"):
  if score>0:
    st.write(
    "Good job"
)
