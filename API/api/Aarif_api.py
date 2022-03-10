print("Aarif_api.py")

# 1 you have to scrape data from the following link.
# import requests , json
# data1=requests.get("http://saral.navgurukul.org/api/courses") # this is in json form
# print(data1)             # this will give us respond that we re getting permission or not
# with open("/home/ng/Desktop/Aarif_alam/Scraping/Aarif_api1.json","w") as api1:
#     json.dump(data1.json(),api1,indent=5)

# with open("/home/ng/Desktop/Aarif_alam/Scraping/Aarif_api1.json","r") as api2:
#     data2=json.load(api2)
#     print(data2)




# * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

import requests 
import  json

data1=requests.get("http://saral.navgurukul.org/api/courses")
print(data1)

with open("/home/ng/Desktop/Aarif_alam/Scraping/api1-1.json","w") as api1:
    json.dump(data1.json(),api1,indent=5)
with open("/home/ng/Desktop/Aarif_alam/Scraping/api1-1.json","r") as api1r:
    data2=json.load(api1r)

num1=0
list1=[]
for i in data2["availableCourses"]:
    print(num1,end=" ")
    num1+=1
    print(i["name"])
    list1.append(i["id"])
# print(list1)
input1=int(input("neter your number  - "))
data3=requests.get("http://saral.navgurukul.org/api/courses"+"/"+list1[input1]+"/"+"exercises")

with open("/home/ng/Desktop/Aarif_alam/Scraping/slug_api1-1.json","w") as api2:
    json.dump(data3.json(),api2,indent=5)
with open("/home/ng/Desktop/Aarif_alam/Scraping/slug_api1-1.json","r") as api2r:
    data4=json.load(api2r)
list2=[]
name=[]
num2=0
for j in data4["data"]:
    print(num2,end=" ")
    print(j["name"])

    name.append(j["name"])
    list2.append(j["id"])
    num2+=1
    if j["childExercises"]==True:
        print(j["childExercises"])
# print(name)
# print(list2)
input2=int(input("Enter your any number :- "))
data5=requests.get("http://saral.navgurukul.org/api/courses/"+list1[input1]+"/exercise/getBySlug?slug="+name[input2])
# print(data5)
with open("/home/ng/Desktop/Aarif_alam/Scraping/childslug_api1-1.json","w") as api3:
    json.dump(data5.json(),api3,indent=5)
with open("/home/ng/Desktop/Aarif_alam/Scraping/childslug_api1-1.json","r") as api3r:
    data6=json.load(api3r)
for i in data6:
    if i=="content":
        a=data6.get(i)
        print(a)
b=json.loads(a)
print(type(b))
for k in b:
    for l in k:
        if l=="value":
            c=k.get(l)
            print(c)