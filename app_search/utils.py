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

baseUrl = "https://www.coursera.org"

def get_course_info(url_):

    url = baseUrl + url_
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    n_count = 0
    try:
        star = soup.find('span', attrs={"data-test": "number-star-rating"}).text.replace("stars", "")
    except:
        n_count += 1
        star = "N/A" 
    try:
        students = soup.find('div', attrs={"class": "_1fpiay2"}).text.replace(" already enrolled","") 
    except:
        n_count += 1
        students = "N/A"
    try:
        title = soup.find('h1', attrs={"data-e2e": "xdp-banner-title"}).text
    except:
        n_count += 1
        title = "N/A"
    try:
        description = soup.find('div', attrs={"data-e2e":"description"}).text
    except:
        try:
            description = soup.find('div', attrs={"class":"content-inner"}).text
        except:
            n_count += 1
            description = "N/A"
    url += "#instructors"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    try:
        instructor = soup.find('h3', attrs={"class": "instructor-name headline-3-text bold"}).text.replace("Top Instructor", "")
    except:
        n_count += 1
        instructor = "N/A"
    try:
        provider = soup.find('h3', attrs={"class": "headline-4-text bold rc-Partner__title"}).text
    except:
        n_count += 1
        provider = "N/A"
    if n_count > 3:
        return None 
    return title, description, star, instructor, provider, students, baseUrl + url_

def get_course_info_by_page(page_no, course, visited_page):

    options = Options()
    options.add_argument("--headless")
    # initiating the webdriver. Parameter includes the path of the webdriver.
    driver = webdriver.Chrome(chrome_options=options, executable_path='/home/fkj/Devs/coursera-scrape/app_search/chromedriver')

    course = "%20".join(course.split())
    course_details = []
    url = f"https://www.coursera.org/search?query={course}&"
    # if page > 1:
    #     url += f"page={page}&index=prod_all_launched_products_term_optimization"
    print(url)
    
    driver.get(url)
    for page in range(1, page_no+1):
         
        
        # this is just to ensure that the page is loaded
        time.sleep(3) 
        
        html = driver.page_source  
        # this renders the JS code and stores all
        # of the information in static HTML code.
        
        # Now, we could simply apply bs4 to html variable
        soup = BeautifulSoup(html, "html.parser")
        all_divs = soup.find_all('a', {"data-click-key": "search.search.click.search_card"})

        
        for div in all_divs:
            url = div.get("href")
            if url in visited_page:
                continue 
            visited_page[url] = True
            details = get_course_info(url)
            
            if details:
                # print(url)
                course_details.append(details)
        WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-e2e='pagination-controls-next']"))).click()

    driver.close()

    return course_details