import re
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# Set up the Chrome driver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def daraz(url):
    # Create Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Create the driver with the options
    driver = webdriver.Chrome(options=chrome_options)

    # Load the page with Selenium
    driver.get(url)

    # Wait up to 10 seconds for the page to load
    # Wait for the page to finish loading all JavaScript
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//body[not(@class='loading')]")))

    # Get the HTML of the page and pass it to BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Use a regular expression to match classes that have a similar pattern
    pattern = re.compile(r'gridItem--\w+')

    # Find all tags that have classes matching the pattern
    matching_tags = soup.find_all(class_=pattern)

    driver.close()

    # Append the matching classes to a list
    matching_classes = []
    for tag in matching_tags:
        for class_name in tag['class']:
            if pattern.match(class_name):
                matching_class = str(tag)
                matching_classes.append(matching_class)

    # Extract the price for each class content
    prices = []
    names = []
    img_links = []
    for class_content in matching_classes:
        soup = BeautifulSoup(class_content, 'html.parser')
        price_tag = soup.find(class_=re.compile('currency--\w+'))
        if price_tag:
            price = price_tag.text.strip()
            prices.append(price)
        else:
            prices.append(None)

        image = soup.find(class_=re.compile('image--\w+'))
        if image:
            image_link = image['src']
            alt_text = image['alt']
            names.append(alt_text)
            img_links.append(image_link)
        else:
            names.append(None)
            img_links.append(None)

    x = "https://icms-image.slatic.net/images/ims-web/217b267f-b12e-4693-9d1d-7a77d2265b91.png"
    df = pd.DataFrame(
        {'Site': '<img src="' + x + '" width="60" >', 'Product Name': names, 'Price': prices, 'Image Link': img_links})
    return df.iloc[[0]]


def kapruka(url):
    # Create Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Create the driver with the options
    driver = webdriver.Chrome(options=chrome_options)

    # Load the page with Selenium
    driver.get(url)

    # Wait up to 10 seconds for the page to load
    # Wait for the page to finish loading all JavaScript
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//body[not(@class='loading')]")))

    # Get the HTML of the page and pass it to BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Use a regular expression to match classes that have a similar pattern
    pattern = re.compile(r'catalogueV2Repeater')

    # Find all tags that have classes matching the pattern
    matching_tags = soup.find_all(class_='catalogueV2Repeater')

    driver.close()

    # Append the matching classes to a list
    matching_classes = []
    for tag in matching_tags:
        for class_name in tag['class']:
            if pattern.match(class_name):
                matching_class = str(tag)
                matching_classes.append(matching_class)

    # Extract the price for each class content
    prices = []
    names = []
    img_links = []
    for class_content in matching_classes:
        soup = BeautifulSoup(class_content, 'html.parser')
        price_tag = soup.find(class_='catalogueV2Local')
        if price_tag:
            price = price_tag.text.strip()
            prices.append(price)
        else:
            prices.append(None)

        image = soup.find(class_='CatalogueV2ImageWrapper')
        if image:
            # Use regular expression to extract the src attribute value
            match = re.search(r'src="([^"]+)"', str(image))
            if match:
                image_link = match.group(1)
            else:
                image_link = None

            # Use regular expression to extract the alt attribute value
            match = re.search(r'alt="([^"]+)"', str(image))
            if match:
                alt_text = match.group(1)
            else:
                alt_text = None

            names.append(alt_text)
            img_links.append("https://www.kapruka.com" + image_link)

    x = "https://www.kapruka.com/images/kapruka_logo_square.png"
    df = pd.DataFrame(
        {'Site': '<img src="' + x + '" width="60" >', 'Product Name': names, 'Price': prices, 'Image Link': img_links})
    return df.iloc[[0]]


def wasi(url):
    # Create Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Create the driver with the options
    driver = webdriver.Chrome(options=chrome_options)

    # Load the page with Selenium
    driver.get(url)

    # Wait up to 10 seconds for the page to load
    # Wait for the page to finish loading all JavaScript
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//body[not(@class='loading')]")))

    # Get the HTML of the page and pass it to BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Use a regular expression to match classes that have a similar pattern
    pattern = re.compile(r'product-inner')

    # Find all tags that have classes matching the pattern
    matching_tags = soup.find_all(class_='product-inner')

    driver.close()

    # Append the matching classes to a list
    matching_classes = []
    for tag in matching_tags:
        for class_name in tag['class']:
            if pattern.match(class_name):
                matching_class = str(tag)
                matching_classes.append(matching_class)

    # Extract the price for each class content
    prices = []
    names = []
    img_links = []
    for class_content in matching_classes:
        soup = BeautifulSoup(class_content, 'html.parser')
        price_tag = soup.find(class_='woocommerce-Price-amount amount')
        if price_tag:
            # Use regular expression to extract the number
            match = re.search(r'[0-9,]+(?:\.[0-9]+)?', str(price_tag))
            if match:
                price = match.group()
                prices.append("Rs " + price)
            else:
                prices.append(None)

        image = soup.find(class_='mf-product-thumbnail')
        if image:
            # Use regular expression to extract the src attribute value
            match = re.search(r'src="([^"]+)"', str(image))
            if match:
                image_link = match.group(1)
                print(image_link)
            else:
                image_link = None

            # Use regular expression to extract the alt attribute value
            match = re.search(r'alt="([^"]+)"', str(image))
            if match:
                alt_text = match.group(1)
            else:
                alt_text = None

            names.append(alt_text)
            img_links.append(image_link)

    x = "https://www.wasi.lk/wp-content/uploads/2019/11/wasilk-header-logo-250x66.png"
    df = pd.DataFrame(
        {'Site': '<img src="' + x + '" width="60" >', 'Product Name': names, 'Price': prices, 'Image Link': img_links})
    return df.iloc[[0]]
