from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd 
import random 
import time
import re
import json


def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html.encode())


# function to add to JSON 
def write_json(data, filename='data.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 


def create_dict_from_script(html_data):

    for script in html_data(text=re.compile(r'trackingParam' )):
        regex = re.search('trackingParam = (?P<data>.+})', script)
        data = json.loads(regex.group('data'))
        return data


driver = webdriver.Chrome('/Applications/chromedriver')
base_url = 'https://www.daft.ie'
df = pd.read_csv('./data/link_data.csv')
temp_file = './temp.html'

for index, row in df.iterrows():
    url = base_url + row['link']
    driver.get(url)
    html = driver.page_source
    save_html(html, temp_file)
    time.sleep(3)

    with open(temp_file, 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        scraped_data = create_dict_from_script(soup)

    with open('data.json','r+') as json_file:
        house_data = json.load(json_file) 
        temp_house_data = house_data['house_data'] 
        # python object to be appended 
        data_to_be_added = scraped_data

        # appending data to house_data  
        temp_house_data.append(data_to_be_added) 

    write_json(house_data)
    print(index)
    
    time.sleep(random.randint(5,10));