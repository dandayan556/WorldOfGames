from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to the URL of the application
driver.get("http://www.example.com")

# Find the search box element and enter a search term
search_box = driver.find_element_by_name("q")
search_box.send_keys("Python")
search_box.send_keys(Keys.RETURN)

# Verify that the search results page is displayed
assert "Google" in driver.title

# Close the browser window
driver.close()