import json
from bs4 import BeautifulSoup
import requests

url="https://www.giveindia.org/certified-indian-ngos"
page=requests.get(url)
# print(page)
soup=BeautifulSoup(page.text,"html.parser")
# print(soup)
def scrape_give_india():
    NGO_names={}
    # main_div=soup.find("div",id="__next").div
    # second=main_div.find("div",class_="jsx-3668981697 sc-desktop-padding-style")
    # print(second)
    divs=soup.find("div",class_="d-flex f-d-col w-100 p-0 container")
    
    # print(divs)
    for i in divs:
        # print(i.text)
        second_div=i.find("div",class_="d-flex f-d-col col-10 col-sm-10").h5.text
        # print(second_div)
        NGO_informationas={}
        third_div=i.find("div",class_="d-flex f-d-col col-10 col-sm-10").div
        type=""
        state=""
        a=0
        for i in third_div.text:
            if a==1:
                state=state+i
            else:
                type=type+i
            if i =="|":
                a+=1    
        NGO_informationas["type"]=type[:len(type)-1:]
        NGO_informationas["state"]=state

        NGO_names[second_div]=NGO_informationas
            # print(i)
            # print(i.text)
            # print("<<<<<<")
        # print(third_div)
    return NGO_names
ss=scrape_give_india()
file= open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/give_india_ngos/give_india_task1.json","w")
save=json.dump(ss,file,indent=4)
file.close()