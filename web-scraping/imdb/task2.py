import json


# from task1 import scrape_top_list
# print(scrape_top_list())



try:
    read_file=open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/imdb/task1.json","r")
    scrape_top_list=json.load(read_file)
    years=[]
    for i in scrape_top_list:
        years.append(i["year"])
except:
    from task1 import scrape_top_list
    years=[]
    for i in scrape_top_list():
        years.append(i["year"])
movie_years=list(set(years))
movie_years.sort()    

def group_by_year():
    dict1={}
    for i in movie_years:
        list1=[]
        for j in scrape_top_list:
            if j["year"]==i:
                list1.append(j)
        dict1[i]=list1
    return dict1
call=group_by_year()
creat=open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/imdb/task2.json","w")
dumping=json.dump(call,creat,indent=4)
creat.close()
