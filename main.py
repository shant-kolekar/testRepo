from src.scripts.web_scraping import Glassdoor

# You must have a Glassdoor account to use this scraper.
# You must have signed up for an account with an email and password, not Google or Facebook.
# Provide credentials for Glassdoor in the following format:
credentials = {
    "email": "degaha8017@nexxterp.com",
    "password": "Test@123"
}

HR_url = "https://www.glassdoor.com/Interview/hr-interview-questions-SRCH_KO0,2_SDMC_IP2.htm"
cust_support_url = "https://www.glassdoor.com/Interview/customer-support-interview-questions-SRCH_KO0,16.htm"

business_dev_manager_url = "https://www.glassdoor.com/Interview/business-development-manager-interview-questions-SRCH_KO0,29.htm"
sales_manager_url = "https://www.glassdoor.com/Interview/sales-manager-interview-questions-SRCH_KO0,13_SDMC.htm"
account_exec_url = "https://www.glassdoor.com/Interview/account-executive-interview-questions-SRCH_KO0,17.htm"
account_manager_url = "https://www.glassdoor.com/Interview/account-manager-interview-questions-SRCH_KO0,15.htm"


if __name__ == "__main__":
        
    # Create a new instance of Glassdoor
    gd = Glassdoor(credentials, HR_url)

    # Login to Glassdoor
    gd.login()

    # Extract all interview questions available for specified role
    gd.get_interview_questions_from_all_pages()

    # Close the current window
    gd.close_driver()
