
print('API "application object interface"')
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * * * * * *  * *
#                              M E R A K I
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **

# 1 API humne abhi samjha kya hote hai. Ab hum ek API ko call kar kar kuch data mangwayenge.
#   http://saral.navgurukul.org/api/courses iss link ko open karo. SARAL ke server par yeh data hai, jo hum 
#   iss course mei use karenge. Abhi ke liye, humei ek bahut simple sa code likhna hai.

# import requests , json
# data1=requests.get("http://saral.navgurukul.org/api/courses") # this is in json form
# print(data1)             # this will give us respond that we re getting permission or not
# with open("/home/ng/Desktop/Aarif_alam/Scraping/api1.json","w") as api1:
#     json.dump(data1.json(),api1,indent=5)









#  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

































# with open("/home/ng/Desktop/Aarif_alam/Scraping/api1-1.json","w") as api1:
#     json.dump(soup.json(),api1,indent=3)

# with open("/home/ng/Desktop/Aarif_alam/Scraping/api1-2.json","r") as api2:
#     data2=json.load(api2)
#     print(data2)

# for i in data2:
#     print(i)








# # # # # #
# import requests , json
# data1=requests.get("http://saral.navgurukul.org/api/courses").text # this is in json form
# print(data1)             # this will give us respond that we re getting permission or not
# with open("/home/ng/Desktop/Aarif_alam/Scraping/api1-2.json","w") as api1:
#     # data1=json.dumps(data1)
#     json.dump(data1,api1,indent=5) # Error- "str" object has no attribute "json"

# # # # # #



# ####################
# import requests
# import json
# from bs4 import BeautifulSoup
# url=requests.get("https://saral.navgurukul.org/api/course")
# print(url.json())
# soup=BeautifulSoup(url,"html.parser")
# print(soup)
# with open("/home/ng/Desktop/Aarif_alam/Scraping/api1-3.json","w") as api1:
#     data1=json.dumps(url)
#     json.dump(url,api1,indent=5)
# #########################

# import requests , json
# from bs4 import BeautifulSoup
# res = requests.get("https://www.flipkart.com/").text
# print(res)
# url=BeautifulSoup(res,"html.parser")
# print(url)
##########
# import requests , json
# from bs4 import BeautifulSoup
# res = requests.get("https://www.flipkart.com/")
# soup=BeautifulSoup(res,"html.parser")
# print(soup)
# with open("/home/ng/Desktop/Aarif_alam/Scraping/karo11.json","w") as obb:
#     data1=json.dump(soup,obb,indent=3)
##########


# soup=BeautifulSoup(res,"html.parser")
# print(soup)


# import requests
# import json
# from bs4 import BeautifulSoup
# url=requests.get("https://saral.navgurukul.org/course").text
# soup=BeautifulSoup(url,"html.parser")
# print(soup)
# print(url)



# import json
# import requests
# from bs4 import BeautifulSoup

# url=requests.get("http://saral.navgurukul.org/api/courses").text
# soup=BeautifulSoup(url,"html.parser")
# with open("qwer.json","w") as obj:
#     json.dump(url.json(),obj,sort_keys=True,indent=4)
# with open("api.json","r") as a:
#     d=json.load(a)
# for x in d["availableCourses"]:

#     print(x["name"])
#     json.dumps(x,indent=4)


# import requests , json
# data1=requests.get("http://saral.navgurukul.org/api/courses")
# print(data1)
# # # # data1=json.loads(data1)   # Error:- Data have to be json str to change into json object/ pyhton
# with open("/home/ng/Desktop/Aarif_alam/Scraping/api2.json","w") as api1:
    # json.dump(data1,api1,indent=5)        # here we have to change in data in argument
# with open("/home/ng/Desktop/Aarif_alam/Scraping/api2.json","r") as api1:
#     a=json.load(api1)
#     print(a)




