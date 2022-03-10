# * * * Task 1 * * *
# Pehli task mein humein Top Rated Indian Movies wale IMDB page se saari top rated movies ki list
# nikaalni hai. Page ka link yeh hai: https://www.imdb.com/india/top-rated-indian-movies/ 
# Humein ek function likhna hai 1. name movie ka naam hai. Yeh ek string mein hona chaiye.
# 2. year should be an integer. Yeh movie ki release date hai. 
# 3. positon movie ka position in the list hai. Yeh ek integer hona chaiye.
# 4. url movie ke indivual page ka link hona chaiye. 
# 5. rating movie ke rating honi chaiye. Yeh ek float hoga.

import requests
import json
import pprint
from bs4 import BeautifulSoup
url="https://www.imdb.com/india/top-rated-indian-movies/"
page= requests.get(url)
# print(page)
soup=BeautifulSoup(page.text,"html.parser")
# print(soup)
def scrape_top_list():
    main_div=soup.find("div",class_="lister")
    # return main_div
    tbody=main_div.find("tbody",class_="lister-list")
    # return tbody
    trs=tbody.find_all("tr")
    movie_ranks=[]
    movie_name=[]
    year_of_realease=[]
    movie_rating=[]
    movie_link=[]
    for tr in trs:
        position=tr.find("td",class_="titleColumn").get_text().strip()
        rank=""
        for i in position:
            if "." not in i:  
                rank=rank+i
            else:
                break
        movie_ranks.append(rank)
        name=tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(name)
        year=tr.find("td",class_="titleColumn").span.get_text()
        year_of_realease.append(int(year[1:5]))
        rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(rating)
        url=tr.find("td",class_="titleColumn").a["href"]
        url1="https://www.imdb.com"+url
        movie_link.append(url1)    
    movie_list=[]
    dict1={"name":"","year":"","position":"","rating":"","url":""}
    for i in range(0,len(movie_ranks)):
        dict1["name"]=str(movie_name[i])
        year_of_realease[i]=year_of_realease[i]
        dict1["year"]=int(year_of_realease[i])
        dict1["position"]=int(movie_ranks[i])
        dict1["rating"]=float(movie_rating[i])
        dict1["url"]=movie_link[i]        
        movie_list.append(dict1)
        dict1={"name":"","year":"","position":"","rating":"","url":""}


    return movie_list
ss=scrape_top_list()
s=open('/home/dhruv101/Desktop/programming_languages/python/web_scraping/imdb/task1.json','w')
d=json.dump(ss,s,indent=4)
s.close()