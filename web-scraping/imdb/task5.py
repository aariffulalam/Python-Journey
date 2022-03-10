from os import close
import requests
from bs4 import BeautifulSoup
import json
import pprint


try:
    read_file=open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/imdb/task1.json","r")
    scrape_top_list=json.load(read_file)
    top_movie=[]
    for i in scrape_top_list:
        top_movie.append(i["url"])
except:
    from task1 import scrape_top_list
    top_movie=[]
    for i in scrape_top_list():
        top_movie.append(i["url"]) 
from task4 import scrape_movie_details
def scrape_movie_details(movies_list):
    movies_details=[]
    for i in movies_list:
        details=scrape_movie_details(i)
        movies_details.append(details)
    return movies_details
data=scrape_movie_details(top_movie[:10])
file=open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/task5.json","w")
save=json.dump(data,file,indent=4)
file.close()