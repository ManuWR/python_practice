import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
    # Open the Wikipedia homepage
    driver.get("https://www.wikipedia.org/")
    # Locate the search input field by its name attribute and enter a search term
    search_input = driver.find_element(By.NAME, 'search')
    search_input.send_keys('Selenium (software)')
    # Submit the search form
    search_input.send_keys(Keys.RETURN)
    # Wait for the results page to load and display the results
    time.sleep(2)
    # Click on the first search result link
    first_result = driver.find_element(
        By.CSS_SELECTOR, 'ul.mw-search-results li a')
    first_result.click()
    # Optional: Wait for a few seconds to ensure the page loads completely
    time.sleep(5)
    # Print the title of the current page
    print("Page title after click:", driver.title)
finally:
    # Close the browser
    driver.quit()
