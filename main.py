from src.scripts.web_scraping import Glassdoor

# You must have a Glassdoor account to use this scraper.
# You must have signed up for an account with an email and password, not Google or Facebook.
# Provide credentials for Glassdoor in the following format:
credentials = {
    "email": "chetan.jain.extras@proton.me",
    "password": "Test@123"
}

url = "https://www.glassdoor.com/Interview/hr-interview-questions-SRCH_KO0,2_SDMC_IP2.htm"

if __name__ == "__main__":
        
    # Create a new instance of Glassdoor
    gd = Glassdoor(credentials, url)

    # Login to Glassdoor
    gd.login()

    # Extract all interview questions available for specified role
    gd.get_interview_questions_from_all_pages()

    # Close the current window
    gd.close_driver()
