# This file is a Stramlit application used to built Fast GUI template with less efforts.
# This code is a Streamlit application that allows users to search for companies by name or industry, view details about selected companies, and access quick links and contact information. It uses a CSV file as the data source and provides filtering capabilities based on user input.

import streamlit as st
import pandas as pd
import ast

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    return df

df = load_data()


st.title("Company Search Portal")

# Sidebar search options
search_by = st.sidebar.selectbox(
    "Search by",
    ("Company Name", "Industry")
)

query = st.sidebar.text_input("Enter search term:")


# Filter logic
def filter_df(df, search_by, query):
    if not query:
        return df
    if search_by == "Industry":
        # Match query in both Industry and Specialties columns
        mask = df["Industry"].str.contains(query, case=False, na=False) | \
               df["Specialties"].str.contains(query, case=False, na=False)
        return df[mask]
    else:
        # For Company Name and Specialties, match only the selected column
        col = search_by
        return df[df[col].str.contains(query, case=False, na=False)]

filtered_df = filter_df(df, search_by, query)

st.write(f"### Results ({len(filtered_df)})")
st.dataframe(filtered_df)


# Show details for a selected company
if not filtered_df.empty:
    selected = st.selectbox("Select a company for details", filtered_df["Company Name"])
    details = filtered_df[filtered_df["Company Name"] == selected].iloc[0]
    st.write("#### Company Details")
    st.write(f"**Company Name:** {details['Company Name']}")
    st.write(f"**Website:** {details['Website']}")

    st.write(f"**Industry:** {details['Industry']}")
    st.write(f"**Company Size:** {details['Company Size']}")
    st.write(f"**Specialties:** {details['Specialties']}")
    st.write(f"**Headquarters:** {details['Headquarters']}")
    st.write(f"**Overview:** {details['Overview']}")
    
    st.write("**Quick Links:**")
    quick_links = ast.literal_eval(details["Quick Links"])["Quick_links"]
    for section, url in quick_links.items():
        if url and url != "None":
            st.markdown(f"- [{section.title()}]({url})", unsafe_allow_html=True)
        
    st.write("**Contact Info:**")
    contact_info = ast.literal_eval(details["Contact Info"])["Contact_info"]
    st.write(f"- **Email:** {contact_info['Email']}")
    st.write(f"- **Mobile:** {contact_info['Phone']}")
    st.write(f"- **Location:** {contact_info['Location']}")

    