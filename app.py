import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Load the CSV file
file_path = os.path.join(os.path.dirname(__file__), 'vehicles_us.csv')

# Check if the file exists
if not os.path.exists(file_path):
    st.error("The file 'vehicles_us.csv' was not found. Please make sure it exists in the project directory.")
else:
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
        st.write("File loaded successfully.")

        # Handle missing values and convert types
        df.dropna(subset=['model_year', 'cylinders', 'odometer', 'paint_color'], inplace=True)
        df['is_4wd'] = df['is_4wd'].fillna(0).astype(int)
        df['model_year'] = df['model_year'].astype(int)

        if df.empty:
            st.error("The DataFrame is empty after cleaning.")
        else:
            st.write(df.info())

            # Histogram of Car Prices
            st.header("Car Advertisement Data Analysis")
            st.subheader("Distribution of Car Prices")
            fig_price = px.histogram(df, x="price", nbins=50, title="Distribution of Car Prices")
            fig_price.update_xaxes(range=[0, 100000])
            st.plotly_chart(fig_price)

            # Scatter Plot: Price vs. Days Listed with Adjustable Range
            st.subheader("Price vs. Days Listed (Adjustable Range)")
            show_full_range = st.checkbox("Show full price range")
            fig1 = px.scatter(df, x='days_listed', y='price', title="Price vs. Days Listed",
                              labels={'days_listed': 'Days Listed', 'price': 'Price ($)'})
            fig1.update_yaxes(range=[0, df['price'].max()] if show_full_range else [0, 100000])
            st.plotly_chart(fig1)

    except Exception as e:
        st.error(f"Error reading the CSV file: {e}")
