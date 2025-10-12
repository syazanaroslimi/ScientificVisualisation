import pandas as pd
import streamlit as st # Import the streamlit library

# Set the URL for the CSV file
url = 'https://raw.githubusercontent.com/syazanaroslimi/ScientificVisualisation/refs/heads/main/ARTS_STUDENT-SURVEY_exported.csv'

# Load the data from the URL into a pandas DataFrame
# Streamlit provides a caching mechanism (@st.cache_data) for functions 
# that load data, which is highly recommended for performance.
@st.cache_data
def load_data(data_url):
    """Loads data from a URL and returns a pandas DataFrame."""
    try:
        df = pd.read_csv(data_url)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on failure

# Call the function to load the data
df_url = load_data(url)

# Use Streamlit functions to display the DataFrame's head
st.title("Student Survey Data Preview 📊")
st.write("Displaying the first 5 rows of the loaded DataFrame:")

# st.dataframe() displays an interactive table, and .head() selects the first 5 rows
st.dataframe(df_url.head()) 

# Optionally, you can display the whole DataFrame (if it's not too big)
# st.subheader("Full DataFrame")
# st.dataframe(df_url)

