import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
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

def fetch_sidebar_links(driver, sidebar_url):
    print(f'Fetching sidebar links from: {sidebar_url}')
    driver.get(sidebar_url)
    
    # Wait for the JavaScript to load and render the sidebar content
    time.sleep(5)  # Adjust this sleep time if necessary

    # Extract the page source after JavaScript has rendered the content
    page_source = driver.page_source
    
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Print out the structure of the sidebar container for debugging
    sidebar_container = soup.find('div', class_='sidenav-container')
    if sidebar_container:
        print('Found the sidebar container. Here is its structure:')
        print(sidebar_container.prettify())
    else:
        print('Sidebar container not found.')
        return []

    # Adjust this selector to match the sidebar links in your documentation site
    sidebar_links = sidebar_container.select('ul.sidenav a')
    
    if not sidebar_links:
        print('No sidebar links found. Check the CSS selector.')
        return []

    links = []
    for link in sidebar_links:
        href = link.get('href')
        if href:
            # Use urljoin to correctly resolve relative URLs
            href = urljoin(sidebar_url, href)
            links.append(href)
    
    print(f'Found {len(links)} sidebar links.')
    return links

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

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def expand_sidebar_item(driver, item):
    try:
        toggle_button = item.find_element(By.XPATH, './/span[contains(@class, "submenu-toggle-container")]')
        toggle_button.click()
        time.sleep(2)  # Wait for the expansion
        return True
    except (NoSuchElementException, ElementClickInterceptedException):
        print(f'No expandable button found for: {item.text}')
        return False

def process_sidebar_item(driver, link, content_div_id, depth=0):
    driver.get(link)
    time.sleep(5)  # Wait for the page to load

    # Fetch and save the article content
    content = fetch_article_content(link, content_div_id)
    if content:
        Path(f'articles/depth_{depth}').mkdir(parents=True, exist_ok=True)
        filename = sanitize_filename(f'articles/depth_{depth}/article_{os.path.basename(link)}.html')
        save_content_to_html(content, filename)
    else:
        print(f'No content to save for: {link}')

    # Find and expand the current sidebar item
    try:
        sidebar_container = driver.find_element(By.CLASS_NAME, 'sidenav-container')
        current_item = sidebar_container.find_element(By.CSS_SELECTOR, f'a[href="{link}"]')
        if expand_sidebar_item(driver, current_item):
            # Debug: Print the current expanded sidebar container structure
            print('Expanded sidebar container structure:')
            print(sidebar_container.get_attribute('innerHTML'))

            # Get all sub-items and process them recursively
            sub_items = current_item.find_elements(By.XPATH, '../ul[@class="vertical menu accordion-menu is-accordion-submenu nested"]/li/a')
            for sub_item in sub_items:
                sub_link = sub_item.get_attribute('href')
                print(f'Found sub-item link: {sub_link}')
                process_sidebar_item(driver, sub_link, content_div_id, depth + 1)
    except NoSuchElementException:
        print(f'No sub-items found for: {link}')

def main():
    base_url = 'https://docs.brevis.one/current/en/Content/Home.htm'
    sidebar_url = 'https://docs.brevis.one/current/en/Content/Home.htm'
    content_div_id = 'mc-main-content'
    
    driver = setup_webdriver()
    links = fetch_sidebar_links(driver, sidebar_url)
    
    if not links:
        print('No links to process.')
        return
    
    os.makedirs('articles', exist_ok=True)
    
    for link in links:
        process_sidebar_item(driver, link, content_div_id)

    driver.quit()

if __name__ == '__main__':
    main()
