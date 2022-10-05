import streamlit as st
import numpy as np
import plotly.graph_objects as go 
import pandas as pd

st.title("Dashboard Regressione lineare")
st.write(r'''
# Report

## Introduzione Regressione Lineare
Come funziona la regressione lineare?
> $y = w0 + w1x1 + w2x2 \dots wnxn$

## Codice esempio

''')


#a = 0.1*np.random.random(1000)
#b = -0.1*np.random.random(1000)
X1  = np.linspace(0,20,1000)
#Y = np.cos(X1)*np.exp(-0.2*X1) +a + b

#data = {
#    "x": X1, 
#    "y": Y
#}
#df = pd.DataFrame(data)
df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vS0qs6nT7qbHVMlxb596iF3qynx8foUEkQWK-1EiEL6NrTxZzvwr6OyV2cvTy5YcQ/pub?output=csv")
X1 = df["x"].values
Y = df["y"].values


#save = st.button("Save")
#if save:
#    df.to_excel("dataset.xlsx", index=False)

st.dataframe(df)

Y = Y.reshape(-1,1)
fig_original_data = go.Figure()
fig_original_data.add_traces( go.Scatter( x=X1,y=Y[:,0], mode="markers", name="res" ))
st.plotly_chart(fig_original_data, use_container_width=True)

fig_filtered = go.Figure()
Y_hat_f = []
#l = 30
l = st.slider("Approximation", min_value=10, max_value=100, value=30, step=10)
for i in range(0,len(X1),l):
    Xt = X1[i:i+l]
    Yt = Y[i:i+l]
    X = np.array([ np.ones(len(Xt)), Xt]).T # np.power(X1,2),np.power(X1,3),np.power(X1,4),np.power(X1,5),np.power(X1,6),np.power(X1,7),np.power(X1,8),np.power(X1,9)]).T
    #print(X.shape,Yt.shape)
    W = np.matmul( np.linalg.inv( np.matmul( X.T, X ) ) , np.matmul( X.T, Yt ) )
    Y_hat = np.matmul(W.T, X.T).T
    Y_hat_f.extend(Y_hat.reshape(-1))
    fig_filtered.add_traces( go.Scatter( x=Xt,y=Y_hat.reshape(-1), mode="markers", name=f"line {i}" ))




st.plotly_chart(fig_filtered, use_container_width=True)