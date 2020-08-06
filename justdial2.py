from bs4 import BeautifulSoup
import urllib
import requests
import urllib.request
import csv
import pandas as pd


def get_category(body):
	return body.text.strip()

def get_data(url):   
    
    req = urllib.request.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}) 
    page = urllib.request.urlopen( req )
    soup = BeautifulSoup(page.read(), "html.parser")
    service = soup.find('a', {'class': 'lng_als_lst'})
    if service:
        print("url>>>>>>>", url)
        print("servicess>>>>>>>>>>>>>", service)
        category = get_category(service)
        print("Category:", category)

        return category
    print("category:", None)    
    return None
     

out_file = open('panchkula_categories_data.csv','w')

# out_df = pd.read_csv('hardware3.csv', delim_whitespace=True)
# print(out_df.columns)

fields = ['Url', 'Category']
main_file = pd.read_csv('PANCHKULA.csv', error_bad_lines=False)
csvwriter = csv.DictWriter(out_file, delimiter=',', fieldnames=fields)

for row in main_file.itertuples():
    dict_service = {}
    url = row[1]
    category = get_data(url)
    dict_service['Url'] = url
    dict_service['Category'] = category
    csvwriter.writerow(dict_service)

out_file.close()
    


# 


