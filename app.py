import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set the port for Render deployment
port = int(os.environ.get("PORT", 8501))

# Check if the file exists
file_path = os.path.join(os.path.dirname(__file__), 'vehicles_us.csv')
st.write(f"File path: {file_path}")

try:
    # Try loading the CSV file with a common encoding fallback
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    st.write("File loaded successfully.")
except (FileNotFoundError, UnicodeDecodeError):
    st.error("Error loading the CSV file. Make sure 'vehicles_us.csv' exists in the project directory and has the correct encoding.")
    df = None

# Header
st.header("Car Advertisement Data Analysis")

if df is not None:
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
else:
    st.error("Data could not be loaded, so no charts are displayed.")
