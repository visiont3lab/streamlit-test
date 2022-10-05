import streamlit as st

st.title("Dashboard Manuel")

test = st.button("Test")

if test:
    st.text("Ho premuto iao")
else:
    st.text("Ciao")
