# Glassdoor Interview Questions Scraper

This is a web scraper that automates the collection of interview questions for various non-technical roles from Glassdoor.

## Prerequisites

Before you run the script, ensure the following:

- Python 3.8 or higher is installed on your system.
- The latest version of Google Chrome is installed. This is necessary because the `webdriver-manager` used in the script relies on ChromeDriver.


## Installation

Clone the repository to your local machine, navigate to the project directory in your terminal, and run the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

## Customizing the Script

To collect interview questions for a specific job role, modify the `main.py` script. Look for the following line in main.py:

```python
gd = Glassdoor(credentials, HR_url)
```

Replace HR_url with the variable that holds your desired URL of specific role.


## Running the Script

After configuring the script with desired URL, run the script using:

```bash
python main.py
```

##### The script will perform the following actions:

* Log in to Glassdoor using the provided credentials.
* Navigate to the specified URL.
* Scrape the interview questions.
* Close the browser window upon completion