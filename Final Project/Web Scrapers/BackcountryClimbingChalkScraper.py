# Webscraper for the climbing chalk of https://www.backcountry.com This scraper is intended for the use of
# collecting attributes of climbing chalk from https://www.backcountry.com in an attempt to make inferences,
# regarding chalk costs and brand quality
# Anders Evans - (4-27-2023)

# Imports
import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create webdriver options
options = Options()
options.add_argument("--headless")

# New instance of webdriver
driver = webdriver.Chrome('/home/anders/College/Spring2023/drivers/chromedriver')

# Ethical Check & Protocol for webdriver
driver.get('https://www.backcountry.com/robots.txt')
time.sleep(2)

# Open the climbing chalk search page
url = "https://www.backcountry.com/search?q=climbing%20chalk&p=group_id%3Abc-climb&s=u"
driver.get(url)

# Initialize the lists for collecting climbing chalk search pages (webpage_links)
# & individual chalk pages (product_links)
webpage_links = []
product_links = []

# Scrape first page of climbing chalk for link of each individual chalk page
product_blocks = driver.find_elements_by_xpath("//div[@data-id='productListingItems']")
for block in product_blocks:
    link = block.find_element_by_xpath(".//a[@variant='text']").get_attribute('href')
    print(link)
    product_links.append(link)
print(product_links)

# Click the "Next Page" button and scrape for webpage_links from the original webpage
while True:
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-id='nextPage']")))
        next_button.click()
        webpage_links.append(driver.current_url)
        print("Clicked the Next Page button")
        print(webpage_links)

    except:
        print("No more pages to click")
        break
# Quit initial webdriver
driver.quit()

# Run webdriver in headless mode
options.add_argument("--headless")
driver = webdriver.Chrome('/home/anders/College/Spring2023/drivers/chromedriver')

# Loop through webpage_links and scrape the links of each individual chalk page (product_links)
for webpage in webpage_links:
    time.sleep(3)
    driver = webdriver.Chrome('/home/anders/College/Spring2023/drivers/chromedriver')
    driver.get(webpage)
    print(webpage)
    time.sleep(3)
    product_blocks = driver.find_elements_by_xpath("//div[@data-id='productListingItems']")
    for block in product_blocks:
        link = block.find_element_by_xpath(".//a[@variant='text']").get_attribute('href')
        print(link)
        product_links.append(link)
    print(product_links)
    driver.quit()

# Create BackcountryClimbing-Chalk.csv file
# & scrape each product_link page for desired attributes and store scraped information in csv file
with open('../Inferences/BackcountryClimbing-Chalk.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Chalk_Link', 'Chalk_Brand', 'Chalk_Name', 'Chalk_Price'])
    for link in product_links:
        options = Options()
        # Run webdriver in headless mode
        options.add_argument("--headless")
        driver = webdriver.Chrome('/home/anders/College/Spring2023/drivers/chromedriver', options=options)
        driver.get(link)

        # Extract the attributes of each chalk page
        # Extract chalk Link
        try:
            chalk_link = driver.current_url
        except:
            chalk_link = "N/A"

        # Extract Chalk Brand
        try:
            div_element = driver.find_element_by_xpath("//div[contains(@class, 'css-ryjapq')]")
            a_element = div_element.find_element_by_xpath(".//a[contains(@class, 'chakra-link')]")
            chalk_brand = a_element.text
        except:
            chalk_brand = "N/A"

        # Extract Chalk Name
        try:
            span_element = driver.find_element_by_xpath(
                "//span[@class='chakra-text css-1oyyk97' and @data-id='productTitle']")
            chalk_name = span_element.text
        except:
            chalk_name = "N/A"

        # Extract Chalk Price
        try:
            price_element = driver.find_element_by_css_selector("span[data-id='pricing']")
            price_text = price_element.text
            prices = price_text.split("$")
            current_price = prices[1]
            match = re.search(r'\d+\.\d+', current_price)
            chalk_price = match.group()
        except:
            chalk_price = "N/A"

        if "bag" in chalk_name.lower() or "bucket" in chalk_name.lower() or "harness" in chalk_name.lower() or "brush" in chalk_name.lower() or "pouch" in chalk_name.lower() or "file" in chalk_name.lower() or "tank" in chalk_name.lower() or "hoodie" in chalk_name.lower() or "kit" in chalk_name.lower() or "tape" in chalk_name.lower():
            # Skip writing to the CSV file
            pass
        else:
            print(chalk_link)
            print(chalk_brand)
            print(chalk_name)
            print(chalk_price)
            writer.writerow([chalk_link, chalk_brand, chalk_name, chalk_price])
        # Close the webdriver for the current product_link
        driver.quit()
