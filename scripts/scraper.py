import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urljoin
from pathlib import Path
import re

def setup_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headless Chrome
    driver = webdriver.Chrome(options=options)
    return driver

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def fetch_article_content(url, content_div_id):
    print(f'Fetching content from: {url}')
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f'Failed to retrieve article content. Status code: {response.status_code}')
        return ''
    
    soup = BeautifulSoup(response.content, 'html.parser')
    content_div = soup.find(id=content_div_id)
    
    if content_div:
        print(f'Found content in div with ID: {content_div_id}')
    else:
        print(f'No content found in div with ID: {content_div_id}')
    
    return str(content_div) if content_div else ''

def save_content_to_html(content, filename):
    print(f'Saving content to: {filename}')
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def process_li(driver, li_xpath, content_div_id, depth):
    try:
        link = driver.find_element(By.XPATH, li_xpath + '/a')
        href = link.get_attribute('href')
        
        # Navigate to the link and fetch the content
        driver.get(href)
        time.sleep(2)  # Wait for the page to load
        content = fetch_article_content(href, content_div_id)
        
        if content:
            Path(f'articles/depth_{depth}').mkdir(parents=True, exist_ok=True)
            filename = sanitize_filename(f'articles/depth_{depth}/article_{os.path.basename(href)}.html')
            save_content_to_html(content, filename)
        
        # Check for sub-items
        sub_uls = driver.find_elements(By.XPATH, li_xpath + '/ul')
        for index, sub_ul in enumerate(sub_uls):
            sub_ul_xpath = f'{li_xpath}/ul[{index + 1}]'
            process_ul(driver, sub_ul_xpath, content_div_id, depth + 1)
    except NoSuchElementException:
        print('No link found in this list item.')
    except StaleElementReferenceException:
        print('Encountered a stale element reference. Retrying...')
        time.sleep(1)  # Wait a bit before retrying
        process_li(driver, li_xpath, content_div_id, depth)

def process_ul(driver, ul_xpath, content_div_id, depth):
    try:
        lis = driver.find_elements(By.XPATH, ul_xpath + '/li')
        for index, li in enumerate(lis):
            li_xpath = f'{ul_xpath}/li[{index + 1}]'
            process_li(driver, li_xpath, content_div_id, depth)
    except StaleElementReferenceException:
        print('Encountered a stale element reference while processing UL. Retrying...')
        time.sleep(1)  # Wait a bit before retrying
        process_ul(driver, ul_xpath, content_div_id, depth)

def main():
    base_url = 'https://docs.brevis.one/current/en/Content/Home.htm'
    content_div_id = 'mc-main-content'
    
    driver = setup_webdriver()
    driver.get(base_url)
    time.sleep(5)  # Wait for the page to load
    
    try:
        # Get the first UL in the sidebar and start processing
        sidebar_container = driver.find_element(By.CLASS_NAME, 'sidenav-container')
        first_ul_xpath = "//div[@class='sidenav-container']/ul"
        process_ul(driver, first_ul_xpath, content_div_id, 0)
    except NoSuchElementException as e:
        print(f'Error: {e}')
    
    driver.quit()

if __name__ == '__main__':
    main()
