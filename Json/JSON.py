# print('I am JSON')

#JSON is the short form of JavaScript Object Notation and is a text-based information format that follows JavaScript object syntax.


# JSON stand for Java Script object Notetion.
# JSON is a formate of Storing and Transporting data.
# JSON is often used when data is sent from a Server to a Web page.
# JSON is lightweight data interchange formate.
# JSON is language Independent.
# JSON is "self-discribing" and Easy to understand.
# json is string format and accept only "" quots, inside it's dictonary forma - "{}"



# * * * json.dumps() * * *
# dumps() function, it is convert python dictionary to json format string.
# import json
# a={'name':'Aarif','age':19}
# print(type(a))
# a=json.dumps(a)           # here it is changening python dictionry to to json string 
# print(a)
# print(type(a))


# * * * JSON.loads() * * *
# loads() function parsed the "str data"  - 
#                              Parsing JSON means interpreting the data with the specific language that you are 
#                              using at that moment.JSON is usually read as a string  called the JSON string.
#                              When we parse JSON, it means we are converting the string into a JSON object by 
#                              following the JSON specification, where we can then use it in any way we wish.
# import json
# a={'name':'Aarif','age':19}  # '_' , if we take json values in single quots then gives error
# #                                    TypeError:- the JSON object must be str, bytes or bytearry, not dict 
# # a={"name":"Aarif","age":19}     # same error 
# # so first we have to change it into json
# a=json.dumps(a)        # python dict is changing into json str
# a=json.loads(a)
# print(a)
# print(type(a))


# import json
# s={1:"shubham",2:"Aarif"}
# f=open("/home/ng/new2.json","r")
# a=json.dump(s,f,indent=5)
# # b=f.read()
# b=json.load(f)
# print(b)
# f.close()



# import json 
# s={1:"shubham",2:"Aarif"}
# f=open("/home/ng/Desktop/Aarif_alam/JSON/new4.json","r")
# # a=json.dump(s,f,indent=4)
# b=json.load(f)
# print(b)
# f.close()



# import json
# dict1={"Aa":1,"Bb":2}        #
# dict1=json.dumps(dict1)      # Dictionary change into json
# print(dict1)
# print(type(dict1))
# f=open("new8.json","w")      #
# data1=f.write(dict1)         #
# f=open("/home/ng/new8.json","r")  ##
# print(data1)                      ## readind the json
# print(type(data1))                ##
# f=open("/home/ng/new8.json","r")
# data1=json.


# write and dumps







# import json
# f=open("new6.json","w")          # making file
# s={"Aarif":99,"Akash":99.9}      #
# data1=f.write(str(s))            #
# f.close()                        #
# f=open("new5.json","r")                           #reading file
# data=f.read()                                     #
# print(data)                                       #
# print(type(data))                                 #
# f.close()                                         #
# f=open("/home/ng/Desktop/Aarif_alam/JSON/new6.json","r")
# data=json.dump(s,f,6)
# j=json.load(f)
# print(j)


# import json
# f=open("/home/ng/new6.json","r")
# data1=json.dump(f)
# print(data1)
# f.close()



# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
#                                      w3schools    JSON
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.

# # Import the json module:
# import json




#    * * Parse JSON * * 

# #  Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
#  The result will be a Python dictionary.


# ex- convert json to python
# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'       # some JSON:
# y = json.loads(x)                 # parse x:
# print(y["age"])              # the result is a Python dictionary:


# # Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# Convert from Python to JSON:

# import json
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# y = json.dumps(x)                  # convert into JSON:
# print(y)                      # the result is a JSON string:


# You can convert Python objects of the following types, into JSON strings:
# dict
# list
# tuple
# str
# int
# float
# True
# False
# None


# Example- Convert Python objects into JSON strings, and print the values:
# import json
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# # * Python                               * JSON
# dict	                               Object
# list	                               Array
# tuple                                  Array
# str	                                   String
# int	                                   Number
# float	                               Number
# True	                               true
# False	                               false
# None	                               null


# ex - Convert a Python object containing all the legal data types:
# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# c=1
# a=json.dumps(x)    # json is a form of str so it will take all laters in loop.
# print(a)
# for i in a:
#     print(type(i))
#     print(c)
#     c+=1


# Using only dumps() function then it will be harder to read without indententation.
# The json.dumps() method has parameters to make it easier to read the result:
# ex-Use the indent parameter to define the numbers of indents:

# json.dumps(x, indent=4)



#      * * json.dump()
# The dump() method is used when the Python objects have to be stored in a file. The dumps() is used 
# when the objects are required to be in string format and is used for parsing, printing, etc, .
# The dump() needs the json file name in which the output has to be stored as an argumen

# dump() and its arguments
# Syntax: 
# json.dump(d, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True,
# cls=None, indent=None, separators=None)

# creating a file in json
# import json
# a='{"peraunda":"keli"}'
# a=json.loads(a)
# print(type(a))
# f=open("/home/ng/Desktop/Aarif_alam/JSON/1.json","w")    #   fp- file point
# data1=json.dump(a,f,indent=5)
# f.close()



#      * * json.load() * *     #
# json.load() takes a file object and returns the json object.
# A JSON object contains data in the form of key/value pair.
# The keys are strings and the values are the JSON types.
# Keys and values are separated by a colon.


# Syntax : json.load(file_object)

# Return : It return json object.

# import json
# f=open("/home/ng/Desktop/Aarif_alam/JSON/1.json","r")
# a=json.load(f)
# print(a)







# Q.1 Json data ko python object main convert karne ka program likho?.
# import json
# a='{"Name":"Ram", "Class":"IV","Age":"9" }'
# a=json.loads(a)
# print(a)
# print(type(a))


# Q.2 Python object ko json data main convert karne ka program likho?
# import json
# from os import write
# a={
#     "name": "David",
#      "class":"I",
#      "age": 6  
#  }
# a=json.dumps(a)                              # python object to json-str
# f=open("/home/ng/Desktop/Aarif_alam/JSON/2.json","w")
# data1=f.write(a)
# f.close()

# f=open("/home/ng/Desktop/Aarif_alam/JSON/2.json","r")     # converting json-str  to  json object
# a=json.load(f)
# print(a)
# print(type(a))


# Q.3 Python object ko json string mai convert karne ka program likho?
# import json
# a={
#     "name": "David",
#      "class":"I",
#      "age": 6  
#  }
# a=json.dumps(a)
# print(a)
# print(type(a))


# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho? 

# import json
# a={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4
#     }

# a=json.dumps(a)                              # python object to json-str
# f=open("/home/ng/Desktop/Aarif_alam/JSON/3.json","w")
# data1=f.write(a)
# f.close()

# f=open("/home/ng/Desktop/Aarif_alam/JSON/3.json","r")   #reading the file and this fully string every object
# data1=f.read()
# print(data1)
# print(type(data1))
# for i in data1:
#     print(i)
#     print(type(i))

# f=open("/home/ng/Desktop/Aarif_alam/JSON/3.json","r")     # converting json-str  to  json object
# a=json.load(f)
# print(a)
# print(type(a))


# # Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?
# import json      ##################### to using complex number in json you will get error ##################
# # a={'4': 5, '6': 7, '1': 3, '2': 4}
# # # a=json.dumps(a)                            # python object to json-str     # it will not accept complex number
# # print(type(a))
# # f=open("/home/ng/Desktop/Aarif_alam/JSON/4.json","w")
# # data1=json.dump(a,f,indent=5)
# # f.close()
# f=open("/home/ng/Desktop/Aarif_alam/JSON/4.json","r")     # converting json-str  to  json object
# a=json.load(f)
# print(a)
# print(type(a))


# Q6.Python object key unique key value ko access karne ka program likho?
# import json
# a='{"a":  1,"a":  2,"a":  3, "a": 4,"b": 1,"b": 2}'
# a=json.loads(a)
# print(a)
# print(type(a))


# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
# import json
# a=open("/home/ng/Desktop/Aarif_alam/JSON/7text.txt","w")
# b=a.write("""Name Abhishek
# Designation CEO of navgurukul
# Gender male
# Age 29 """)
# a.close()

# a=open("/home/ng/Desktop/Aarif_alam/JSON/7text.txt","r")
# c=a.readlines()
# z=open("/home/ng/Desktop/Aarif_alam/JSON/7Json_file.json","w")
# new={}
# for x in c:
#     old=""
#     b=0
#     for y in x:     
#         if y!=" ":
#             old+=y
#         else:
#             c=x[b:]
#             d=c[:-1]
#             break 
#         b+=1
#     new[old]=d
# json.dump(new,z,indent=4)
# a.close()
# z.close()



# Q8.Tumhare pass four employes ki details hai list mai:- ab aapko 4 dictionaries create karni hai jaise
# ki emp1 emp2 emp3 and emp4.har ek employee ka dictionary main name,designation,age and salary honi chahiye.
# aur ye sab dictionary ki keys hai jismai maine list main value di hai.Iska use kar ke aapko ek 
# json file create karni hai? Jaise ki niche diya hai.
# import json
# fp=open("/home/ng/Desktop/Aarif_alam/JSON/8emp.txt","w")
# data1=[["neelam","programer","24","2400"],
# ["komal","trainer","24","20000"],
# ["anuradha","HR","25","40000"],
# ["Abhishek","manager","29","63000"]]

# data2=json.dumps(data1)
# print(data2)
# print(type(data2))

# fp=open("/home/ng/Desktop/Aarif_alam/JSON/8emp.txt","r")
# app1=fp.readlines()
# print(app1)
# app2=json.loads(app1)
# print(app2)
# print(type(app2))

# for  i in data1:
# fp.close()

# fp=open("/home/ng/Desktop/Aarif_alam/JSON/8emp.txt","r")
# app=fp.readlines()
# a=json.dumps(app)
# print(a)
# print(type(a))