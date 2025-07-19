# 📰 News Scraper using BeautifulSoup

This project is a simple **Python-based web scraper** that extracts headlines from an RSS feed using the **requests** and **BeautifulSoup** libraries. The scraped headlines are stored in a text file called `headlines.txt`.


## 📌 Project Objective

The goal of this project is to demonstrate basic web scraping techniques using BeautifulSoup and handle HTTP requests responsibly while writing the scraped data to a local file. It also aims to highlight how HTTP status codes and user-agents can impact scraping permissions.


## 🛠 Technologies Used

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)


## 📁 File Structure

Task 3/
│
├── news_scraper.py # Main script for scraping headlines
├── headlines.txt # Output file containing extracted headlines
├── README.md # Project documentation


## ✨ Features
  Sends an HTTP GET request to the specified URL.
  Parses the RSS feed using BeautifulSoup.
  Extracts and cleans up headline titles.
  Saves all headlines to a file (headlines.txt) in UTF-8 format.
  Includes User-Agent headers to bypass access denial.
  Handles errors like 403 and 401 responses gracefully.
  Uses proper exception handling (try-except) to prevent crashes.

## 🧠 What You Learn
  Basics of web scraping and RSS feed parsing
  Using HTTP headers (like User-Agent) to avoid scraping blocks
  Handling different HTTP status codes
  File I/O in Python
  Error handling with try-except blocks

## 👨‍💻 Author
  Asmi Dagar — Python Developer Intern at BroskiesHub
