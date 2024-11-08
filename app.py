import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Check if the file exists
file_path = os.path.join(os.path.dirname(__file__), 'vehicles_us.csv')
st.write(f"File path: {file_path}")

if not os.path.exists(file_path):
    st.error("The file 'vehicles_us.csv' was not found. Please make sure it exists in the project directory.")
else:
    try:
        # Attempt to load the CSV file with specified encoding
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
        st.write("File loaded successfully.")
    except Exception as e:
        st.error(f"Error reading the CSV file: {e}")

# Header
st.header("Car Advertisement Data Analysis")

# Histogram of Car Prices
st.subheader("Distribution of Car Prices")
fig_price = px.histogram(df, x="price", nbins=50, title="Distribution of Car Prices")
fig_price.update_xaxes(range=[0, 100000])
st.plotly_chart(fig_price)

# Scatter Plot: Price vs. Days Listed with Adjustable Range
st.subheader("Price vs. Days Listed (Adjustable Range)")
show_full_range = st.checkbox("Show full price range")

# Create the scatter plot
fig1 = px.scatter(df, x='days_listed', y='price', title="Price vs. Days Listed",
                  labels={'days_listed': 'Days Listed', 'price': 'Price ($)'})

# Update the y-axis range based on checkbox state
if show_full_range:
    fig1.update_yaxes(range=[0, df['price'].max()])
else:
    fig1.update_yaxes(range=[0, 100000])

# Display the scatter plot
st.plotly_chart(fig1)
