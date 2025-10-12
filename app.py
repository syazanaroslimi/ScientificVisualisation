import pandas as pd
import streamlit as st # Import the streamlit library
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

#SECOND CODE
# --- Data Loading Function (Same as before, using caching) ---
@st.cache_data
def load_data():
    """Loads the student survey data from a public URL."""
    url = 'https://raw.githubusercontent.com/syazanaroslimi/ScientificVisualisation/refs/heads/main/ARTS_STUDENT-SURVEY_exported.csv'
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Load the DataFrame
df_url = load_data()

st.title("Gender Distribution in Arts Faculty (Pie Chart) 📊")

if not df_url.empty:
    # 1. Data Processing
    gender_counts_df = df_url['Gender'].value_counts().reset_index()
    gender_counts_df.columns = ['Gender', 'Count']

    # 2. Create the Plotly Pie Chart (The 'hole' parameter is REMOVED)
    fig = px.pie(
        gender_counts_df,
        values='Count',
        names='Gender',
        title='Distribution of Gender in Arts Faculty',
        hover_data=['Count'],
        labels={'Count':'Number of Students'}
        # Removed: hole=0.4 ⬅️ This is what caused the donut chart!
    )

    # Enhance layout for better presentation
    fig.update_traces(textposition='inside', textinfo='percent+label')
    
    # 3. Display the Chart
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Could not process data because the DataFrame is empty.")
