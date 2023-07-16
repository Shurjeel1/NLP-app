import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape data from a URL
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    scraped_data = []

    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        scraped_data.append({'Author': author, 'Quote': text})

    return scraped_data

# Streamlit application code
def main():
    st.title("Web Scraping Application")

    # User input for the URL to scrape
    url = st.text_input("Enter the URL to scrape:")

    # Scrape button
    if st.button("Scrape"):
        # Check if the URL is provided
        if url:
            # Call the scrape_data function to perform scraping
            scraped_data = scrape_data(url)

            # Display the scraped data
            st.write("Scraped Data:")
            for data in scraped_data:
                st.write(f"Author: {data['Author']}")
                st.write(f"Quote: {data['Quote']}")
                st.write("---")
        else:
            st.write("Please enter a URL to scrape.")

if __name__ == "__main__":
    main()
