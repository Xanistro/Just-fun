import streamlit as st

st.title("Click the button to increase yoour score")

If "score" no in st.session_state:
  st.session_state.score=0

st.write(f"**Your current score:** {st.session_state.score}")

if st.button("Increase Score"):
    st.session_state.score += 1
    st.success(f"✅ Score increased! New score: {st.session_state.score}")
