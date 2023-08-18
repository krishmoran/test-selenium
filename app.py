import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from streamlit import components

from sites import *

# Define a function to create the search page
def create_search_page():
    # Create a search page with a title and a search bar
    st.title("Product Price Comparison")
    search_term = st.text_input("Enter a product name:")

    # Add a button to start scraping the prices
    if st.button("Search"):
        with st.spinner('Fetching data. Please wait...'):
            # Define the URLs for Amazon, Best Buy, and Walmart
            daraz_df = daraz("https://www.daraz.lk/catalog/?q=" + search_term.replace(" ", "+"))
            kapruka_df = kapruka("https://www.kapruka.com/srilanka_online_shopping.jsp?d=" + search_term.replace(" ", "%20"))

            # Convert the "Image Link" column to HTML with image tags
            def convert_images():
                daraz_df["Image Link"] = daraz_df["Image Link"].apply(
                    lambda x: '<img src="' + x + '" width="60" >')
                kapruka_df["Image Link"] = kapruka_df["Image Link"].apply(
                   lambda x: '<img src="' + x + '" width="60" >')

            def merge_dataframes():
                # Merge the dataframes vertically
                merged_df = pd.concat([daraz_df, kapruka_df], axis=0)
                return merged_df

            convert_images()
            merged_df = merge_dataframes()

            html = merged_df.to_html(escape=False)
            # Display the prices in a table

            st.markdown(
                html,
                unsafe_allow_html=True
            )

# Create the search page
create_search_page()