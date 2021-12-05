from bs4 import BeautifulSoup
import pandas as pd
import re
import glob


# Helpers
# This one creates a lsit of items we need from the html
def create_list(link_type, attrib_type, attrib_name, property_type=None):
    lst = [];
    all_items = soup.find_all(link_type, attrs={ attrib_type : attrib_name})

    for item in all_items:
        if property_type:
            line_item = item.get(property_type)
        else: 
            line_item = item.text

        lst.append(line_item)
    return lst

# Create the DataFrame we will save to CSV 
df = pd.DataFrame(columns=['link'])

# Get the files we have scraped
files = glob.glob("./data/*.html")

# For each file create a list of all the attributes etc from the webpage that we need 
for i in files: 
    with open(i, 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')

    link_list = create_list('a','class','PropertyInformationCommonStyles__quickPropertyDetailsContainer--link', 'href') 

    i=0;

    # Add the lists to the dataframe row by row
    while i < len(link_list):
        df = df.append(
            {
                'link': link_list[i]
            }
        , ignore_index=True)
        i+=1;

df.to_csv('./data/link_data.csv', index=False)





