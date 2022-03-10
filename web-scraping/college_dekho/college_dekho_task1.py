import requests
from bs4 import BeautifulSoup
import json
import pprint

url="https://www.collegedekho.com/btech-mechanical_engineering-colleges-in-india/"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")

def scrape_collage_list():
    first_div=soup.find("div",class_="body collegeListing")
    second_div=first_div.find("div",class_="container collegeListingContent")
    third_div=second_div.find("div",class_="listing-content rightside")
    fourth_div= third_div.find("div",class_="middle-container")
    fifth_div=fourth_div.find("div",class_="row collegeBlock")
    sixth_div=fifth_div.find_all("div")
    dict1={}
    for i in sixth_div:
            url_base="https://www.collegedekho.com"
            name_data=""
            found=i.find("div",class_="box")
            if found==None:
                pass
            else:
                data2=found.a["href"]
                url_data=url_base+data2
                data1=found.find("a").text.strip()
                dict1[data1]=url_data
    return dict1
details_source=scrape_collage_list()
file=open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/college_dekho/college_dekho_task1.json","w")
save=json.dump(details_source,file,indent=4)
file.close()