import streamlit as st

st.title("Hello!, I am srikanth yadav")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("Wellcome my first data ap")
    st.balloons()