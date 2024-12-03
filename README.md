# My-First Redbus-project
Redbus Data Scrapping with selenium &amp; My SQL Database &amp; Dynamic Filtering using stream lit
My-First Redbus Project
This project demonstrates how to scrape bus data from Redbus, store it in a MySQL database, and provide dynamic filtering options using Streamlit. The goal of the project is to allow users to interact with bus data, filter it based on their preferences (such as source and destination), and view the results in a user-friendly interface.

Project Overview
Key Features:
Web Scraping: Scrape bus details (such as bus names, prices, departure/arrival times, etc.) from the Redbus website using Selenium.
MySQL Database: Store the scraped data in a MySQL database for efficient querying and management.
Streamlit Interface: Create an interactive dashboard where users can filter bus data based on their criteria (source, destination, price, etc.).
Technologies Used
Selenium: For web scraping dynamic content from Redbus.
MySQL: To store the bus information in a relational database.
Streamlit: For building a dynamic, interactive web app for filtering and displaying bus data.
Python: Programming language for implementing the entire workflow.
BeautifulSoup (Optional): For parsing HTML if needed (alternative to Selenium's built-in methods).
Installation
Prerequisites
Python 3.x
MySQL Server installed and running
WebDriver for Selenium (e.g., ChromeDriver)
Steps to Set Up the Project
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/My-First-Redbus-Project.git
cd My-First-Redbus-Project
Install required Python libraries:

bash
Copy code
pip install selenium mysql-connector-python streamlit beautifulsoup4
Download and set up WebDriver:

Download the appropriate WebDriver (e.g., ChromeDriver) from here.
Make sure the WebDriver is in your system's PATH or specify the path in the Selenium code.

Project Structure
graphql
Copy code
My-First-Redbus-Project/
│
├── scrape_redbus.py         # Python script to scrape data using Selenium
├── app.py                   # Streamlit app for dynamic filtering
├── requirements.txt         # List of Python dependencies
├── README.md                # Project documentation
└── database_config.py       # (Optional) Store MySQL credentials and config
Usage
Web Scraping:

The scrape_redbus.py script will launch the browser, navigate to the Redbus website, and scrape the bus data for a given search query.
The data is then inserted into the MySQL database for further querying.
Streamlit Interface:

Open the Streamlit app at http://localhost:8501.
Use the dropdown menus to select your source and destination, then click the Show Buses button to see the filtered results.
Filtering Options:

Users can filter bus information by source and destination, and view details such as departure time, price, and bus names.
