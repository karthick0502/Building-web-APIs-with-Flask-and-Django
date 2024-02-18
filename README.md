# News Scraper Using Flask and Django

This project is a Flask-based web application designed to scrape news from two different websites and display the collected information on a single webpage. 
It provides a convenient way to browse through headlines, images, and summaries of news articles from the BBC and Times of India websites.

## Features
- Scrapes news articles from BBC and Times of India websites.
- Displays headlines, images, and summaries of news articles.
- Allows users to navigate between BBC and Times of India news sections.
- Provides direct links to the official websites for full article reading.

## Technologies Used
- **Flask**: Used as the web framework for building the API and serving web pages.
- **Beautiful Soup**: A Python library for web scraping, utilized to extract news information from HTML content.
- **Requests**: A Python HTTP library used to fetch web pages and handle HTTP requests/responses.
- **Pandas**: A data manipulation and analysis library, employed to organize scraped data into structured formats.

## Usage
1. Clone the repository to your local machine.
2. Install the required dependencies listed in `requirements.txt`.
3. Run the `main.py` file to start the Flask web server.
4. Navigate to `http://localhost:5000` in your web browser to view the news webpage.
5. Explore the latest news articles from the BBC and Times of India.

## Project Structure
- **main.py**: Flask application script containing routes and server setup.
- **scrap.py**: Python module for scraping news articles from BBC and Times of India websites.
- **forms.py**: Module defining Flask-WTF forms for user registration and login (not implemented in this version).
- **templates/**: Folder containing HTML templates for rendering web pages.
- **static/**: Folder containing static files such as CSS stylesheets.

## Django Implementation

Additionally, this repository includes a zip file containing the Django implementation of the News Scraper project. The Django version offers an alternative approach to the original Flask implementation, providing users with a choice of web frameworks to explore.

