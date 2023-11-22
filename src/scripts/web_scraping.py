import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Glassdoor():
    """
    Glassdoor is a web scraper for glassdoor.com. 
    
    It is used to scrape Interview Questions for non-technical roles for eaxample: HR, Marketing, Sales, etc.
    """

    # Start of Glassdoor class methods
    def __init__(self, credentials: dict, url: str):
        """
        You must have a Glassdoor account to use this scraper. 
        You must have signed up for an account with an email and password, not Google or Facebook.

        Provide credentials for Glassdoor in the following format:
        {
            "email": "email",
            "password": "password"
        }
        """

        # Create a new instance of Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.delay = 10

        # Load credentials
        self.email = credentials["email"]
        self.password = credentials["password"]

        # Load url
        self.url = url

    # Start of Glassdoor helper methods
    def get_driver(self):
        """
        Return the current driver.
        """
        return self.driver

    def close_driver(self):
        """
        Close the current driver.
        """
        self.driver.close()

    def maximize_window(self):
        """
        Maximize the current window.
        """
        self.driver.maximize_window()

    def take_me_to(self, url):
        """
        Take me to the given URL.
        """
        self.driver.get(url)

    def get_sleep(self, sleep_time):
        """
        Sleep for the given time.
        """
        time.sleep(sleep_time)

    # Start of Glassdoor login methods             
    def glassdoor_login_url(self):
        """
        Return the Glassdoor login URL.
        """
        return "https://www.glassdoor.com/index.htm"

    def enter_email(self):
        """
        Enter the email into the email field. Return True if successful, False otherwise.
        """
        try:
            # Find the email field
            email_field = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, \
                                                "input[id='inlineUserEmail']")))

            # Enter the email into the email field
            email_field.send_keys(self.email)

            print("Entered email.")

            return True

        except Exception as e:
            print("Error entering email.")
            print(e)
            return False

    def click_continue_with_email(self):
        """
        Click the "Continue with Email" button. Return True if successful, False otherwise.
        """
        try:

            # Find the "Continue with Email" button
            contine_with_email_button = WebDriverWait(self.driver, self.delay). \
                until(EC.element_to_be_clickable((By.CLASS_NAME, "emailButton")))

            # Click the "Continue with Email" button
            contine_with_email_button.click()

            print("Clicked continue with email button.")

            return True

        except TimeoutException:
            print("Timed out waiting for continue with email button.")
            return False
        except Exception as e:
            print("Error clicking continue with email button.")
            print(e)
            return False

    def enter_password(self):
        """
        Enter the password into the password field. Return True if successful, False otherwise.
        """
        try:
            # Find the password field
            password_field = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, \
                                                "input[id='inlineUserPassword']"))
            )

            # Enter the password into the password field
            password_field.send_keys(self.password)

            print("Entered password.")

            return True

        except Exception as e:
            print("Error entering password.")
            print(e)
            return False

    def getInnerHtml(self, element):
        """
        Return the inner HTML of the given element.
        """
        try:
            return element.get_attribute("innerHTML")
        except Exception as e:
            print("Error getting inner HTML.")
            print(e)
            return None

    def getTagName(self, element):
        """
        Return the tag name of the given element.
        """
        try:
            return element.tag_name
        except Exception as e:
            print("Error getting tag name.")
            print(e)
            return None

    def getInnerElements(self, element, tag_name):
        """
        Return the inner elements of the given element.
        """
        try:
            return element.find_elements(By.TAG_NAME, tag_name)
        except Exception as e:
            print("Error getting inner elements.")
            print(e)
            return None

    def click_sign_in(self):
        """
        Click the "Sign In" button. Return True if successful, False otherwise.
        """
        try:
            all_buttons = self.driver.find_elements(By.XPATH, "//button")
            sign_in_button = None

            for button in all_buttons:
                for span in self.getInnerElements(button, "span"):
                    if 'Sign In' in self.getInnerHtml(span):
                        sign_in_button = button

            WebDriverWait(self.driver, self.delay + 40).until(EC.element_to_be_clickable(sign_in_button))

            # Click the "Sign In" button
            sign_in_button.click()

            print("Clicked sign in button.")

            return True

        except TimeoutException:
            print("Timed out waiting for sign in button.")
            return False
        except Exception as e:
            print("Error clicking sign in button.")
            print(e)
            return False

    def login(self):
        """
        Login to Glassdoor using the provided credentials. Return True if successful, False otherwise.
        """
        try:
            # Go to the Glassdoor login page
            self.take_me_to(self.glassdoor_login_url())

            self.get_sleep(5)

            # Enter the email into the email field
            self.enter_email()

            self.get_sleep(5)

            # Click the "Continue with Email" button
            self.click_continue_with_email()

            self.get_sleep(5)

            # Enter the password into the password field
            self.enter_password()

            self.get_sleep(5)

            # Click the "Sign In" button
            self.click_sign_in()

            print("Successfully logged in.")

            self.get_sleep(10)

        except Exception as e:
            print("Error logging in.")
            print(e)

    # Start of Glassdoor interview questions helper methods
    def extract_job_role(self):
        start_idx = self.url.find('Interview') + len('Interview') + 1
        end_idx = self.url.find('interview')
        job_role = self.url[start_idx:end_idx].strip('-').replace('-', '_')
        return job_role

    def add_opening_square_bracket(self, fileWriter):
        fileWriter.write('[')

    def add_closing_square_bracket(self, fileWriter):
        # write the clsoing bracket of the JSON array
        fileWriter.write(']')

    def remove_line_char(self, fileWriter):
        # Remove the extra comma and newline character
        fileWriter.seek(0, 2)  # seek to end of file; f.seek(0, os.SEEK_END) is legal
        fileWriter.seek(fileWriter.tell() - 3,
                        0)  # seek to the second last char of file; f.seek(f.tell()-2, os.SEEK_SET) is legal
        fileWriter.truncate()

    # Start of Glassdoor interview questions scraping methods
    def click_next_button(self):
        # wait until the next button appears
        next_button = WebDriverWait(self.driver, self.delay).until \
            (EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Next"]')))

        # click the next button and wait
        self.driver.execute_script("arguments[0].click();", next_button)

    def get_interview_questions_from_a_page(self, fileWriter):

        interview_question_divs = self.driver.find_elements(by=By.CSS_SELECTOR,
                                                            value='[data-brandviews*="interviews-search-top-questions"]')

        for interview_question_div in interview_question_divs:
            interview_que, date, job_title, = "NA", "NA", "NA"

            try:  # try to get the job title
                job_title_txt = interview_question_div.find_element(by=By.CSS_SELECTOR,
                                                                    value='[class*="css-1entq9v edupdmz4"]')
                job_title = job_title_txt.text

            except NoSuchElementException as e:  # job title could not be found
                print('could not extract job title')

            try:  # try to get the interview question
                interview_que_txt = interview_question_div.find_element(by=By.CSS_SELECTOR,
                                                                        value='[class*="css-1jvs3tk edupdmz3"]')
                interview_que = interview_que_txt.text

            except NoSuchElementException as e:  # interview question could not be found
                print('could not extract interview question')

            try:  # try to get the interview date
                date_elements = interview_question_div.find_elements(by=By.CSS_SELECTOR,
                                                                     value='.css-pdd0hg.edupdmz5')

                if len(date_elements) >= 2:
                    # Get the text from the second element
                    date = date_elements[1].text

            except NoSuchElementException as e:  # interview date could not be found
                print('could not extract interview date')

            print(job_title, interview_que, date)

            # write a new row for interview question
            row_data = {"date": date, "job_title": job_title,
                        "interview_question": interview_que}

            json.dump(row_data, fileWriter, indent=1)
            fileWriter.write(',\n')

    def get_interview_questions_from_all_pages(self, file_path='data/raw_data/'):
        """
        This function takes to next page till available.

        """
        job_role = self.extract_job_role()

        # create a new josn writer for the interview posts
        fw = open(f'{file_path}{job_role}_interview_questions.json', 'w')

        # write the opening bracket of the JSON array
        self.add_opening_square_bracket(fw)

        print('Now, Going to the given url.. \n')

        # visit the interview page
        self.take_me_to(self.url)

        # keep track of page count
        page_cnt = 1

        print('Scraping information.....')

        while page_cnt <= 1:  # keep going until there are no more pages

            print('page', page_cnt)  # print current page count

            flag = True  # setting flag for refresh

            # extract and write the interview posts from the current page
            self.get_interview_questions_from_a_page(fw)

            try:
                self.click_next_button()  # Click on next button
                self.get_sleep(self.delay)  # wait for sec

            except TimeoutException as e:

                if flag:
                    print(f'Refreshing Page: {page_cnt}')
                    self.driver.refresh()  # Refreshing current page
                    self.get_sleep(20)  # try after some secs
                    flag = False

                    try:
                        self.click_next_button()  # click on next button after refresh
                        self.get_sleep(self.delay)  # wait for sec

                    except TimeoutException as e:

                        print("No more pages.")

                        self.remove_line_char(fw)
                        self.add_closing_square_bracket(fw)

                        break

            page_cnt += 1  # increment

        fw.close()
