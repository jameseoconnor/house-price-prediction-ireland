import time
import random
from selenium import webdriver
driver = webdriver.Chrome('/Applications/chromedriver')

def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html.encode())

offset = 0;
throttle = 780;

while offset<throttle:   
    url = 'https://www.daft.ie/wexford/houses-for-sale/'
    if offset>=20: 
        url = url + f'?offset={offset}'
    driver.get(url)
    html = driver.page_source
    save_html(html, f'./data/offest_{offset}.html')
    offset+=20;
    time.sleep(random.randint(5,10));
