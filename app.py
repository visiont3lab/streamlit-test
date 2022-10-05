import streamlit as st

st.title("Dashboard")

test = st.button("Test")

if test:
    st.text("Ho premuto")
else:
    st.text("Ciao")