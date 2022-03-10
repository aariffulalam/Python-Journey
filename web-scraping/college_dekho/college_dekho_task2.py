import json
url_list=[]
try:
    read_file=open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/college_dekho/collage_dekho_task1.json","r")
    scrape_collage_list=json.load(read_file)
    for i in scrape_collage_list:
        url_list.append(scrape_collage_list[i])    
except:
    from college_dekho_task1 import scrape_collage_list
    for i in scrape_collage_list():
        url_list.append(scrape_collage_list()[i])

import requests
from bs4 import BeautifulSoup
import json
import pprint

def scrape_collage_details():
    collage_details={}
    for j in url_list:
        page=requests.get(j)
        soup=BeautifulSoup(page.text,"html.parser")
        main_div=soup.find("div",class_="header collegeDetails").find("div",class_="container").find("ul",class_="breadcrumb").find_all("li")
        a=1
        for k in main_div:
            # print(k.text)
            if a==4:
                collage_name=k.text
                # print(k.text)
                # print("collage name")
            a+=1
        # print(collage_name)
        dict1={"Contact No":"","Email ID":"","Website":"","address":"","features":""}
        second_div=soup.find("div",class_="block collegeContactBlock").find("div",class_="box").find("div",class_="collegeContacts").find("div",class_="collegeAddress").find("ul",class_="addressList").find_all("li")
        a=1
        for i in second_div:
            contacts=i.find("div",class_="data").text
            # print(contacts)
            if a == 1:
                dict1["Contact No"]=contacts[67::]
                # print(len(contacts))
            elif a==2:
                dict1["Email ID"]=contacts
            elif a==3:
                dict1["Website"]=contacts
            else:
                dict1["address"]=contacts
            a+=1
        
        # print(contacts)       
        
        third_div= soup.find("div",class_="block facilitiesBlock").find("div",class_="box").text
        dict1["features"]=third_div
        # print(third_div)
        collage_details[collage_name]=dict1
    return collage_details    
ss=scrape_collage_details()        
file=open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/college_dekho/college_dekho_task2.json","w") 
put=json.dump(ss,file,indent=4)
file.close()   