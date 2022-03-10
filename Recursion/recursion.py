# # print("hello Recursion")
# def tri_recursion(k):
   
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
  
# print("\n\nRecursion Example Results")
# tri_recursion(6)



# def xyz():
#     a=1
#     print("hello akshay pandey")
#     a=a+1
#     print(a)
#     xyz()
# xyz()

# def fibo(n):
#     if n == 1:
#         return 0
#     if n==2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# n=int(input("enter the number:-"))
# a=fibo(n)
# print(a) 


# def recall(a):
#     print(a)
#     recall(5)
# recall(1)


# 1 print the string in reverse order using recursion
# def xyz(s,n):
#     if n==0:
#         print(s[0]) 
#     else:
#         print(s[n],end='')
#         xyz(s,n-1)
# s=input('enter your word    = ')
# xyz(s,len(s)-1)


# 2 Programe to find x power y using recursion.
# def xyz (x,y):
#     if y==0:
#         return 1
#     else:
#         return x*xyz(x,y-1)
# x=int(input('enter your number     = '))
# y=int(input('enter your number'))
# z=xyz(x,y)
# print(z)


# 3 find GCD of two given numbers using recrsion.
# def gcd(p,q):
#     if q==1:
#         return 1
#     elif p%q==0:
#         return q
#     else:
#         return gcd(q,p%q)
# p=int(input('enter your number   = '))
# q=int(input('enter your your divisior number    = '))
# z=gcd(p,q)
# print(z)


# 4 find the factorial of your input.
# def xyz(n):
#     if n==1:
#         return 1
#     else:
#         return n*(xyz(n-1))
# n=int (input('enter your number    = '))
# z=xyz(n)
# print(z)



# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
#                                 W3  R E S O U R C E S
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# 1. Write a Python program to calculate the sum of a list of numbers.
# list1=[12,3,4,1,345,46,47,1]
# def func(list1):
#     if len(list1)==1:
#         return list1[0]
#     else:
#         return list1[0]+func(list1[1::])
# z=func(list1)
# print(z)


# 2. Write a Python program to converting an Integer to a string in any base
# def integer(a):
#     return str(a)
# a=int(input('enter your number     = '))
# print(integer(a))


# 3. Write a Python program of recursion list sum.
# list1=[1, 2, [3,4], [5,6]]
# def fnc(list1):
#     sum1=0
#     for i in list1:
#         if type(i)==list:
#             sum1=sum1+fnc(i)
#         else:
#             sum1=sum1+i 
#     return sum1
# print(fnc([1, 2, [3,4], [5,6]]))
       


#  4. Write a Python program to get the factorial of a non-negative integer
# def xyz(n):
#     if n==1:
#         return 1
#     else:
#         return n*(xyz(n-1))
# n=int (input('enter your number    = '))
# z=xyz(n)
# print(z)


# 5. Write a Python program to solve the Fibonacci sequence using recursion.
# def fibo(a,b,c):
#     if c<=z:
#         print(c,end=" ")
#         a=b
#         b=c
#         c=a+b
#         return fibo(a,b,c)
# z=int(input('enter your number    = '))
# fibo(0,1,0)


# 6. Write a Python program to get the sum of a non-negative integer.
# def sum1(a):
#     if len(a)==1:
#         return int(a[0])
#     else:
#         return int(a[0])+sum1(a[1::])
# num1=input('enter your number     = ')
# print(sum1(num1))


# 7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
# def sum_series(a):
#     if a==2:
#         return 2 
#     elif a==1:
#         return 1
#     else:
#         return a+ sum_series(a-2)
# a=int(input('enter your number    '))
# z=sum_series(a)
# print(z)


# 8. Write a Python program to calculate the harmonic sum of n-1. Go to the editor
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# 1 + 1/2 + 1/3 + 1/4 + 1/5
# def harmo(a):
#     sum=0
#     if a==1:
#         return 1
#     else:
#         return 1/a + harmo(a-1)
# num1=int(input('enter your number    = '))
# print(harmo(num1))


# 9. Write a Python program to calculate the geometric sum of n-1. Go to the editor
# Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.
# 1/2 + 1/4 + 1/8 +........1/n
# def geometric(a):
#     if a==2:
#         return 1/2
#     else:
#         return 1/a+geometric(a/2)
# num1=int(input('enter your number    = '))
# print(geometric(num1))


# 10. Write a Python program to calculate the value of 'a' to the power 'b'.
# def calculate(a,b):
#     if b==1:
#         return a
#     else:
#         return a*calculate(a,b-1)
# num1=int(input('enter your  number    = '))
# power=int(input('enter your number   = '))
# print(calculate(num1,power)) 


# 11. Write a Python program to find  the greatest common divisor (gcd) of two integers. 
# def gcd(p,q):
#     if q==1:
#         return 1
#     elif p%q==0:
#         return q
#     else:
#         return gcd(q,p%q)
# p=int(input('enter your number   = '))
# q=int(input('enter your your divisior number    = '))
# z=gcd(p,q)
# print(z)



# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#                                      M E R A K I
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# 1 Pelindrome
# def ifPalindrome(string):
#     if string == "":  # BASE CASE CONDITION
#         return True
#     elif len(string) == 1:  # BASE CASE CONDITION
#         return True
#     elif string[0] == string[len(string)-1]:  # RECURSION
#         return ifPalindrome(string[1:][:-1])
#     else:
#         return False 
# print(ifPalindrome('naman'))


# 2 Binary Search
# Humei ek list mei koi element search karna hai. Ek example lete hai.
# to_find_list = [2, 5, 9, 12, 81, 23, 71, 28, 90, 67]
# to_find_element = 81 

# first way
# def is_present_in_list(number_to_search, list_to_search):
#     length_of_list = len(list_to_search)
#     if length_of_list == 0:
#         return False
#     if length_of_list == 1:
#         # list_to_search[0] is the only element left in this list
#         if number_to_search == list_to_search[0]:
#             return True
#         else:
#             return False
#     first_half_of_list = list_to_search[:int(length_of_list/2)]
#     second_half_of_list = list_to_search[int(length_of_list/2):]
#     return (is_present_in_list(number_to_search, first_half_of_list) or is_present_in_list(number_to_search, second_half_of_list))
# print (is_present_in_list(3, [3, 5, 7, 8, 4, 6, 2, 1, 9]))
# print (is_present_in_list(10, [3, 5, 7, 8, 4, 6, 2, 1, 9]) )

# second way
# def is_present_in_list(number_to_search, list_to_search):
#     counter = 0
#     while (counter < len(list_to_search)):
#         if number_to_search == list_to_search[counter]:
#             return True
#         counter += 1
#     return False
# print (is_present_in_list(3, [3, 5, 7, 8, 4, 6, 2, 1, 9]))
# print (is_present_in_list(10, [3, 5, 7, 8, 4, 6, 2, 1, 9]))

