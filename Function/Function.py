# print('Hello Function')

# def my_function():                 # here we are creating a fucntion
#   print("Hello from a function")


# def my_function():                   # Creating a function
#   print("Hello from a function")
# my_function()


# def my_function():               # Calling a function   
#   print("Hello from a function")     #To call a function, use the function name followed by parenthesis:

# my_function()
# * * * * *
# def moss():    # if we use positional Argument but in parameter we don't have Argument then it will give Error
#     print('dhinchak pooja')      # Error- take 0 positional argument but 1 was given
# moss(21)



# Arguments    * informations can be passed into function as arguments.
# def my_function(fname):
#   print(fname + " Refsnes")   

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
# # funtion work line wise but not in loop wise
# a=0
# def my_function(fname):
#   print(fname + " Refsnes")
#   print(a)

# # following three will take one by one with printing a
# my_function("Emil")   
# my_function("Tobias")
# my_function("Linus")

# a+=1 # function will not comes to this increment because it is not called in function

# my_function(a=1) # if this will take then coms Error   * function got an unexpected keyword argument 'a'



# Parameter or Arguments
#   * a Parameter is the veriable listed inside the parentheses() in the function defination.
#   * an Argument is the value that is sent to the function when it is called.
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# * * * Experiment * * *
# def my_function(fname, lname,jam):
#   print(fname + jam+"Hello Aarif "+jam+jam + lname+jam)

# my_function("Emil", "Refsnes",'12')


# If you try to call the function with 1 or 3 arguments, you will get an error:
# def my_function(fname, lname):        
#   print(fname + " " + lname)     # Error:  function is missing one argument of lname (parameter)

# my_function("Emil")


#   * * *  Number of Arguments   * * *
# By default, a function must be called with the correct number of arguments. Meaning that if your
# function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

#This function expects 2 arguments, and gets 2 arguments:
# def my_function(fname, lname):
#   print(fname + " " + lname)    # if here you use only one argument then you also het one output

# my_function("Emil", "Refsnes")           # if here you will you use one argument then you wil get Error-  1 argument is missing



# Arbitrary Arguments, *argsArbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name:

# def my_function(*kids):      # # * * * Arbitrary Arguments are often shortened to *args in Python documentations.
#   print("The youngest child is " + kids[0])    
# my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
# You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# we can't use int,set, tuple, list, dictionary. it will give Error. because diffent type will not Add.
# my_function(child1 = "Emil", child2 = "Tobias", child3 = ["Linus"])    



# * * * Arbitrary Keyword Arguments, **kwargs * * * #
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
# def my_function(**kid):
# #   print("His last name is " + kid["lname"])
#   print("His last name is " + kid['ArRa'])             # Error- KeyError: 'ArRa'      because key is not in argument
# my_function(fname = "Tobias", lname = "Refsnes")


# Default Parameter Value
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()          # if we wants to use in empty function call then we have to this form, to not get Error
#                         # it will put the value in default 
# my_function("Brazil") 



# * * * for addition method with using of Argument. * * * #
# * * * * * * 
# def Aarif(a,b):
#     c=a+b
#     print(c)
# Aarif(1,5)          # in this calling we are giving value of each argument of one value of it's position.
# * * * * * *
# def Aarif(a,b):
#     c=a+b
#     print(c)
# a=int(input())
# b=int(input())
# Aarif(a,b)     # we take input but it will exicut only once, because second call will exicute the first input. 
# Aarif(a,b)     # here we are two times with aruments have their input.
# * * * * * *
# def Aarif(a,b):
#     c=a+b
#     print(c)
# a=int(input())
# b=int(input())
# Aarif(a,b)        # now it will ask for two times because here we are giving input for exicute the function
# a=int(input())
# b=int(input())
# Aarif(a,b)

# def aarif(a,b):
#     a=2        # here the values of parameter will be change because we are assining new veluis.
#     b=3        # * * * value of parameter inside the function are Local values
#     total=a+b
#     print('Total',total)
# x=10       # out-side's values all are Globle.
# y=20
# aarif(x,y)

# * * * * * * Default Argument * * * * * * #
# * * * * * *
# def add(a,b,c):
#     print()
# add(1,2,3)      # here if we will not give same amount of values like Arguments then it will give Error
# add(1,2)       # add() missing 1 required positional argument: 'c'  
# * * * * * *
# def add(a,b,c=5):
#     print()
# # add(1,2)      # first way to write because c have already default value
# add(1,2,3)  
# second way to write because if we take value of those who have default value then default value will be *Null*


# def add(a,b,c,e=50):
#     print()
# # add(1,2)      # first way to write because c have already default value
# add(1,2,3,100)




# * * * * * * pasing a list as an Argumemt * * * * * * #
# You can send any data types of argument to a function (string, number, list, dictionary etc.), 
# and it will be treated as the same data type inside the function.

# fruits = ["apple", "banana", "cherry"] # in this position function will not accept list.
                                       # error- take 0 positional arguments but 1 was given.
# def my_function(food):
#   for x in food:
#     print(x)

# #fruits = ["apple", "banana", "cherry"]    # it will accept, without Error function will run

# my_function(fruits)
# fruits = ["apple", "banana", "cherry"]     # it will not go to this list




# * * * Return Values * * * #

# To let a function return a value, use the return statement
# def my_function(x):
#   return 5 * x              # after using return it will goes to caller3
# #   return 5 + x
# #   return 10/x            # Return function is for calling the function
#     # return x * 5      #A return statement ends the execution of a function, and
# print(my_function(3))   #  returns control to the calling function
# print(my_function(5))
# print(my_function(9))

# def hero(a,b):
#     result=a+b

#     return result           # it will not print the next  print function  
#     print('world')

# a=hero(3,3)
# print(a)


# * * * * * *return And print
# * * * * * *why we use return in fuction.    
# * * * * * *what is difference b/t return and print.   #Printing and returning are completely different 
                                                        # concepts. print is a function you call. When a 
                                                        # return statement is reached, Python will stop the
                                                        # execution of the current function, sending a value 
                                                        # out to where the function was called. Use return when
                                                        # you want to send a value from one point in your code
                                                        # to another.
# * * * * * *lamda function
# * * * * * *globle veriables and local veriables



# def ram(a,b):
#     mlti=a*b
#     print('hero')
#     return 

# ra=ram(2,4)
# print(mlti)
# print(ram(2,4))
# def ram():
#     for i in range(1,11):
#         print(i)
#         # return       # after using return it goes to the caller
# print('i m Don')
# # a=ram()
# print(ram())
    





# * * * The "Paas statement" * * * #

# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
# def myfunction():
#   pass





# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#                     L A M B D A   F U N C T I O N 
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

# A lambda function is a small anonymous function.
# * * * A lambda function can take any number of arguments, but can only have one expression. * * *


# SYNTEXT
# lamda arguments : expression


# EX- Add 10 to argument a, and return the result:
# x = lambda a : a + 10
# print(x)     
# print(x(5))      
# print(x(x(x(5))))
# print(x())
# print()


# EX- Multiply argument a with argument b and return the result:
# x = lambda a, b : a * b      # we can't this- x = lambda (a, b) : (a * b)
# print(x(5, 6)) # we can't take Argument in any Array like list, tuple etc.


# EX- Summarize argument a, b, and c and return the result:
# x = lambda a, b, c : a + b + c     # we can take lots of Arguments but not Expression.
# x = lambda a, b, c : a + b + c, a+b+c     # Error- 'a' is not defined
# print(x(5, 6, 1))


























# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#                                          M E R A K I
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 
# print ("NavGurukul")

# def say_hello():
#     print ("Hello!")
#     print ("Aap kaise ho?")

# say_hello()
# print ("Python is awesome")
# say_hello()
# print ("Hello…")
# say_hello()





# Question 1

# Question 1 (Part 1)
# "ask_question" naam ka Ek function likhiye jo yeh text ko "ek baar" print kare.
# Fir iss function ko 5 baar call kar ke yeh text 5 baar print karvao.
# def ask_question():
#     print('ek baar')
# ask_question()
# ask_question()
# ask_question()
# ask_question()
# ask_question()

# Question 1 (Part 2)
# Fir while loop ka use kar ke iss function ko 100 baar call karne ka code likho.
# Dono parts ka code ek hi file mein likh ke upload karo!
# def ask_question():
#     print('ek baar')
# for i in range(0,100):
#     ask_question()


# Q1 . Aapko max function ka use krke di hue list me se sbse bada value print krvani hai. Input
# numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# def arra():
#     print(max(numbers))
# arra()


#  Q2. Aapko sum function ka use krke di hue list ke element ka sum print krvana hai. Input
# numbers = [1, 2, 3, 4, 5] 
# def number(list1):
#     c=0
#     for i in list1:
#         c+=i
#     print(c)
# number(numbers)


# Q3. Aapko sort function ka use kr ke di hue list ko sort krna hai. Input:- 
# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15] 
# def arra(list1):
#     list1.sort()
#     print(list1)
# arra(unorder_list)


# Q4. reverse function ka use kr ke aapko di hue list ka revrse print krna hai. Input:-
# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"] 
# def arra(list1):
#     list1.reverse()
#     print(list1)
# arra(reverse_list)


# Q5. Aapko min function ka use krke di hue list me se sbse chhoti value print krvani hai. Input:- 
# list2 = [8, 6, 4, 8, 4, 50, 2, 7] 
# def arra(list1):
#     a=min(list1)
#     print(a)
# arra(list2)



# * * * * * * D E B U G    C O D E * * * * * *

# Question 1 
# def sum()                            # Here is (:) missing
#     print(12+13)
# sum() 


# Question 2
# daf welcome():                   # here we forgot to use (def)
#     print("Welcome to function")
# welcome() 


# Question 3
# isEven()           # Here we are (Calling function) but in wrong line.
# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number") 


# # Multiple Function Arguments
# def add_numbers(number1, number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(num_x, name)  # here it will give Error- int and str cn't be concatenate.


# * * * * * * *  * M U L T I    T A S K I N G

# Question 1
# def greet(names):         # here we have to use (*) befofe parammeter
#     for name in names:
#         print("Welcome", name)
# greet("Rinki", "Vishal", "Kartik", "Bijender") 


# Question 2 
# def info(name, age = ):                # here we have to give default value
#    print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18") 


# Question 3
# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
# studentDetails("Nilam","loop")   # here is misiing one argument



# * * * * * * C O D E * * * * * * * *

# Question 2
# function_print_lines naam ka ek function likho jo 2 strings leta ho,aur unko neeche diye 
# hue dhang se print karta ho. Jaise agar hum usko"Mera naam Rishabh hai." aur
# "Main NavGurukul ka co-Founder hun." denge toh woh yeh print karega
# def function_print_lines():
#     print('Mere naam Rishabh hai')
#     print('Main NavGurukul ka co-Founder hun.')
# function_print_lines()


# Question 3
# Question 3 (Part 1)
# Apko students naam ka ek function define karna hai or uss function mai list of students name as a 
# parameter pass karna hai(List ka use nahi karna hai)
# def students(*list_of_students):
#     for i in list_of_students:
#         print(i)
# students('kamal','rohan','gagan')

# Question 3 (Part 2)
# Apko isGreaterThen20 naam ka function define karna hai jismai apko function mai do parameter
# pass karane hai or first parameter by default 20 hi hona chahiye.
# def students(list_of_students,hero=20):
#     print(list_of_students,hero)
# students('kamal')


# Question 4
# Yeh question 2 parts mein hai. Dono parts ka code same file mein likh ke submit karein.

# Question (Part 1)
# add_numbers naam ka function likhiye jo do numbers ko arguments ke tarah le aur fir unka sum print karta hai.
# Arguments ka naam number1 aur number2 hona chaiye. Input :-
# num1 = 56
# num2 = 12
# def add_numbers(num1,num2):
#     print(num1+num2)
# add_numbers(num1,num2) 

# Question (Part 2)
# add_numbers_list naam ka function likhiye jo do integers ki 2 lists leta ho aur fir same position 
# wale integers ka sum print karta ho. Same position waale 2 integers ka sum karne ke liye Part 1 mein
# di gayi add_numbers waale function ka use karo. Jaise agar hum iss function
# ko [50, 60, 10] aur [10, 20, 13] denge ko woh yeh print karega
# list1=[50, 60, 10] 
# list2= [10, 20, 12]
# def misti(a,b):
#     for i in range(len(list1)):
#         c=0
#         c=a[i]+b[i]
#         print(c)
# misti(list1,list2)


# Question 5
# Yeh question 2 parts mein hai. Dono parts ka code same file mein likh ke submit karein.

# Question (Part 1)
# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain" 
# agar dono numbers even (2 se divide hote hain) nahi toh print kare "Dono numbers even nahi hai"
# def check_numbers(a,b):
#     if a%2==0 and b%2==0:
#         print('both are Even numbers')
# number1=int (input('enter you 1st num  '))
# number2=int(input('enter your 2nd num  '))
# check_numbers(number1,number2)

# Question (Part 2)
# Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko arguments ki tarah
# le aur fir check kare ki same index waale dono integers even hain ya nahi. Yeh check karne keliye
# pichle Part 1 mein likhe check_numbers function ka use karo. Agar aapne apne function ko 
# [2, 6, 18, 10, 3, 75] aur [6, 19, 24, 12, 3, 87] Toh usko yeh output deni chaiye:
# list1=[2, 6, 18, 10, 3, 75]
# list2=[6, 19, 24, 12, 3, 87]
# for i in range(len(list2)):
#     def check_numbers_list(a,b):
#         if a%2==0 and b%2==0:
#             print('both are Even numbers')
#         else:
#             print('not')
#     check_numbers_list(list1[i],list2[i])



# * * * * * * * * * * * * * * * R E T U R N  method * * * * * * * * * * * * * * * * * * * * * *

# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum      # if we will not use return method then after finishing of function it wii not go to
# sum1 = add_numbers(20, 40) #'sum1' veriable. it's mean that value can't be assine, it will give print() "None".
# print (sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print (sum2)
# print (sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print (number_a) 


# # here is also happning same and it never take those witch are comes after Return method
# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print ("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x               # *   it will not take 
#     print ("Kya main yahan tak pahunchunga?")      # *
#     return number_sum                              # *

# sum6 = add_numbers_more(100, 20) 


# * * * FOOD MENU * * * Using of Return method in every statements
# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"

#     print ("Kya main print ho payungi? :-(")

# mon_menu = menu("monday")
# print (mon_menu)
# tues_menu = menu("tuesday")
# print (tues_menu)
# fri_menu = menu("friday")
# print (fri_menu) 

# * * * FOOD MENU * * * Using of Return method in LAST statements 
# def menu(day):
#     if day == "monday":
#         food = "Butter Chicken"
#     elif day == "tuesday":
#         food = "Mutton Chaap"
#     else:
#         food = "Chole Bhature"
#     print ("Kya main print ho payungi? :-(")
#     return food
#     print ("Lekin main toh pakka nahi print hounga :'(")
# print(menu("monday")) 


# Question 6 
# part-1    make calculetre wuth 2 parameters. Use Add, subtract, multiply, devide
# def cal(a,b):
#     choose=input('what you want. +, -, *, /')
#     print(num1+num2) if choose=='+' else print(num1-num2) if choose=='-' else print(num1*num2) if choose=='*' else print(num1/num2)         
# num1=int(input('enter    '))
# num2=int(input('enter    '))
# cal(num1,num2)


# part-2      use 4 call
# def cal(a,b):
#     choose=input('what you want. +, -, *, /')
#     print(num1+num2) if choose=='+' else print(num1-num2) if choose=='-' else print(num1*num2) if choose=='*' else print(num1/num2)         
# num1,num2=int(input('enter    ')),int(input('enter    '))
# cal(num1,num2)
# num1,num2=int(input('enter    ')),int(input('enter    '))
# cal(num1,num2)
# num1,num2=int(input('enter    ')),int(input('enter    '))
# cal(num1,num2)
# num1,num2=int(input('enter    ')),int(input('enter    '))
# cal(num1,num2)


# part-3    we 2 lists same index of values we have to multipy and make new list 
# list1=[5, 10, 50, 20]
# list2=[2, 20, 3, 5]
# list3=[]
# for i in range(len(list1)):
#     def num(a,b):
#        multi=a*b 
#        return multi
#     c=num(list1[i],list2[i])
#     list3.append(c)
# print(list3)


# * * * * * * * * * * * * Python Inner Functions * * * * * * * * * * #
# those function which we use in another function is called inner function and nested function

# 1 
# def f1():
#    s = "I Love Aarif alam"
#    def f2():
#        print(s)
#    f2()

# f1() 

# 2
# def first_function():
#     s = 'I love Aarif alam'
#     def second_function():
#         print(s)     
#     second_function()
# first_function() 

# 3
 
# def first_function():
#     s = 'I love India'         # this is a local function
#     def second_function():
#         s = "MY NAME IS JACK"   # this is also a local function
#         print(s)     
#     second_function()
#     print(s)     
# first_function()


# Question 1
# eligible_for_vote name ka function likho jo ki user ko bataye ki vo (he/she) vote de sakta hai ya nahi.
#  ( Consider minimum age of voting to be 18. ) Example:- Agar user input me 18 se kam deta hai to 
# “not eligible“ print kare aur agar user 18 ya 18 se jyaada input kare to “you are eligible” print kare.
# def eligible_for_vote(a):
#     if a<18:
#         print ( 'you are not eligible')
#     else:
#         print('you are eligible')
# age=int(input('enter your age    '))
# eligible_for_vote(age)


# Question 2
# Ek perfect() naam ka function define kijiye jo ki ek parameter lega aur uss parameter ko hume check karana 
# hai ki vo perfect number hain ya nahi. Iske baad uss function ko use karke ek program likhiye jo ki 1 se 
# 1000 tak sabhi perfect numbers ko print kare.[ hum ek aise integer number ko perfect number kahenge jo ki 
# uske sabhi factors ( including 1 & excluding itself) ka sum uss number ke barabar hota hai. 

# def perfect(a):
#     c=0
#     for i in range(1,a):
#         if a%i==0:
#             c+=i
#     if c==a:
#         print('perfect number')
#         return c
#     else:
#         print("it is not perfect number")
# num1=int(input('enter your nummber   '))
# print(perfect(num1))

# for j in range(2,1001):
#     def perfect(a):
#         c=0
#         for i in range(1,a):
#             if a%i==0:
#                 c+=i
#         if c==a:
#             print(c)
#     perfect(j)


# Question 3
# Ek function banaiye jo 3 numbers ka sum aur average print kare.Hum user se 3 number input karwayenge
# aur fir unn 3 numbers ka sum aur average print karwayenge jaisa ki niche output diya hua hain.
# def number(a,b,c):
#     sum=a+b+c
#     print(sum)
#     ave=sum/3
#     print(ave)
# num1=int(input('enter your number'))
# num2=int(input('enter your number'))
# num3=int(input('enter your number'))
# number(num1,num2,num3)


# Question 4
# Ek showNumbers() naam ka function define kijiye jo ki ek limit naam ka parameter lega aur 0 se limit tak ke 
# beech ke sabhi even aur odd numbers ko label ke saath print karega jaisa ki niche dikhaya gaya hai
# def showNumbers(limit):
#     for i in range(1,limit):
#         if i%2==0:
#             print('Even number    ',i)
#         else:
#             print('Odd number    ',i)
# num=int(input('enter your no    '))
# showNumbers(num)


# Ek function define kijiye jo ki drivers ki speed check karega. Aur ye function speed naam ka ek parameter lega. 
# 1. Agar speed 70 se kam hai to ye “ok” print karega.

# 2- Agar driver ki speed 70 se jyaada hai to function use har 5 km ke liye 1 point dega
#    (ye 70 ko count nahi karega).
#    example ke liye agar speed 80 hai to print karega “points:2” .

# 3- Agar driver ko 12 points se jyaada points milte hai to , function “License suspended” print karega.
# def limit(a):
#     if a<70:
#         print('OK')
#     else:
#         b=a-70
#         c=b//5
#         if c>=12:
#             print('Licence suspended')
#         else:
#             print('you are crossed the limit of 70km/hr    -' ,a)
# speed=int(input('enter your speed   '))
# limit(speed)


# Question 7
# Ek function define karo jo ki input me 2 strings lega aur dono strings me se jiski length jyaada hogi use
# print karega aur agar dono strings ki length equal hui to dono ko line by line print karega .
# def string(a,b):
#     if len(a)>=len(b):
#         print(a)
#     if len(b)>=len(a):
#         print(b)
# str1=input('enter your word    -')
# str2=input('enter your word    -')
# string(str1,str2)


# Question 8
# Ek function likho jo ki ek argument le jo number ho or dictionary return karega jisme keys 1 se lekar 
# argument ke number tak hogi aur values unke squares honge.jaisa ki niche dikhaya gaya hai.
# def func1(a):
#     dict1={}
#     for i in range(1,a+1):
#         dict1[i]=i**2
#     print(dict1)
# num=int(input('enter your number   -'))
# func1(num)


# * * * * * * * * * * *  C O D E      O U T P U T   * * * * * * * * * * * * * * * *

# Question 2
# Niche diye gye code snippet ki output kya hogi? 
# def primeorNot(num):                                 #    Prime number
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break                              # this is wrong code of Prime number
#             else:
#                 print(num,"is a prime number")
#     else:
#            print(num,"is not a prime number")
# primeorNot(406)


# Question 3
# Niche diye gye code snippet ki output kya hoga?
# def greet(*names):
#     for name in names:
#                print("Hello", name)      # it will all positional arguments
# greet("sonu", "kartik", "umesh", "bijender")


# Question 4
# Niche diye gye code snippet ki output kya hoga?
# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10      #######################################################################
#     return sum
# print(sumofdigits(123))


# Question 5
# Niche diye gye code snippet ki output kya hogi?
# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice" # we can't use default here because default wiil not allow other rather then lunch
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner"    :
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))


# * * * * * * * * * * * * * * * D E B U G  the  Code  * * * * * * * * * * * * * * * * * * * * * *
# Question 1
# Neeche diye huye codes mai kuch bugs hai. Ab aapko error find kar ke unhe solve karne hai.(number of bugs) 

# def calculate_sum(a,b):
#     sum = a+b 
#     print(sum) 
# sum(4,5)           # here we have to call "calculate_sum  " 


# Question 2
# Neeche diye huye codes mai kuch bugs hai. Ab aapko error find kar ke unhe solve karne hai.(number of bugs)
# function_multi(a,b):        # here we have to define with "def"
#     multiply=a*b
#     return multiply
# print(function_multi(3,4)) 


# Question 3
# Neeche diye huye codes mai kuch bugs hai. Ab aapko error find kar ke unhe solve karne hai.(number of bugs)
# Def Avg(number1,number2,number3):       # here we have to define proper way using of "def"
#     avg=number1+number2+number3/3
#     print(sum)
# Avg(1,3,2)
 

# Question 4
# Neeche diye huye codes mai kuch bugs hai. Ab aapko error find kar ke unhe solve karne hai.(number of bugs) 
# def voter(age):
# if age < 18:               # wrong indentaion
#     print("eligible")
# else:
#     print("not eligible")
#     voter(20)


# Question 5
# Neeche diye huye codes mai kuch bugs hai. Ab aapko error find kar ke unhe solve karne hai.(number of bugs)
# def distance(kms):
#         if kms < 20:
#             print("close")
#         elif kms < 50:
#             print(median)                # in print() we have to use in (" ") quotes
#         else:
#             Print(far)                   # in print "p" is capital & in print() we have to use in (" ") quotes
#     distance(20,30)             # here is it have wrong indentation 


