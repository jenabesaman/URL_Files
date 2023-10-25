import wget
import os
from bs4 import BeautifulSoup
import requests

# Define the URL of the website you want to download
url = 'https://galaxy.framer.website/'  # Replace with the URL of the website you want to download

# Define the local directory where you want to save the website
local_directory = 'downloaded_website'  # Replace with your desired directory path

# Create the local directory if it doesn't exist
if not os.path.exists(local_directory):
    os.makedirs(local_directory)

# Download the main page (HTML) of the website
wget.download(url, out=local_directory)

# Create a BeautifulSoup object to parse the HTML
with open(os.path.join(local_directory, 'index.html'), 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all links (e.g., images, CSS, JavaScript files) on the page
links = soup.find_all('a', href=True)
for link in links:
    link_url = link['href']
    if link_url.startswith('http') or link_url.startswith('www'):
        response = requests.get(link_url)
        if response.status_code == 200:
            wget.download(link_url, out=local_directory)

print("Website downloaded successfully to", local_directory)