import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# Load the dataset
df = pd.read_csv('banking.csv')

# Create a multipage structure
st.set_page_config(page_title="Banking App", page_icon=":bank:", layout="wide")

# Function to load and encode an image file
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# # Specify the local image file path (ensure the path is correct)
# img_file_path = "C:\Users\nazif\SHRDC\Jupyter Notebook\Day 4\banking\background.png" 

# # Encode the image file to base64
# base64_img = get_base64_of_bin_file(img_file_path)

# # Background image or color styling
# page_bg_img = f'''
# <style>
# body {{
#     background-image: url("data:image/jpeg;base64,{base64_img}");
#     background-size: cover;
#     background-repeat: no-repeat;
#     background-attachment: fixed;
# }}
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Charts"])

if page == "Home":
    st.title("Welcome to the Banking Data App")
    st.write("This app helps you explore banking data interactively.")
    from PIL import Image
    logo = Image.open('background.png')
    st.image(logo)

elif page == "Charts":
    st.title("Interactive Charts")

    # Add a dropdown to filter by job type
    job_filter = st.selectbox("Select Job", options=["All"] + list(df['job'].unique()), index=0)

    # Filter the dataframe based on selected job type
    if job_filter != "All":
        filtered_df = df[df['job'] == job_filter]
    else:
        filtered_df = df

    # Create two columns
    col1, col2 = st.columns(2)

    # First chart in the first column
    with col1:
        st.subheader("Chart 1: Distribution of Age")
        fig1 = px.histogram(filtered_df, x='age', title=f"Age Distribution for {job_filter if job_filter != 'All' else 'All Jobs'}")
        st.plotly_chart(fig1)

    # Second chart in the second column (using 'duration' instead of 'balance')
    with col2:
        st.subheader("Chart 2: Duration by Job")
        fig2 = px.bar(filtered_df, x='job', y='duration', color="marital", title=f"Duration by Job for {job_filter if job_filter != 'All' else 'All Jobs'}")
        st.plotly_chart(fig2)

    # Add interactive control for marital status
    st.subheader("Filter by Marital Status")
    marital_status = st.selectbox("Choose marital status", options=["All"] + list(df['marital'].unique()))

    # Filter the dataframe based on selected marital status
    if marital_status != "All":
        filtered_df = filtered_df[filtered_df['marital'] == marital_status]

    # Show filtered data in chart and table
    st.write(f"Filtered Data by {marital_status} status:" if marital_status != "All" else "Complete Data:")
    st.write(filtered_df)