import pandas as pd
import streamlit as st # Import the streamlit library
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

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
#_________________________________________________________________________________________________________________________________________
#code kedua
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
#_________________________________________________________________________________________________________________________________________
#code ketiga
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
    column_name = [col for col in df_url.columns if 'Bachelor  Academic Year in EU' in col][0]
    
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
        color_continuous_scale=px.colors.sequential.Plasma # Use a sequential purple palette
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
#_________________________________________________________________________________________________________________________________________
#code 4
# --- Data Loading Function (Assumed to be defined and used above this snippet) ---
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
# --------------------------------------------------------------------------------

st.title("Student Coaching Center Attendance 🎓")

if not df_url.empty:
    # 1. Safely find the column name
    search_term = 'Did you ever attend a Coaching center?'
    column_list = [col for col in df_url.columns if search_term in col]

    if not column_list:
        st.error(f"Required column containing '{search_term}' not found in the data.")
    else:
        column_name = column_list[0]

        # 2. Data Processing: Calculate counts and prepare DataFrame for Plotly
        coaching_counts_df = df_url[column_name].value_counts().reset_index()
        coaching_counts_df.columns = ['Attended_Coaching_Center', 'Count']

        # 3. Create the Plotly Pie Chart (equivalent to plt.pie)
        fig = px.pie(
            coaching_counts_df,
            values='Count',
            names='Attended_Coaching_Center',
            title='Total Students Who Attend a Coaching Center',
            # You can customize the colors here, e.g., use a distinct palette
            color_discrete_sequence=px.colors.qualitative.Pastel
        )

        # Enhance layout for better presentation (displaying percentage and label inside)
        fig.update_traces(textposition='inside', textinfo='percent+label')

        # 4. Display the Chart
        st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Could not process data because the DataFrame is empty.")

#_________________________________________________________________________________________________________________________________________
#code 5
# --- Data Loading Function (Assumed to be defined and used above this snippet) ---
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
# --------------------------------------------------------------------------------

st.title("Program Improvement Suggestions by Gender 🧑‍🎓👩‍🎓")

if not df_url.empty:
    # 1. Safely find the column names
    gender_col = 'Gender'
    search_term = 'What aspects of the program could be improved?'
    
    # Robustly find the improvement column (handling potential invisible spaces)
    improvement_col_list = [col for col in df_url.columns if search_term in col]
    
    if not improvement_col_list:
        st.error(f"Required column containing '{search_term}' not found in the data.")
    elif gender_col not in df_url.columns:
        st.error(f"Required column '{gender_col}' not found in the data.")
    else:
        improved_aspects_column = improvement_col_list[0]

        # 2. Data Cleaning and Transformation (Same Pandas logic as before)
        
        # Drop rows with missing values in the relevant columns
        df_cleaned = df_url.dropna(subset=[gender_col, improved_aspects_column]).copy()

        # Split the multiple responses and stack them
        df_split = df_cleaned.assign(**{
            improved_aspects_column: df_cleaned[improved_aspects_column].astype(str).str.split(',')
        }).explode(improved_aspects_column)

        # Clean up any leading/trailing whitespace
        df_split[improved_aspects_column] = df_split[improved_aspects_column].str.strip()

        # Group by gender and the improved aspects, then count the occurrences
        grouped_counts = df_split.groupby([gender_col, improved_aspects_column]).size().reset_index(name='Count')
        
        # Filter out empty or meaningless responses that resulted from splitting
        grouped_counts = grouped_counts[grouped_counts[improved_aspects_column] != '']

        # 3. Create the Plotly Grouped Bar Chart (Replaces Seaborn/Matplotlib)
        
        # Define custom colors (Plotly uses color names or hex codes)
        colors_map = {'Male': 'lightblue', 'Female': 'lightcoral'} # Using lightcoral for visibility

        fig = px.bar(
            grouped_counts,
            x=improved_aspects_column,
            y='Count',
            color=gender_col,          # 'hue' equivalent
            barmode='group',           # Displays bars side-by-side
            title='Aspects of the Program that Could Be Improved by Gender',
            labels={'Count': 'Number of Respondents', improved_aspects_column: 'Aspects to Improve'},
            color_discrete_map=colors_map # Apply the custom colors
        )

        # 4. Customizing the layout (Replacing plt.xticks(rotation=45) and plt.tight_layout())
        fig.update_layout(
            xaxis_title='Aspects to Improve',
            yaxis_title='Number of Respondents',
            xaxis_tickangle=-45,
            legend_title_text='Gender',
            # Move legend to the top for better use of space
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1) 
        )
        
        # Ensure categories are treated as strings
        fig.update_xaxes(type='category')

        # 5. Display the Chart
        st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Could not process data because the DataFrame is empty.")

#_________________________________________________________________________________________________________________________________________
#code 6
# --- Data Loading Function (Assumed to be defined and used for efficiency) ---
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
# --------------------------------------------------------------------------------

st.title("Distribution of Responses to 'Classes are mostly' 🏫")

if not df_url.empty:
    # 1. Safely find the column name
    search_term = 'Classes are mostly'
    column_list = [col for col in df_url.columns if search_term in col]

    if not column_list:
        st.error(f"Required column containing '{search_term}' not found in the data.")
    else:
        column_name = column_list[0]

        # 2. Data Processing: Calculate counts and prepare DataFrame for Plotly
        classes_counts_df = df_url[column_name].value_counts().reset_index()
        classes_counts_df.columns = ['Class_Type', 'Count']
        
        # Sort the results by count (optional, but good practice for bar charts)
        classes_counts_df = classes_counts_df.sort_values('Count', ascending=False)

        # 3. Create the Plotly Bar Chart (Replaces Matplotlib)
        fig = px.bar(
            classes_counts_df,
            x='Class_Type',
            y='Count',
            title='Distribution of Responses to "Classes are mostly"',
            labels={'Class_Type': 'Class Type', 'Count': 'Count'},
            
            # Attractive Color: Use a sequential color scale like "Blues"
            color='Count', 
            color_continuous_scale=px.colors.sequential.Blues
        )

        # 4. Customizing the layout (Replacing plt.xticks(rotation=45) and plt.tight_layout())
        fig.update_layout(
            xaxis_title='Class Type',
            yaxis_title='Count',
            xaxis_tickangle=-45, # Rotates the x-axis labels
            hovermode="x unified"
        )
        
        # Ensure categories are treated as strings
        fig.update_xaxes(type='category')

        # 5. Display the Chart
        st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Could not process data because the DataFrame is empty.")

#_________________________________________________________________________________________________________________________________________
#code 7
# --- Data Loading Function (Retained for application context) ---
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
# ---------------------------------------------------------------

st.title("Average Performance by Semester and Year Heatmap 📈")

if not df_url.empty:
    
    # 1. ROBUST COLUMN IDENTIFICATION (Most likely source of the error)
    
    # Define a list of expected column name segments
    search_list = []
    for year in range(1, 5):
        year_str = f"{year}st" if year == 1 else f"{year}th"
        for sem in range(1, 4):
            search_list.append(f"{year_str} Year Semester {sem}")

    # Find the actual columns in the DataFrame using flexible substring matching
    actual_semester_columns = []
    
    # Normalize DataFrame column names to remove common invisible spaces
    normalized_df_cols = [col.replace('\xa0', ' ').strip() for col in df_url.columns] 
    
    # Create a mapping from normalized name back to original name
    col_map = {normalized_df_cols[i]: df_url.columns[i] for i in range(len(df_url.columns))}

    for expected_substring in search_list:
        # Search the normalized names for the expected substring
        found = [norm_col for norm_col in col_map.keys() if expected_substring in norm_col]
        
        if found:
            # Add the original, exact column name to our list
            actual_semester_columns.append(col_map[found[0]])
        # Note: If not found, it's simply skipped, leading to fewer columns, which is handled below.

    # 2. DATA PROCESSING AND RESHAPE CHECK
    
    if len(actual_semester_columns) < 12:
        st.warning(f"Could only find {len(actual_semester_columns)} out of 12 required semester columns. Visualization may be incomplete or impossible.")
        st.write("Columns found:", actual_semester_columns)
        
        # If less than 12 columns are found, stop here to avoid the reshape error
        # A more complex script could handle this by reshaping to (N, 3) where N < 4, but let's assume 12 are needed.
        if len(actual_semester_columns) != 12:
            st.error("Cannot create a complete 4x3 heatmap. Please check column names in your CSV.")
            return # Exit the function if we can't proceed
    
    # Proceed only if we have all 12 columns
    semester_df = df_url[actual_semester_columns]

    # Convert data to numeric
    semester_df = semester_df.apply(pd.to_numeric, errors='coerce')
    semester_means = semester_df.mean()
    
    # If the number of means is not 12, it still indicates a structural issue, but let's trust the column selection now.
    
    # Reshape the data for the heatmap (This is where the IndexError was likely occurring)
    heatmap_data = np.array(semester_means).reshape(4, 3) # 4 years, 3 semesters

    # Define labels and text for Plotly
    x_labels = ['Sem 1', 'Sem 2', 'Sem 3']
    y_labels = ['Year 1', 'Year 2', 'Year 3', 'Year 4']
    text_data = np.round(heatmap_data, decimals=2)

    # 3. Create and Display Plotly Heatmap
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data,
        x=x_labels,
        y=y_labels,
        colorscale='RdBu', 
        colorbar=dict(title='Average Score'),
        text=text_data,
        texttemplate="%{text}",
        hoverinfo="z+x+y"
    ))

    fig.update_layout(
        title='Average Performance by Semester and Year',
        xaxis_title='Semester',
        yaxis_title='Year',
        yaxis=dict(autorange="reversed") 
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Could not process data because the DataFrame is empty.")


