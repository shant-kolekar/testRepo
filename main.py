from src.scripts.web_scraping import Glassdoor

# Credentials for Glassdoor
credentials = {
    "email": "chetan.jain.extras@proton.me",
    "password": "Test@123"
}


if __name__ == "__main__":
        
    # Create a new instance of Glassdoor
    gd = Glassdoor(credentials)

    # Login to Glassdoor
    gd.login()

    # Close the current window
    gd.close_driver()
