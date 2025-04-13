import streamlit as st
import time
import os
from scrape import (
    scrape_website,
    extract,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama
from dotenv import load_dotenv
load_dotenv()

# Streamlit UI
st.title("AI Job Scraper")
if st.button("Google"):
    url = os.getenv('google')
# Step 1: Scrape the Website
    if url:
        # Scrape the website
        with st.status("Scraping...", expanded=True) as status:
            st.write("Searching for data...")
            time.sleep(5)
            dom_content = scrape_website(url)
            st.write("Found URL.")
            time.sleep(3)
            body_content = extract(dom_content)
            st.write("Downloading data...")
            time.sleep(3)
            cleaned_content = clean_body_content(body_content)
            status.update(label="Download complete!", state="complete", expanded=False)

            
            # Store the DOM content in Streamlit session state
            st.session_state.dom_content = cleaned_content

        # Display the DOM content in an expandable text box
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)


# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)