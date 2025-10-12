import pandas as pd
import streamlit as st # Import the streamlit libraryimport pandas as pd
import plotly.express as px

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

# --- Setup: Assuming 'arts_df' is already loaded and available ---
# You would typically load your data here.
# For demonstration, let's create a dummy DataFrame that mimics the structure.
# In your actual app, replace this with your data loading logic (e.g., from the previous question).
data = {
    'Gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Other', 'Female', 'Male']
}
arts_df = pd.DataFrame(data)
# ----------------------------------------------------------------

st.title("Gender Distribution in Arts Faculty 🎭")

# 1. Calculate the counts (same logic as before)
gender_counts = arts_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count'] # Rename columns for Plotly clarity

# 2. Create the Plotly Pie Chart
# Plotly Express uses the DataFrame directly, making it very clean.
fig = px.pie(
    gender_counts,
    values='Count',          # The column to use for the size of the slices
    names='Gender',          # The column to use for the labels of the slices
    title='Distribution of Gender in Arts Faculty',
    hole=.3,                 # Optional: creates a donut chart
    color_discrete_sequence=px.colors.sequential.RdBu # Optional: set a color palette
)

# 3. Use Streamlit to display the interactive Plotly figure
st.plotly_chart(fig, use_container_width=True)

