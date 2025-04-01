import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("Lightning Strike(2018).csv")

data = load_data()

# Display dataset preview
st.title("Lightning Strikes Dataset Overview")
st.write("This application provides an overview of the lightning strikes dataset.")

st.subheader("Dataset Sample")
st.dataframe(data.head()) #displays a DataFrame in a scrollable and interactive format on the app. data.head() shows the first 5 rows

st.subheader("Basic Statistics")
st.write(data.describe())

st.subheader("Column Information")
st.write(data.dtypes)
