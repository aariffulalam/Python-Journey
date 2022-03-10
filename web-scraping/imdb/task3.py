import json

try:
    read_file=open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/imdb/task1.json","r")
    movie_list=json.load(read_file)
    years=[]
    for i in movie_list:
        years.append(i["year"])
except:
    from task1 import scrape_top_list
    years=[]
    for i in scrape_top_list():
        years.append(i["year"]) 

def group_by_decade():
    dict2={}
    l=1950
    while l<2030:
        list2=[]
        for k in movie_list:
            if k["year"]>=l and k["year"]<l+10:
                list2.append(k)
        dict2[l]=list2
        l+=10
    return dict2
call=group_by_decade()
creat=open("/home/dhruv101/Desktop/programming_languages/python/web_scraping/imdb/task3.json","w")
dumping=json.dump(call,creat,indent=4)
creat.close()