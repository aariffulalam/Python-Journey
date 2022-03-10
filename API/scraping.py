

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
        url1="https://www.imbd.com"+url
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
s=open('task1.json','w')
d=json.dump(ss,s,indent=4)
s.close()
# pprint. pprint(scrape_top_list())
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 

# * * * Task 2 * * *
# Group by year method saari same saal wali movies ko ek saath group karega.
# Aapke iss function ko ek aisa data structure return karna hai.
# import requests
# import pprint
# from bs4 import BeautifulSoup
# url="https://www.imdb.com/india/top-rated-indian-movies/"
# page= requests.get(url)
# soup=BeautifulSoup(page.text,"html.parser")
# def group_by_year():
#     main_div=soup.find("div",class_="lister")
#     tbody=main_div.find("tbody",class_="lister-list")
#     trs=tbody.find_all("tr")
#     movie_ranks=[]
#     movie_name=[]
#     year_of_realease=[]
#     movie_rating=[]
#     movie_link=[]
#     for tr in trs:
#         position=tr.find("td",class_="titleColumn").get_text().strip()
#         rank=""
#         for i in position:
#             if "." not in i:
#                 rank=rank+i
#             else:
#                 break
#         movie_ranks.append(rank)
#         name=tr.find("td",class_="titleColumn").a.get_text()
#         movie_name.append(name)
#         year=tr.find("td",class_="titleColumn").span.get_text()
#         year_of_realease.append(int(year[1:5]))
#         rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
#         movie_rating.append(rating)
#         url=tr.find("td",class_="titleColumn").a["href"]
#         url1="https://www.imbd.com"+url
#         movie_link.append(url1)  
#     set1=set(year_of_realease)
#     list1=list(set1)
#     list1.sort() 
#     movie_list=[]
#     dict1={"name":"","year":"","position":"","rating":"","url":""}
#     for i in range(0,len(movie_ranks)):
#         dict1["name"]=str(movie_name[i])
#         year_of_realease[i]=year_of_realease[i]
#         dict1["year"]=int(year_of_realease[i])
#         dict1["position"]=int(movie_ranks[i])
#         dict1["rating"]=float(movie_rating[i])
#         dict1["url"]=movie_link[i]        
#         movie_list.append(dict1)
#         dict1={"name":"","year":"","position":"","rating":"","url":""}
#     dict2={}
#     for j in list1:
#         list2=[]
#         for k in movie_list:
#             if k["year"]==j:
#                 list2.append(k)
#         dict2[j]=list2
#     return dict2
# pprint.pprint(group_by_year())
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 

# * * * Task 3 * * *
# Ab hum inn hi movies ko decade ke hisaab se group karenge. 10 saal se milakar ek decade banta hai. 
# Jaise: 1. 1960 se 1969 tak ke beech ke saare saal 1960s ke decade mein aate hain.
# 2. 1970 se 1979 tak ke beech ke saare saal 1970s ke decade mein aate hain.
# 3. 1980 se 1989 tak ke beech ke saare saal 1980s ke decade mein aate hain.
# 4. 2000 se 2009 tak ke beech ke saare saal 2000s ke decade mein aate hain.

# import requests
# import pprint
# from bs4 import BeautifulSoup
# url="https://www.imdb.com/india/top-rated-indian-movies/"
# page= requests.get(url)
# soup=BeautifulSoup(page.text,"html.parser")
# def group_by_decade():
#     main_div=soup.find("div",class_="lister")
#     tbody=main_div.find("tbody",class_="lister-list")
#     trs=tbody.find_all("tr")
#     movie_ranks=[]
#     movie_name=[]
#     year_of_realease=[]
#     movie_rating=[]
#     movie_link=[]
#     for tr in trs:
#         position=tr.find("td",class_="titleColumn").get_text().strip()
#         rank=""
#         for i in position:
#             if "." not in i:
#                 rank=rank+i
#             else:
#                 break
#         movie_ranks.append(rank)
#         name=tr.find("td",class_="titleColumn").a.get_text()
#         movie_name.append(name)
#         year=tr.find("td",class_="titleColumn").span.get_text()
#         year_of_realease.append(int(year[1:5]))
#         rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
#         movie_rating.append(rating)
#         url=tr.find("td",class_="titleColumn").a["href"]
#         url1="https://www.imbd.com"+url
#         movie_link.append(url1)  
#     set1=set(year_of_realease)
#     list1=list(set1)
#     list1.sort() 
#     movie_list=[]
#     dict1={"name":"","year":"","position":"","rating":"","url":""}
#     for i in range(0,len(movie_ranks)):
#         dict1["name"]=str(movie_name[i])
#         year_of_realease[i]=year_of_realease[i]
#         dict1["year"]=int(year_of_realease[i])
#         dict1["position"]=int(movie_ranks[i])
#         dict1["rating"]=float(movie_rating[i])
#         dict1["url"]=movie_link[i]        
#         movie_list.append(dict1)
#         dict1={"name":"","year":"","position":"","rating":"","url":""}
#     dict2={}
#     l=1950
#     while l<2030:
#         list2=[]
#         for k in movie_list:
#             if k["year"]>=l and k["year"]<l+10:
#                 list2.append(k)
#         dict2[l]=list2
#         l+=10
#     return dict2
# pprint.pprint(group_by_decade())
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


# * * * Task 4 * * *

# import requests
# import pprint
# from bs4 import BeautifulSoup
# url="https://www.imdb.com/india/top-rated-indian-movies/"
# page= requests.get(url)
# # print(page)
# soup=BeautifulSoup(page.text,"html.parser")
# # print(soup)
# def scrape_top_list():
#     main_div=soup.find("div",class_="lister")
#     # return main_div
#     tbody=main_div.find("tbody",class_="lister-list")
#     # return tbody
#     trs=tbody.find_all("tr")
#     movie_ranks=[]
#     movie_name=[]
#     year_of_realease=[]
#     movie_rating=[]
#     movie_link=[]
#     for tr in trs:
#         position=tr.find("td",class_="titleColumn").get_text().strip()
#         rank=""
#         for i in position:
#             if "." not in i:  
#                 rank=rank+i
#             else:
#                 break
#         movie_ranks.append(rank)
#         name=tr.find("td",class_="titleColumn").a.get_text()
#         movie_name.append(name)
#         year=tr.find("td",class_="titleColumn").span.get_text()
#         year_of_realease.append(int(year[1:5]))
#         rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
#         movie_rating.append(rating)
#         url=tr.find("td",class_="titleColumn").a["href"]
#         url1="https://www.imbd.com"+url
#         movie_link.append(url1)    
#     movie_list=[]
#     dict1={"name":"","year":"","position":"","rating":"","url":""}
#     for i in range(0,len(movie_ranks)):
#         dict1["name"]=str(movie_name[i])
#         year_of_realease[i]=year_of_realease[i]
#         dict1["year"]=int(year_of_realease[i])
#         dict1["position"]=int(movie_ranks[i])
#         dict1["rating"]=float(movie_rating[i])
#         dict1["url"]=movie_link[i]        
#         movie_list.append(dict1)
#         dict1={"name":"","year":"","position":"","rating":"","url":""}
#     print (movie_link)

# pprint. pprint(scrape_top_list())