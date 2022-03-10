import requests
from bs4 import BeautifulSoup
import json
import pprint

try:
    read_file=open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/imdb/task1.json","r")
    scrape_top_list=json.load(read_file)
    url=[]
    for i in scrape_top_list:
        url.append(i["url"])
except:
    from task1 import scrape_top_list
    url=[]
    for i in scrape_top_list():
        url.append(i["url"]) 
choose_movie_rank=int(input("enter your movie rank for scraping details of that movie   - "))
url_of_movie=scrape_top_list[choose_movie_rank-1]["url"]

def scrape_movie_details(movie_url):
    page= requests.get(movie_url)
    soup=BeautifulSoup(page.text,"html.parser")

    dictionary={"name":"","director":"","country":"","language":"","poster_image_url":"","bio":"","runtime":"","genre":""}

    name_div=soup.find("div",class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt").h1.get_text()
    dictionary["name"]=name_div
    # print(name_div)

    list1=[]
    gener = soup.find("div",class_="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL")
    for x in gener:
        list1.append(x.text)
        # print(x.text)
    dictionary["genre"]=list1

    time_=soup.find("ul",class_="ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt").find_all("li")
    p=1
    for i in time_:
        # print(i.text)
        if p==3:
            dictionary["runtime"]=i.text
        p+=1

    bio_=soup.find("span",class_="GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD").text
    dictionary["bio"]=bio_
    # print(bio_)

    dir_=soup.find("section",class_="ipc-page-section ipc-page-section--base StyledComponents__CastSection-y9ygcu-0 fswvJC celwidget").find("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all StyledComponents__CastMetaDataList-y9ygcu-10 cbPPkN ipc-metadata-list--base").find("ul",class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base").find_all("li",class_="ipc-inline-list__item")
    dir_list=[]
    for i in dir_:
        anchor=i.find("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
        dir_list.append(anchor)
        # print(anchor)
    dictionary["director"]=dir_list
    # print(dir_list)

    country_main_div=soup.find(class_="ipc-page-grid ipc-page-grid--bias-left").find("div",class_="TitleMainBelowTheFoldGroup__TitleMainPrimaryGroup-sc-1vpywau-1 btXiqv ipc-page-grid__item ipc-page-grid__item--span-2").find_all("section")
    j=1
    for i in country_main_div:
        if choose_movie_rank==20:
            if j==10:
                section1=i.find("div",class_="styles__MetaDataContainer-sc-12uhu9s-0 cgqHBf").find("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base").find_all("li")
                z=1
                for l in section1:
                    # print(l.text,">>>")
                    if  z==4:
                        dictionary["country"]=l.text        
                    elif z==8:
                        dictionary["language"]=l.text
                    z+=1
        else:
            if j == 9:
                section=i.find("div",class_="styles__MetaDataContainer-sc-12uhu9s-0 cgqHBf").find("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base").find_all("li")
                x=0
                for k in section:
                    # print(k.text,"<<<")
                    if x==3:
                        dictionary["country"]=k.text
                    elif x==5:
                        dictionary["language"]=k.text
                    x+=1
        j+=1


    poster=soup.find("div",class_="ipc-media ipc-media--poster ipc-image-media-ratio--poster ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img").img["src"]
    # print(poster)
    dictionary["poster_image_url"]=poster
    # print(dictionary)

    with open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/imdb/task4.json","w") as create:
        json.dump(dictionary,create,indent=4)


scrape_movie_details(url_of_movie)






























































    # country=soup.find("section",class_="ipc-page-section ipc-page-section--base celwidget").find_all("div")
    # j=1
    # for i in country:
    #     print(i)


    # country_=soup.find("li",class_="ipc-metadata-list__item").find("div",class_="ipc-metadata-list-item__content-container").find("ul",class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base")
    # print(country_)


    # gener1= soup.find("div",class_="ipc-metadata-list-item__content-container")
    # print(gener1)
    # for x in gener1:
    #     m=soup.find("x")
    #     print(m)
    # genre_main_div=soup.find_all("div",class_="ipc-metadata-list-item__content-container")
    # genre_div=genre_main_div.find_all("li")
    # for i in genre_div:
    #     print(i)
        

    # bio_div=soup.find("div",class_="Hero__MetaContainer__Video-kvkd64-4 kNqsIK").span.get_text()
    # print(bio_div)
    # country_div=soup.find("div",class_="ipc-metadata-list-item__content-container")
    # country1=country_div.find("ul")
    # print(country1)
    # print()
    # country2=country1.find("li")
    # print(country2)
    # print()
    # country3=country2.find("a").get_text()
    # print(country3)


    # runtime_main_div=soup.find("div",class_="ipc-metadata-list-item__content-container")
    # runtime_sub_dive=runtime_main_div.find("li").span.get_text()
    # print(runtime_sub_dive)
    
    # director_list=[]
    # directors_div=soup.find_all("div",class_="ipc-metadata-list-item__content-container")
    # directors_div_command=soup.find_all("div",class_="ipc-metadata-list-item__content-container").a.get_text()
    # print(directors_div_command)
    # for i in directors_div:
    #     print(i())
    #     print(type(i))
    #     if i==directors_div_command:
    #         director_list.append(directors_div_command.get_text())
    # print(director_list)
        
    