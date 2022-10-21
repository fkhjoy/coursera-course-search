import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

baseUrl = "https://www.coursera.org/"

def get_course_info(url_):
    url_ = baseUrl + url_
    page = requests.get(url_)
    soup = BeautifulSoup(page.text, 'html.parser')
    star = soup.find('span', attrs={"data-test": "number-star-rating"}).text.replace("stars", "")
    students = soup.find('div', attrs={"class": "_1fpiay2"}).text.replace(" already enrolled","") 
    title = soup.find('h1', attrs={"data-e2e": "xdp-banner-title"}).text
    description = soup.find('div', attrs={"data-e2e":"description"}).text
    url_ += "#instructors"
    page = requests.get(url_)
    soup = BeautifulSoup(page.text, 'html.parser')
    instructor = soup.find('h3', attrs={"class": "instructor-name headline-3-text bold"}).text
    provider = soup.find('h3', attrs={"class": "headline-4-text bold rc-Partner__title"}).text
    return title, description, star, instructor, provider, students

for x in range(1, 3):
    url = f"https://www.coursera.org/search?query=data%20science&page={x}&index=prod_all_launched_products_term_optimization_skills_test_for_precise_xdp_variant"
    
    options = Options()
    # options.add_argument("--headless")
    # initiating the webdriver. Parameter includes the path of the webdriver.
    driver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver') 
    driver.get(url) 
    
    # this is just to ensure that the page is loaded
    time.sleep(2) 
    
    html = driver.page_source  
    # this renders the JS code and stores all
    # of the information in static HTML code.
    
    # Now, we could simply apply bs4 to html variable
    soup = BeautifulSoup(html, "html.parser")
    all_divs = soup.find_all('a', {"data-click-key": "search.search.click.search_card"})

    for div in all_divs:
        print(div.get("href"))

driver.close()



'''
https://www.coursera.org/search?query=data%20science&page=2&index=prod_all_launched_products_term_optimization_skills_test_for_precise_xdp_variant
https://www.coursera.org/search?query=data%20science&page=3&index=prod_all_launched_products_term_optimization_skills_test_for_precise_xdp_variant
'''