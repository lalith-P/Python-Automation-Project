from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the Selenium webdriver (in this case, using Chrome)
driver = webdriver.Chrome()

# Navigate to the career website
driver.get("https://www.example.com/careers")

# Find and interact with the necessary web elements (customize based on the website's structure)
# Personal Details
first_name_input = driver.find_element_by_id("first_name")
middle_name_input = driver.find_element_by_id("middle_name")
last_name_input = driver.find_element_by_id("last_name")
local_first_name_input = driver.find_element_by_id("local_first_name")
local_last_name_input = driver.find_element_by_id("local_last_name")
preferred_name_input = driver.find_element_by_id("preferred_name")

# Fill out Personal Details
first_name_input.send_keys("Lalith")
middle_name_input.send_keys("P")
last_name_input.send_keys("")
local_first_name_input.send_keys("")
local_last_name_input.send_keys("")
preferred_name_input.send_keys("Lalith")

# Address
street_name_input = driver.find_element_by_id("street_name")
street_name2_input = driver.find_element_by_id("street_name2")
city_input = driver.find_element_by_id("city")
state_input = driver.find_element_by_id("state")
pin_code_input = driver.find_element_by_id("pin_code")

# Fill out Address
street_name_input.send_keys("123 Main Street")
street_name2_input.send_keys("Apt 4B")
city_input.send_keys("New York")
state_input.send_keys("NY")
pin_code_input.send_keys("12345")

# Education
college_input = driver.find_element_by_id("college")
field_of_study_input = driver.find_element_by_id("field_of_study")
cgpa_input = driver.find_element_by_id("cgpa")
year_of_completion_input = driver.find_element_by_id("year_of_completion")

# Fill out Education
college_input.send_keys("XYZ College")
field_of_study_input.send_keys("Computer Science")
cgpa_input.send_keys("8.5")
year_of_completion_input.send_keys("2022")

# Work Experience
company_input = driver.find_element_by_id("company")
job_title_input = driver.find_element_by_id("job_title")
currently_working_checkbox = driver.find_element_by_id("currently_working")
years_worked_input = driver.find_element_by_id("years_worked")

# Fill out Work Experience
company_input.send_keys("ABC Company")
job_title_input.send_keys("Software Developer")
currently_working_checkbox.click()
years_worked_input.send_keys("2")

# Current and Expected CTC
current_ctc_input = driver.find_element_by_id("current_ctc")
expected_ctc_input = driver.find_element_by_id("expected_ctc")

# Fill out Current and Expected CTC
current_ctc_input.send_keys("x LPA")
expected_ctc_input.send_keys("x LPA")

# File Attachments
resume_upload = driver.find_element_by_id("resume")
additional_attachments_upload = driver.find_element_by_id("additional_attachments")

# Upload files for File Attachments
resume_upload.send_keys("/path/to/resume.pdf")
additional_attachments_upload.send_keys("/path/to/additional_attachments.zip")

# Websites and LinkedIn Profile
portfolio_website_input = driver.find_element_by_id("portfolio_website")
github_link_input = driver.find_element_by_id("github_link")
leetcode_link_input = driver.find_element_by_id("leetcode_link")
linkedin_profile_input = driver.find_element_by_id("linkedin_profile")

# Fill out Websites and LinkedIn Profile
portfolio_website_input.send_keys("https://www.example.com/portfolio")
github_link_input.send_keys("https://github.com/yourusername")
leetcode_link_input.send_keys("https://leetcode.com/yourusername")
linkedin_profile_input.send_keys("https://www.linkedin.com/in/yourprofile")

# Self Voluntary Enclosure
gender = driver.find_element_by_id("male")

# Select the appropriate gender
gender.click()

# Agree to Terms and Conditions
terms_conditions_checkbox = driver.find_element_by_id("terms & conditions")

# Agree to the terms and conditions
terms_conditions_checkbox.click()

# Submit the job application
submit_button = driver.find_element_by_id("submit")
submit_button.click()

# Close the browser
driver.quit()
