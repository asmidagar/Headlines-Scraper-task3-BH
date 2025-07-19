import requests
from bs4 import BeautifulSoup
from datetime import datetime

# RSS feed URL
url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"

# HTTP headers to avoid access denial
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; win64; x64)"
}

# Try to feth and parse the RSS feed
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    print(f"Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error fetching the RSS feed:\n{e}")
    exit()

# Use BeautifulSoup to parse the content as XML
try:
    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")
    print(f"Total headlines found: {len(items)}")
except Exception as e:
    print(f"Error parsing XML:\n{e}")
    exit()

# Dynamic file name with timestamp
filename = f"headlines_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"

# Save Headlines to the file
with open(filename, "w", encoding="utf-8") as f:
    for i, item in enumerate(items, start=1):
        title = item.find("title").text.strip() if item.find("title") else "No Title"
        link = item.find("link").text.strip() if item.find("link") else "No Link"
        pub_date = item.find("pubDate").text.strip() if item.find("pubDate") else "No Date"

        f.write(f"{i}. {title}\n {pub_date}\n {link}\n\n")

print(f"Hedlines saved successfully to '{filename}'")