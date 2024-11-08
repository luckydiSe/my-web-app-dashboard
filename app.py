import streamlit as st
import pandas as pd
import plotly.express as px
import os
if not os.path.exists('vehicles_us.csv'):
    raise FileNotFoundError("The file 'vehicles_us.csv' was not found. Please make sure it exists in the project directory.")

# Construct the path to 'vehicles_us.csv' relative to the script's location
file_path = os.path.join(os.path.dirname(__file__), 'vehicles_us.csv')
df = pd.read_csv(file_path)

# Header
st.header("Car Advertisement Data Analysis")

# Histogram of Car Prices
st.subheader("Distribution of Car Prices")
fig_price = px.histogram(df, x="price", nbins=50, title="Distribution of Car Prices")
fig_price.update_xaxes(range=[0, 100000])
st.plotly_chart(fig_price)  # Display the histogram

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

# Display the scatter plot with a unique key
st.plotly_chart(fig1, key="price_days_scatter")
