import streamlit as st
import pandas as pd
import os

# Check if the file exists
file_path = os.path.join(os.path.dirname(__file__), 'vehicles_us.csv')
st.write(f"File path: {file_path}")

try:
    # Attempt to load the CSV file with a simple encoding
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    st.write("File loaded successfully.")
    st.write(df.head())  # Display the first few rows to verify data
except Exception as e:
    st.error(f"Error reading the CSV file: {e}")
