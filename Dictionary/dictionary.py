print('Dictionary in python')


#   ***  Dictionary is like only colletion of Data. it have key with pare of valus.
# think that Key is our Room and valus are childrens in the room. if we change the room's position th3

# a={'Ar':[1,3,42],'Ra':[345,75,24]}         # Dictionary is in the set thats why key don't have index. *** 
# print(a[0][1]) 


# a={'a':[123,21,90],'b':['dkh','kb','efg'],'a':['ety','yg','fh']}       # Duplicates are not allow 
# print(a)                                                      # ***  It will take the  LAST one Duplicate.


# a={'Ar':[1,3,42],'Ra':[345,75,24]}          #  For key We have to use object's name (kay's name)
# print(a['Ra'][1])                   # indexing is allow only for Values, when values in *** (LIST, TUPLE) ***


# a={'Ar':[1,3,42],'Ra':[345,75,24]}         #  length of Dictonary
# print(len(a))


# a={'Ar':[1,3,42],'Ra':[345,75,24]}                   #    TYPE      ***      <class 'dict'>      ***    #
# print(type(a))


# a={'Ar':[1,3,42],'Ra':[345,75,24]} 
# # print(a['Ar'])                        #  inside square bracket referring the name of the key.
# print(a.get('Ar'))              # There is another way, with using of *** get()*** 
# print(a.get('Ar')[2])



# a={'Ar':[1,3,42],'Ra':[345,75,24],'ArRa':36}    #  ***
# print(a['Ar'])
# print(a.keys()) 

# b=list(a.keys())  ###  this two have lots of diffence    it here we can't use indexing
# print(b)          ###  but in this we can use indexing and get perticular key.
   
# print(len(b))
# for i in b:
#     print(i)


#    Keys()   from this method we can get all keys.
# print(a.keys())  


# Change the valuse    or we can also ADD  ***           from this method we can add
# a['soul']='mate' 
# print(a)


#  UPDATE   ***   this is use for to Update your Dictionary

# a.update({'Ra':999})          # here is changing the value of Dictionry
# print(a)

# a.update({'Aarif':666})       # here is Adding one pair of key:value
# print(a)

#  * * * * * * * * * * * * * * * * * * *   Another way
# a['Ar']='soul'       #  changed item
# print(a)

# a['soul']='mate'      # changed items with pair of Keys
# print(a)


# Get  VALUE 


# #    POP   ***      pop acpected atleast 1 argument
# b=a.pop('Ar')        #  *****    it will remove, what argument you give
# print(a.pop('Ar') )
# print(a)
# print(a)  
# print(b)         #   ***   it can be Store in veriable...


#   DEL ***     del is use for to delet element of dictionary or you can delet whole dictionary

# del a["Ar"]     #     items       #  in Argument it take the object.
# print(a) 

# print(a)          #  here we are eleting whole dictionary  and here gives Error while printing 
# del a
# print(a)


#   CLEAR ***         clear()  method clear the dictoinary.
# a.clear()
# print(a)                 #   it will give us empty dictionary



#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

# dict1={'Ar':3,'Ra':6,'ArRa':9,'soul':12,'mate':18}

#  Accesing    *** KEYS ***              
# for i in  dict1:
#     print(i)

#  Accesing    *** values ***
# for i in dict1:
#     print(dict1[i])
 
# use *** Values() *** method 
# for i in dict1.values():
#     print(i)

# use *** Keys() ***  method
# for i in dict1.keys():
#     print(i) 

# use *** items() *** method
# for i, j in dict1.items():            ***
#     print(i, j)
# for i in dict1.items():               # if we use 1 veriable for iteration.
#     print(i)

# use  *** copy() ***   this method is use for to copy dictionary.

#  *** if we use b==a then here a is not assinig to b . if we will change in *** a *** then it will also change into *** b ***

# dict2=dict1.copy()
# dict1.clear()
# print(dict2)

# dict2=dict(dict1)
# dict1.clear()
# print(dict2)


# Nested list

# a={1:{'A':'ArRa'},2:{'B':'RaAr'}}                         #  first way
# print(a)1234

# a={1:'Aarif',2:'Rahul',3:'Pinku',4:'Akash',5:'Vivek'}       # Second way
# b={1:'Aarif',2:'Rahul',3:'Pinku',4:'Akash',5:'Vivek'}
# c={1:'Aarif',2:'Rahul',3:'Pinku',4:'Akash',5:'Vivek'}
# dict1={'a':a,"b":b,"c":c}
# print(dict1)


#   fromKeys()  method return a ditionry with specified Key with specified Values
# a=(1,2,3)
# b=0
# b=(0,)
# Aarif=dict.fromkeys(a,b)        #   if we use b as int for Values
# print(Aarif)
# Aarif=dict.fromkeys(b,a)      #   if we use b as tuppel for Keys
# print(Aarif)


#   *******************   setdefault()    method is use to find your correct values if you assine wrong default
# dict1={'Ar':3,'Ra':6,'ArRa':9,'soul':12,'mate':18}
# a=dict1.setdefault('Ar',36)          #  if we use key of this dict1 nad give wrong value then it will give correct values
# print(a)
# print(dict1)

# print(dict1.setdefault('AR',3))      # if we use wrong Key with the values then it will append it in dictionary 
# print(dict1)

# print(dict1.popitem())   #  this method remove a element from your dictionary
# print(dict1)





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# * * * * * * * * * * * * * * * * * * * * * *    M E R A K I     * * * *  * * * * * * * * * * * * * * * * * * * * * * * * 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 1  KEY case sensitive
# city_population = {
#     "NewYorkCity":8550405,
#     "newyorkcity":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population)) 

# 2  dict() function 
# a=dict(name="Aarif",classs='A class')
# print(a)

# 3  Keys() method

# 4 values() method

# 5 Nested Dictionary
#   change value of nested dictionary
# a={1:{'A':'ArRa'},2:{'B':'RaAr'}}                  #   very Important.
# a[1]['A']='SubhanAllah'
# print(a)
# a[1].update({'a':'Aarif'})
# print(a)

# 6   Iteration  
 
# movie ={
#     "name":  "Puli",
#     "hero":  "Vijay",
#     "rating":  7.5
#     }
# for x,y in movie.items():
#     print(x,y)



# 1 Ek program likhiye jisse ki niche di hui dictionaries ek hi dictionary me aa jaayejaise ki niche Expected result me diya gaya 
# hain or jisski bhi keys same hai unki values add ho jai.
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}

# dic1.update(dic2)         # first way  but in this value of 2 will only one value which wiil be come in last
# dic1.update(dic3)       
# print(dic1)


# 2 Ek program likhiye jisse ki agar di hui key pehle se dictionary me exist karti ho toh “exists “ print kare
#   aur agar nahi karti ho toh “not exists” print kare.
# a={1:{'A':'ArRa'},2:{'B':'RaAr'}}
# if 'name' in a:
#     print('exist')
# else:
#     print('not exist')


# 3 Ek program likhiye jo ki dictionaries ki values ka sum print kare.
# my_dict = {
#         'data1':100,
#         'data2': -54,
#         'data3': 247
#        } 
# a=0
# for i in my_dtict:
#     a+=my_dict[i]
# print(a)


# 4 Ek program likhiye jo ki nested dictionary me se first key or value ko remove kare.
# Aarif={1:{'a':'Aarif','b':'Aarif'},2:'AaRa',3:{'a':'Aarif','b':'Aarif'}}
# for i in Aarif:
#     a=1
#     if type(Aarif[i])==dict:                   ########################################
#         print("<<>")                           ########################################
#         for j in Aarif[i]:                     ########################################
#             if a==1:
#                 print('<<<')
#                 Aarif[i].pop(Aarif[i][j])
#                 print(Aarif.pop(Aarif[i][j]))
#                 a+=1
# print(Aarif)

    
        
# 5 Do lists lekar ek dictionary banaiye jisme pehli list ke elements keys ho aur dusri list ke elements unn keys ki values ho

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,] 
# dict1={}
# for i in range(0,5):
#     dict1[list1[i]]=list2[i]
# print(dict1)



# 6 Ek program likhiye jo dictionary me se duplicate keys hata de.
 
# dict1={
#     'ball':'red',
#     'bat':4,                      ###################################################
#     'wickets':8,                  ####################################################
#     'ball':'green',              ######################################################
#     'bat':3
#     } 
# for i in dict1:



# 7 Ek list lijiye aur uske andar dictionaries me keys and values likhiye jaisa ki niche dikhaya gaya hai 
#   aur uske baad saare unique values ko ek list me print karaye. 
# list1=[{"first":"1"}, {"second": "2"},  {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}] 
# a=[]
# for i in list1:
#     print(i)
#     b= list(i.values())
#     print(b)
#     for j in b:
#         print(j)
#         if j not in a:
#             a.append(j)
# print(a)


# 8 User se 10 students ke naam aur marks lekar unhe ek dictionary me store karaye.
# ***  Direct  ***
# dict1={}
# list1=[['Aarif',99],['Akash',99.9],["Pinku",98],['Rahul',98],['Vivek',98],['Ritik',96],['Raju',80],['Rajnish',61],['Abhishek',72],['life-ji',100]]
# for i in list1:
#     dict1[i[0]]=i[1]
# print(dict1)

# ***  Input  ***
# dict1={}
# students=int(input('How many students   -'))
# for i in range(0,students):
#     name=input("Enter student's name   -")
#     marks=int(input('enter his marks   -'))
#     dict1[name]=marks
# print(dict1)



# 9 "MISSISSIPPI" iss word me har letter ki occurrency count karke ek dictionary me store karaye.
#    Jisme letter dictionary ki keys aur occurrency Uss dictionary ki values hongi.
# str1="MISSISSIPPI"
# list1=[]
# list2=[]
# dict1={}
# for i in str1:
#     list2.append(i)
#     if i not in list1:
#         list1.append(i)
# print(list1)
# print(list2)
# for i in list1:
#     a=0
#     for j in list2:
#         if i==j:
#             a+=1
#     dict1[i]=a
# print(dict1)



# 10 Ek dictionary ki value ke sabhi items ko count kijiye jo ki ek list me hai.
# dict1={'Aarif':[1,2,3,42,4,3,26,7372,],'life-ji':[324,2423,24]}
# a=0
# for i in dict1:
#     # print(dict1[i])
#     for j in dict1[i]:
#         # print(j)
#         a+=1
# print(a)


# 11 Ek code likhiye jo dictionary ki 3 highest value print karaye
# dict1={'Aarif':[122,412,535,35,263,2,6516,16,15,],'life-ji':[1233,4,42,4,1,4,4,1,1,3123,]}
# list2=[]
# for j in dict1:
#     list1=dict1[j]
#     i=0
#     c=0
#     list3=[]
#     while i<len(list1):
#         if c<3:
#             b=max(list1)
#             list3.append(b)
#             list1.remove(b)
#             i=0
#             c+=1
#         i+=1
#     list2.append(list3)
# print(list2)


# 12 Ek program likhiye jo:- Ek dictionary me 1 se 15 tak saare numbers ki keys banaye aur unke square unn keys ki values ho.
# dict1={}
# for i in range(1,16):
#     dict1[i]=i**2
# print(dict1)


# # thirteenth  Ek code likhiye jo dictionary ki 3  key  jinki highest value ho, key print karaye.
# dict1 = {
#     'a':50, 
#     'b':58,
#     'c': 56,             
#     'd':40,              
#     'e':100,             
#     'f':20
#     } 
# list1=list(dict1.keys())
# list2=list(dict1.values())
# i=0
# list3=[]
# while i <len(list2):
#     a,j=max(list2),0
#     while j < len(list2):
#         if a==list2[j]:
#             list3.append(list1[j])
#             list2.pop(j)
#             list1.pop(j)    
#         j+=1
#     i+=1
# print(list3)



# 14 Ek program likho jo ki dictionaries ki values ko sort(ascending or descending) kar de
# dict1={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}

# dict1=sorted(dict1.items())              # 1st Way
# print(dict1)
# list1=[]
# dict2={}
# for i in range(0,len(dict1)):
#     list1.append(dict1[i][1])
# list1.sort()                                                #  Asending
# # list1.sort(reverse=True)                                  #  Disending
# for j in range(0,len(list1)):
#     for k in dict1:
#         print(k[1])
#         if list1[j]==k[1]:
#             dict2[k[0]]=k[1]
# print(dict2)

# b=sorted(dict1.values())             # 2nd Way
# print(b)
# dict2={}                                                     # Asending
# # b.reverse()                                                # Disending
# for k in range(0,len(b)):
#     for i ,j in dict1.items():
#         if j==b[k]:
#             dict2[i]=j
# print(dict2)



# 1 what you will get in print() , error or result.
# a={(1,2):2,(2,1):156}
# print(a(1,2))                                   # it will give Error because we are not assining the Key.
# print(a[1,2])                                   # it will give output becat we are assinig the key


# 2 Niche diye gye code snippet ki output kya hogi?
# a = {'a':1,'b':2,'c':3}                                   # give Error- because it cann't take more then one argument
# print (a['a','b']) 



# 3 Niche diye gye code snippet ki output kya hoga?
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1        
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print (len(fruit))
# print(fruit)


# 4 Niche diye gye code snippet ki output kya hoga?
# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print(Details["Student"])
# print(Details)
# print (len(Details["Student"])) 
 

# 5 Niche diye gye code snippet ki output kya hogi?
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print (sum)
# print(my_dict) 


# 6 Niche diye gye code snippet ki output kya hoga?
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates[box]))                # use  "box"        
# print(crates) 
# print(crates['box'])


# 7 Niche diye gye code snippet ki output kya hogi?
# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# print(id1)
# del rec

# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
#     }
# id2 = id(rec)
# print(id1 == id2)


#   * * * * * * * * * * * * * * * * * * * * * * D I B U G * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# 1 aapko ek dictionary di gai hai jisme aapko kuch key ki value print karani hai. Code ko debug karre do bug find karro.
 
# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }

# print(details["name"])
# # print(details["lastname"])   # thos key is not in Dict.
# # print(details[age])        #  KEY's type is Str so we have to use key in str
# print(details['age'])
 


# 2 aapko ek dictionary di gai hai jisme aapko sare key ka sum karna hai. Apko iss code mai dedugging
#   karni or pata karna hai ki aap output 14 kese la sakte ho.
# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     # sum=sum+1               # here is icreasing only one not dict1's values. use i
#     sum+=i
# print(sum) 


# 3 Niche ek program hai jisme keys 1 se lekar 15 ke beech main hai aur values keys ka square hai jaise ki.
#   Output kuch esha hona chahiye :- ab aapko is program ko theek karna hai.
# c=dict()
# for i in range(1,16):
#     # c=i*i              #   this is just increasing the valuse of c
#     c[i]=i**2
# print(c)  


# 4 aapko two dictionary di gai hai unhen aapko concatenate karna hai ab apko code ko
#   debug karna hai Aur aapka output aisa hona chahiye 
#   :- {'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56,'python':20,"gaurav":300,'dev':34,"karan":43} 
# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in s:
#     print(i)
    # update(i)         # wrong syntext
#        c.update(i)
# print(c)



# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#                            W3 School
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# # 1. Write a Python script to sort (ascending and descending) a dictionary by value. 
# dict1={"aarif":64,'Akash':73,'Rahul':43,'Pinku':76,'Vivek':49}
# list1=sorted(dict1.values())
# print(list1)
# # list1.reverse()                # use reverse() method for Disending
# c={}
# for g in list1:
#     for i,j in dict1.items():
#         if g==j:
#             c[i]=j
# print(c)


# 2. Write a Python script to add a key to a dictionary.
# dict1={0: 10, 1: 20}
# dict2={}
# items=list(dict1.values())
# print(items)
# a=items[0]
# for i in range(len(dict1)):
#     print(i)
#     for j,k in dict1.items():
#         if i==len(dict1)-1:
#             dict2[j+1]=k+a
#         else:
#             dict2[j]=k
# print(dict2)


# 3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor
# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50,6:60}
# Dict={}
# for i in (dict1,dict2,dict3):
#     Dict.update(i)
# print(Dict)


# 4. Write a Python script to check whether a given key already exists in a dictionary.
# dict1={"Aarif":34,'Anurag':36,'Akshay':36,'Satpal':38}
# a=int(input('enter 1 for int key or 2 for str key'))
# if a==1:
#     input1=(input('enter your int key          '))
# elif a==2:
#     input1=(input('enter your str key          '))
# if input1 in dict1:
#     print('exist   - ',input1)
# else:
#     print('not exist   - ',input1)


# 5. Write a Python program to iterate over dictionaries using for loops. 
# dict1={"Aarif":34,'Anurag':36,'Akshay':36,'Satpal':38}
# for i , j in dict1.items():
#     print(i,'->',j)


# 6. Write a Python script to generate and print a dictionary that contains
#    a number (between 1 and n) in the form (x, x*x).
# dict1={}
# input1=int (input('what end integer do you wants in your dictionary'))
# for i in range(1,input1+1):
#     dict1[i]=i*i
#     # dict1.update({i:i*i})
# print(dict1)


# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15
#    (both included) and the values are square of keys.

# * * * both are same * * *


# 8. Write a Python script to merge two Python dictionaries.
# dict1={'Aarif':1,'Akash':2,"Pinku":3,'Rahul':4,'Vivek':5}
# dict2={"Aarif":34,'Anurag':36,'Akshay':36,'Satpal':38}
# Dict={}
# Dict.update(dict1)
# # Dict=dict1.copy()              # her  we can also use Copy() method
# Dict.update(dict2)
# print(Dict)


# 9. Write a Python program to iterate over dictionaries using for loops.

# only use of  for loof to iterate key and value seperatelly simantesly.


# 10. Write a Python program to sum all the items in a dictionary.
# dict1={'Aarif':1,'Akash':2,"Pinku":3,'Rahul':4,'Vivek':5}
# c=0
# for i in dict1.values():
#     c+=i
# print(c)


# 11. Write a Python program to multiply all the items in a dictionary. 
# dict1={'Aarif':1,'Akash':2,"Pinku":3,'Rahul':4,'Vivek':5}
# c=1
# for i in dict1.values():
#     c*=i
# print(c)


# 12. Write a Python program to remove a key from a dictionary.
# dict1={'Aarif':1,'Akash':2,"Pinku":3,'Rahul':4,'Vivek':5}
# a=int(input('enter 1 for int key or 2 for str key'))
# if a==1:
#     input1=(input('enter your int key          '))
# elif a==2:
#     input1=(input('enter your str key          '))
# for i in dict1.keys():
#     if input1==i:
#         dict1.pop(i)
#         break
# print(dict1)


# 1three. Write a Python program to map two lists into a dictionary.
# list1=['Aarif','Akash','Pinku','Rahul','Vivek']
# list2=[1,2,3,4,5]
# dict1={}
# for i in range(0,len(list1)):
#     dict1[list1[i]]=list2[i]
# print(dict1)


# 14. Write a Python program to sort a given dictionary by key.
# dict1={"Aarif":34,'Satpal':38,'Anurag':36,'Akshay':36}
# list1=sorted(dict1.keys())
# print(list1)
# # list1.reverse()                # use reverse() method for Disending
# c={}
# for g in list1:
#     for i,j in dict1.items():
#         if g==i:
#             c[i]=j
# print(c)


# 15. Write a Python program to get the maximum and minimum value in a dictionary.
# dict1={"Aarif":34,'Satpal':38,'Anurag':36,'Akshay':36}
# # a=max(dict1.values())              #   Max value
# a=min(dict1.values())                #   Min value   
# print(a)


# 16. Write a Python program to get a dictionary from an object's fields.
# Aarif=12
# Akash=15
# Pinku=18
# Rahul=21
# dict1={}
# dict1['Aarif']=Aarif
# dict1['Akash']=Akash
# dict1['Pinku']=Pinku
# dict1['Rahul']=Rahul
# print(dict1)

# dict1={"Aarif":12,'Akash':{'Tigga':15},'Rahul':21,'Pinku':{'Sarkar':27}}   # *** EXTRA ***
# for i in dict1:
#     if type(dict1[i])==dict:
#         print(dict1[i])


# 17. Write a Python program to remove duplicates from Dictionary. 
# dict1={'di':{'Aarif':12},'d2':{'Akash':15},'d3':{'Pinku':18},'d4':{'Rahul':21},'d5':{'Aarif':12}}
# dict2={}
# for i,j in dict1.items():
#     if j not in dict2.values():
#         dict2[i]=j
# print(dict2)


# 18. Write a Python program to check a dictionary is empty or not.
# dict1={'Aarif':36}
# if dict1=={}:
#     print('dict1',dict1,' is empty')
# else:
#     print('dict1',dict1,' is not empty')


# 19. Write a Python program to combine two dictionary adding values for common keys.
# dict1 = {'a': 100, 'b': 200, 'c':300}
# dict2 = {'a': 300, 'b': 200, 'd':400}
# dict3={}
# set1=list(set(dict1).difference(set(dict2)))
# c=0                                             # Use of Dict(), Set(), List()
# for  i in dict2:
#     if i in dict1:
#         dict3[i]=dict1[i]+dict2[i]
#     else:
#         dict3[i]=dict2[i]
#         dict3[dict1[set1[c]]]=set1[c]
#         c+=1
# print(dict3)


# 20. Write a Python program to print all unique values in a dictionary.
# list1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# set1=set({})
# for i in range(0,len(list1)):  
#     set1.update(set(list1[i].values()))      # Set constructor, set, dic
# print(set1)


# 21. Write a Python program to create and display all combinations of letters,
#      selecting each letter from a different key in a dictionary. Go to the editor
# dict1={'1':['a','b'], '2':['c','d']}
# list1=dict1['1']
# list2=dict1['2']
# for i in list1:
#     a=''
#     for j in list2:
#         a=i+j
#         print(a)



# 22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
# dict1 = {
#     'a':50, 
#     'b':58,
#     'c': 56,             
#     'd':40,              
#     'e':100,             
#     'f':20
#     } 
# list1=list(dict1.keys())
# list2=list(dict1.values())
# i=0
# list3=[]
# while i <len(list2):
#     a,j=max(list2),0
#     while j < len(list2):
#         if a==list2[j]:
#             list3.append(list1[j])
#             list2.pop(j)                                                                                  
#             list1.pop(j)    
#         j+=1
#     i+=1
# print(list3)
    

# 20 third. Write a Python program to combine values in python list of dictionaries.
# list1=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# dict1={}
# for i in list1:
#     if i['item'] not in dict1:
#         dict1[i['item']]=i['amount']
#     else:
#         dict1[i['item']]=dict1[i['item']]+i['amount']
# print(dict1)






















# print("Ankit's challlenging Questions")
# # 1 Employe list change into dictionary
# len_employee=int (input('enter how many employee do you need'))
# dict1={}
# for i in range(0,len_employee):
#     dict2={}
#     name =input("Enter employee's name" )
#     age=int(input("Enter employee's age"))
#     sex=input("Enter employee's sex")
#     job=input("In which company employee do work")
#     dict2={'name':name,'age':age,'sex':sex,'job':job}
#     dict1[i+1,'employee']=dict2
# print(dict1)



# 2 In list you have iterate any date and without changing their charecter
# nested_list=int(input('enter how many neted lists do you wants'))
# list1=[]
# list_int=['1','2','3','4','5','6','7','8','9','0']
# c=0
# d=0
# for i in range(0,nested_list):
#     list2=[]
#     len_elements=int(input('enter how many elements do you need'))
#     for j in range(0,len_elements):
#         input1=input('enter yor input')
#         for k in input1:
#             if k in list_int:
#                 c+=1
#             elif k=='.':
#                 d+=1
#         if c==len(input1):
#             input1=int(input1)
#         elif d==1:
#             input1=float(input1)
#         list2.append(input1)
#     list1.append(list2)
# print(lisvt1)


# # 3 Roman numbers. In input we will give numbers and get roman numbers.
# dict1={1:'I',2:'II',3:"III",4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',
# 20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',100:'C',
# 200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',1000:'M',1001:'MI'}
# input1=int(input('enter your number   '))
# a=list(dict1.keys())
# output=''
# i=0
# c=0
# while i<len(dict1)+2:
#     max1=max(a)
#     if max1>input1:
#         a.remove(max1)
#     elif max1==input1:
#         output=output+dict1[max1]
#         input1=input1-max1
#         c+=max1
#     elif max1<input1:
#         output=output+dict1[max1]
#         input1=input1-max1
#         c+=max1
#     if c==input1:
#         break
#     i+=1
# print(output)


# Pascle Triangle 
# n=int(input('enter your lines how many lines do you want ?'))
# list1=[]
# for i in range(n):
#     list2=[]
#     for j in range(i+1):
#         if j==0 or j==i:
#             list2.append(1)
#         else:
#             list2.append(list1[i-1][j-1]+list1[i-1][j])
#     list1.append(list2)
# # print(list1)
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end='')
#     for j in range(i+1):
#         print(list1[i][j],end=' ')
#     print()


#   ankit done pascle in minimum lines
# for i in range(5):
#     c=1
#     for j in range(1,i+1):
#         print(c,end=" ")
#         c=c*(i-j)//j
#     print()







# suraj start from here
# rr,vv=0,0
# while rr<len(list1) and vv<len(list1):
#     print( str(list1[rr][vv]),end=" ")
#     vv+=1
#     if vv==len(list1[rr]):
#         print()
#         vv=0
#         rr+=1




# Amol,anmol={'aarif':12,'Akshay':24,'Satpal':36},{}

# for i in list(Amol.items()):
#     anmol[i[1]]=i[0]
# print(anmol)

# for i in list(Amol.keys()):
#     anmol[Amol[i]]=i
# print(anmol)

# for i in list(Amol):
#     anmol[Amol[i]]=i
# print(anmol)

# j=0
# for i in a:
#     anmol[a[j]]=Amol[i]
#     j+=1
# print(anmol)





# print(list(Amol.keys())[0])


# print(Amol['aarif'])
a={1:"Aarif"}
print(a)
print("i am lucky")