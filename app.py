import streamlit as st
import numpy as np
import plotly.graph_objects as go 

a = 0.1*np.random.random(1000)
b = -0.1*np.random.random(1000)
X1  = np.linspace(0,20,1000)
Y = np.cos(X1)*np.exp(-0.2*X1) +a + b
Y = Y.reshape(-1,1)
fig = go.Figure()
fig.add_traces( go.Scatter( x=X1,y=Y[:,0], mode="markers", name="res" ))
fig.update_layout(
    title="Data",
    hovermode="x"
)

st.title("Dashboard Regressione lineare")

st.plotly_chart(fig, use_container_width=True)