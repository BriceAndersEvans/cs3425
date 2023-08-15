# Webscraper for the climbing shoes of https://www.backcountry.com This scraper is intended for the use of collecting
# attributes of climbing shoes from https://www.backcountry.com in an attempt to make inferences, regarding shoe
# costs and brand quality
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

# Open the climbing shoes search page
url = "https://www.backcountry.com/search?q=climbing%20shoes&s=u"
driver.get(url)

# Initialize the lists for collecting climbing shoe search pages (webpage_links) & individual shoe pages (product_links)
webpage_links = []
product_links = []

# Scrape first page of climbing shoes for link of each individual shoe
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

# Loop through webpage_links and scrape the links of each individual shoe page (product_links)
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


# Create BackcountryClimbing-Shoes.csv file
# & scrape each product_link page for desired attributes and store scraped information in csv file
with open('../Modeling/BackcountryClimbing-Shoes.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Shoe_Link', 'Shoe_Brand', 'Shoe_Name', 'Shoe_Price', 'Shoe_Color'])
    for link in product_links:
        options = Options()
        # Run webdriver in headless mode
        options.add_argument("--headless")
        driver = webdriver.Chrome('/home/anders/College/Spring2023/drivers/chromedriver', options=options)
        driver.get(link)

        # Extract the attributes of each shoe page
        # Extract Shoe_Link
        try:
            shoe_link = driver.current_url
        except:
            shoe_link = "N/A"

        # Extract Shoe Brand
        try:
            div_element = driver.find_element_by_xpath("//div[contains(@class, 'css-ryjapq')]")
            a_element = div_element.find_element_by_xpath(".//a[contains(@class, 'chakra-link')]")
            shoe_brand = a_element.text
        except:
            shoe_brand = "N/A"

        # Extract Shoe Name
        try:
            span_element = driver.find_element_by_xpath(
                "//span[@class='chakra-text css-1oyyk97' and @data-id='productTitle']")
            shoe_name = span_element.text
        except:
            shoe_name = "N/A"

        # Extract Shoe Price
        try:
            span_element = driver.find_element_by_xpath("//span[@class='chakra-text css-1sxaem' and @data-id='pricing']")
            text = span_element.text
            match = re.search(r'\d+\.\d+', text)
            if match:
                shoe_price = match.group()
        except:
            shoe_price = "N/A"

        # Extract Shoe Color
        try:
            span_element = driver.find_element_by_class_name("css-pn2vcv")
            shoe_color = span_element.text
        except:
            shoe_color = "N/A"

        if "chains" in shoe_name.lower() or "boot" in shoe_name.lower() \
                and "shoe" not in shoe_name.lower():
            # Skip writing to the CSV file
            pass
        else:
            print(shoe_link)
            print(shoe_brand)
            print(shoe_name)
            print(shoe_price)
            print(shoe_color)
            writer.writerow([shoe_link, shoe_brand, shoe_name, shoe_price, shoe_color])
        # Close the webdriver for the current product_link
        driver.quit()


