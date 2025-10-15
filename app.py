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
#st.write("Displaying the first 5 rows of the loaded DataFrame:")

# st.dataframe() displays an interactive table, and .head() selects the first 5 rows
st.dataframe(df_url)#.head()) 

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
        title='Pie chart of Gender in Arts Faculty',
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

#Third CODE
# --- Data Loading Function (re-using the cached function from previous examples) ---
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

st.title("Distribution of Bachelor Academic Year in EU 📊")

if not df_url.empty:
    # 1. Data Processing
    # Ensure the column name is exact, including any hidden characters if present.
    # It seems there might be a non-breaking space ( ) in 'Bachelor Academic Year in EU'.
    # Let's try to access it correctly or clean column names if needed.
    
    # You might want to print df_url.columns to confirm the exact column name
    # st.write(df_url.columns) 
    
    # Using a robust way to find the column if the name has tricky spaces:
    #column_name = [col for col in df_url.columns if 'Bachelor Academic Year in EU' in col][0]
    
    bachelor_year_counts = df_url[column_name].value_counts().reset_index()
    bachelor_year_counts.columns = ['Academic_Year', 'Count']
    
    # Ensure the academic year is sorted for better visualization if it's numerical
    # (assuming academic years are usually numbers, e.g., 1, 2, 3)
    bachelor_year_counts['Academic_Year'] = pd.to_numeric(
        bachelor_year_counts['Academic_Year'], errors='coerce'
    ).fillna(bachelor_year_counts['Academic_Year'])
    
    bachelor_year_counts = bachelor_year_counts.sort_values('Academic_Year')


    # 2. Create the Plotly Bar Chart
    # Use Plotly Express to create the bar chart
    fig = px.bar(
        bachelor_year_counts,
        x='Academic_Year',
        y='Count',
        title='Bar Chart of Bachelor Academic Year in EU',
        labels={'Academic_Year': 'Academic Year', 'Count': 'Number of Students'},
        # To make bars purple and differentiate them, use a sequential purple color scale
        # Plotly Express automatically assigns different shades if 'color' is mapped to a column
        color='Count', # This will assign colors based on the count, creating a gradient
        color_continuous_scale=px.colors.sequential.Purples # Use a sequential purple palette
    )

    # 3. Customize the layout for better readability (similar to tight_layout and xticks rotation)
    fig.update_layout(
        xaxis_title='Academic Year',
        yaxis_title='Count',
        xaxis_tickangle=-45, # Rotates x-axis labels
        hovermode="x unified" # Enhances hover experience
    )
    
    # Ensure discrete x-axis if academic years are categories
    fig.update_xaxes(type='category')


    # 4. Display the Chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Could not process data because the DataFrame is empty.")
