# a=1
# if a==1:
#     print("a")
# else:
#     print("g")

#Guessing game of Aarif alam.

# import random
# i=1
# while i<=3:
#     c=random.randint(1,50)
#     x=int(input("enter your number"))
#     if x!=c:
#         if x<c:
#           print("your number is too high")
#         elif x>c:
#             print("yor number is too low")
#     else:
#         print("congretulatin you choose correct number")
#         i=3
#     i=i+1



#   input have to be reverse....
# 
# # 
# x=input('enter your words')
# b=1
# while b<=len(x):
#     print(x[len(x)-b],end =" ")
#     b=b+1



#####      5       #####

# x=input('enter your word')
# b=0
# while b<len(x):
#     if b%2==0:
#         print(x[b].capitalize(),end=' ')
#     else:
#         print(x[b].casefold(),end =' ')
#     b=b+1

#  2nd way 
# x=input('enter your word')
# b=0
# while b<len(x):
#     print(x[b].capitalize(),end=' ') if b%2==0 else print(x[b].casefold(),end =' ')
#     b=b+1




#####          6             #######
# write a Python program to count the number of even and odd numbers from a series of numbers.

# x=int(input('enter your max number'))
# i=1
# c=0
# d=0
# while i<=x:
#     if i%2!=0:
#         c=c+1
#         print(i)
#     else:
#         d=d+1
#         print(i)
#     i=i+1
# print("Here is your count of odd numbers    ",d)
# print()
# print('here is your count of even numbers      ',c)




####       7         ####

# Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

# datalist=[1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"class":'v',"section":'A'}]
# d=0
# while d<len(datalist):
#     print(datalist[d])
#     d=d+1





#####        8        #####

#  Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

# i=0
# while i<=6:
#     if (i==3 or i==6):
#         i=i+1
#         continue
#     print(i)
#     i=i+1


# ####           9           ######

# v9. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
# Note : The Fibonacci Sequence is the  of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

# x=int(input('enter your max number     '))
# a=0
# b=1
# c=0
# while c<=x:
#     print(c)
#     a=b
#     b=c
#     c=a+b




############################################################################################################
                                #   L    E    A     V     E        
############################################################################################################

######            11               ######

# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional
# array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# # j = 0,1, n-1. 

# m=int(input('enter your max number of Row'))
# n=int(input('enter your max number of column'))
# i=0
# j=0
# while i<m:
#     while j<n:
    #     print(i*j,end=' ')
    #     j=j+1
    # print()
    # i=i+1

#############################################################################################################

#############################################################################################################

#       FOR       LOOP      #

# m=int(input('enter your max number of Row'))
# n=int(input('enter your max number of column'))
# for i in range (m):
#     for j in range (n) :
#         print(i*j,end=' ')
#     print()
  











#############################################################################################################
######    12       ######        M  A  N  Y              W  A  Y  S          ######           12     #######     
#############################################################################################################




# list=[]
# x=input('enter your word')
# a=list.append(x.upper())
# print(list)

##############          2nd WAY to do print of append            #############
# lines = []
# a=0
# while a<3:
#     l = input()
#     if l:
#         lines.append(l.upper())
#     else:
#         break;
#     a+=1
# b=[]
# for l in lines:
#     print(l)

##############     3rd  WAY to fo this print      ###############
# lines = []
# a=0
# while a<3:
#     l = input()
#     if l:
#         lines.append(l.upper())
#     else:
#         break;
#     a+=1
# b=[]
# for l in lines:
#     print([l],end="")






###########                       14                 ######################

#count numbers , alphabets and special characters in your words have in it. 

# a=input('enter your word    :  ')
# d=0
# c=1
# x=0
# y=0
# z=0
# while c<=len(a):
#     if a[d]!='':
#         if ((a[d]=='1') or (a[d]=='2') or (a[d]=='3') or (a[d]=='4') or (a[d]=='5') or (a[d]=='6') or (a[d]=='7') or (a[d]=='8') or (a[d]=='9') or (a[d]=='0')):
#             x=x+1
#         elif (a[d]=='@' or a[d]=='#' or a[d]=='$' or a[d]=='&'):
#             y=y+1
#         else:
#             z=z+1
#     d=d+1
#     c=c+1
# print('total times of occuring of numbers : ',x)
# print('total times of occuring of alphabets : ',z)
# print('total times of occuring of special charecters : ',y)

        




################                     15                      ################

#    Strong paasword
#At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.


# a=input('enter your password    :  ')
# d=0
# c=1
# x=0
# y=0
# z=0
# s=0
# if len(a)>=6 and len(a)<=16:
#     while c<=len(a):
    
#         if a[d] != '':
#             if ((a[d]=='1') or (a[d]=='2') or (a[d]=='3') or (a[d]=='4') or (a[d]=='5') or (a[d]=='6') or (a[d]=='7') or (a[d]=='8') or (a[d]=='9') or (a[d]=='0')):
#                 x=x+1
#             elif (a[d]=='@' or a[d]=='#' or a[d]=='$' or a[d]=='&'):
#                 y=y+1
#             else:
#                 z=z+1
#         else:
#             s=s+1
#         d=d+1
#         c=c+1
#     if x>0 and y>0 and z>0 and s==0:
#         print('your paasword is acceped  :  ',a)
#     else:
#         print('you have  to built you paasword of the rule of this function')
# else:
#     print('your paasword is going to be wrong')






##############              16                        #######################

#find numbers between 100 and 400 (both included) where each digit of a number is an even number.
#  The numbers obtained should be printed in a comma-separated sequence.


# a=100
# b=0
# while a<=400:
#     if a%2==0:
#         print(a,',',end=' ')
#     b=b+1
#     a=a+1
# print()
# print('total count of number occuring      :     ',b)




# Write a Python program to print alphabet pattern 'A'

#  *** 
# *   *
# *   *
# ***** 
# *   *
# *   *
# *   *


# row=0
# while row<=6:
#     col=0   
#     while col<=4:
#         if row==0 and col in {1,2,3}:
#             print('*',end = ' ')
#         elif row in {1,2,4,5,6} and col in {0,4}:
#             print('*',end=' ')
#         elif row ==3 and col in {0,1,2,3,4}:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#         col+=1
#     row=row+1
#     print( )


# for row in range(0,7):
#     for col in range(0,5):
#         if (row==0) and (col in {1,2,3}) :
#             print('*',end =' ')
#         elif row in {1,2,4,5,6} and col in {0,4}:
#             print('*',end=' ')
#         elif row ==3 and col in {0,1,2,3,4}:
#             print('*', end=' ')
#         else:
#             print(' ',end=' ')
#     print()






##################                     18                   ###############

# Write a Python program to print alphabet pattern 'D'

# for row in range(0,7):
#     for col in range(0,5):
#         if row in {0,6} and (col in {0,1,2,3}) :
#             print('*',end =' ')
#         elif row in {1,2,3,4,5} and col in {0,4}:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()




###################                        19                                ##################

#Write a Python program to print alphabet pattern 'E'.


# for row in range(0,7):
#     for col in range(0,5):
#         if row in {0,6} and (col in {0,1,2,3,4}) :
#             print('*',end =' ')
#         elif row in {1,2,4,5} and col==0 :
#             print('*',end=' ')
#         elif row==3 and col in {0,1,2}:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()






####################                     20                        ########################

#Write a Python program to print alphabet pattern 'G

# for row in range(0,7):
#     for col in range(0,5):
#         if row in {0,6} and (col in {1,2,3}) :
#             print('*',end =' ')
#         elif row in {1,4,5} and col in {0,4} :
#             print('*',end=' ')
#         elif row==3 and col in {0,2,3,4}:
#             print('*',end=' ')
#         elif row ==2 and col==0:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()





################                   21                      #################

#Write a Python program to print alphabet pattern 'L'.

# for row in range(0,7):
#     for col in range(0,5):
#         if row in {0,1,2,3,4,5} and (col in {0}) :
#             print('*',end =' ')
#         elif row in {6} and col in {0,1,2,3,4} :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()







########################                     22                            #####################

#Write a Python program to print alphabet pattern 'M'


# for row in range(0,7):
#     for col in range(0,5):
#         if row in {0,3,4,5,6} and (col in {0,4}) :
#             print('*',end =' ')
#         elif row in {1} and col in {0,1,3,4} :
#             print('*',end=' ')
#         elif row in {2} and col in {0,2,4}:
#             print('*',end= ' ')
#         else:
#             print(' ',end=' ')
#     print()





######################                            25                         ########################

#   ooooooooooooooooo                                                       
#  ooooooooooooooooo                                                       
#  ooooooooooooooooo                                                       
#  oooo                                                                    
#  oooo                                                                    
#  oooo                                                                    
#  ooooooooooooooooo                                                      
#  ooooooooooooooooo                                                       
#  ooooooooooooooooo                                                       
#               oooo                                                       
#               oooo                                                       
#               oooo                                                       
#  ooooooooooooooooo                                                       
#  ooooooooooooooooo                                                       
# oooooooooooooooooo

# for row in range(0,15):
#     for col in range(0,19):
#         if row in {1,2,6,7,8,12,13,14} and (col in {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17}) :
#             print('o',end =' ')
#         elif row in {3,4,5} and col in {1,2,3,4} :
#             print('o',end=' ')
#         elif row in {9,10,11} and col in {14,15,16,17}:
#             print('o',end= ' ')
#         elif row in {0} and col in {2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18}:
#             print('o',end=' ')
#         elif row in {14} and col in {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}:
#             print('o', end=' ')
#         else:
#             print(' ',end=' ')
#     print()









################################                          31                          #########################
 
#  # Write a Python program to calculate a dog's age in dog's years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years

###########            L        E         A       V        E             ################################








###########################                           32                            ########################

# Write a Python program to check whether an alphabet is a vowel or consonant.

# var=input('-enter your words      :       ')
# a=0
# d=0
# c=1
# x=0
# y=0
# z=0
# while c<=len(var):
#     if var[d]!='':
#         if ((var[d]=='1') or (var[d]=='2') or (var[d]=='3') or (var[d]=='4') or (var[d]=='5') or (var[d]=='6') or (var[d]=='7') or (var[d]=='8') or (var[d]=='9') or (var[d]=='0')):
#             x=x+1
#         elif (var[d]=='@' or var[d]=='#' or var[d]=='$' or var[d]=='&'):
#             y=y+1
#         elif (var[d]=='a' or var[d]=='A' or var[d]=='e' or var[d]=='E' or var[d]=='i' or var[d]=='I' or var[d]=='o' or var[d]=='O' or var[d]=='u' or var[d]=='U'):
#             z=z+1
#         else:
#             a=a+1
#     d=d+1
#     c=c+1
# print('-your word have vowels     :    ',z)
# print()
# print('-your word have consonants     :    ',a)
# print()
# print('-your word have numbers     :    ',x)
# print()
# print('-your word have special characters     :    ',y)




            




##############                                35                                         ###############

# Write a Python program to check a string represent an integer or not.

# a=input('-enter your input      :     ')
# d=1
# b=0
# int=0
# str=0
# str2=0
# while d<=len(a):
#     if a[b] !='.':
#         if a[b]==0 or a[b]==1 or a[b]==2 or a[b]==3 or a[b]==4 or a[b]==5 or a[b]==6 or a[b]==7 or a[b]==8 or a[b]==9:
#             int+=1
#         else:
#             str+=1
#     else:
#         str2+=1
#     b+=1
#     d+=1
# if (str>0 or str2>0):
#     print('your input is not "int"    :  ',a)
# else:
#     print('your input is "int"      :  ',a)





#         51               

############  L       one loop      (S  H  O  R  T          hand if-else)              ##############

#
#
#
####



# for i in range(8):
#     print('*'*1) if i in {1,2,3,4,5,6} else print('*'*i)






###########                  52                                

#########             ###############                 ############                     #############

#          print     #             H     E     A     R     T                #         

#  ** **
# *  *   *
# *      *
# *      *
#  *    *
#   *  *
#    *

# for row in range(0,7):
#     for col in range(0,7):
#         if row==0 and col in {1,2,4,5}:
#             print('*', end=' ')
#         elif row==1 and col in{0,3,6}:
#             print ('*',end=' ')
#         elif row in {2,3} and col in {0,6}:
#             print('*',end=' ')
#         elif row ==4 and col in {1,5}:
#             print('*',end=' ')
#         elif row ==5 and col in {2,4}:
#             print('*',end=' ')
#         elif row==6 and col==3:
#             print('*',end=' ')
#         else:
#             print('',end=' ')
#     print( )

        




 ##############                                53                                  #################

################                        bult perfect number                       ###################

#                                            While loop

# a= int(input('  -enter your number to find is it perfect number or not       :-  '))
# d=1
# c=0
# b=1

# while d<a:
#     if a%d==0:
#         c=c+d
#     d=d+1
# if a==c:
#     print('-this is perfect number    :-  ',a,"=",c)
# else:
#     print('not perfect number')



#                       FOR   LOOP       using of      Short hand if-else                #

# a= int(input('  -enter your number to find is it perfect number or not       :-  '))
# d=1
# c=0
# for d in range(d,a):
#     if a%d==0:
#         c=c+d 
# print('-this is perfect number    :-  ',c) if a==c else print('not perfect number    :-   ',c)


#########################################################################################################

  






###############                                54                                  #################
##################################################################        Complete it                #####################
#########                                Amstrong  Number                                    #######

# a=input('enter your number      :-  ')
# b=0
# c=0
# while b<len(a):
#     a=int(a)
#     y=a[b]**len(a)
#     c=c+y
# print(c)



###################                                        55                                    ####################

##          print Riverse of your  input                                                                 ##

#####                                         Uing    Of     While  Loop                                     ########


# a=input("enter your number    :-  ")
# d=len(a)
# b=1
# while b<=len(a): 
#     print(a[d-b],end='')
#     b+=1
    
############                                    For     Loop                                                 ###############

# a=input("enter your number    :-  ")
# d=len(a)
# for b in range(1,d+1): 
#     print(a[d-b],end='')










###############################################################################################################
###############################################################################################################
#
#                               T E S T        Q U E S T I O N
#
###############################################################################################################
###############################################################################################################




#  *********************************************************************************************************
#  ***************************** [1]   remove    P U N C H U A T I O N     ************************************
#***********************************************************************************************************

# a=input('enter your input    :-  ')
# d=0

#  ***************************************    Tempapry       punchuation    removing      *********************
# while d<len(a):
#     if a[d]=='!' or a[d]=='?' or a[d]==';' or a[d]==':' or a[d]=='.' or a[d]==',' or a[d]=='"' or a[d]=="'" or a[d]=='(' or a[d]==')' :
#         c=a[d]
#     else:
#         print(a[d],end='')
#     d=d+1


# ****************************        (permanent)   punchuation   removing      *******************************
# e=''
# x='!(),.?/"'"'"':;'
# for i in a:
#     if i in x:
#         pass
#     else:
#         e=e+i
# print(e)



#    ******************************************************************************************************
#****************************       [2]   Anagram         ****************************************************   
#    ********************************************************************************************************




#***********************************************************************************************************
# ********************************  [3]     String    Deleting       *****************************************
#***********************************************************************************************************

# a=input ('enter your number   :-  ')
# x=input ('enter your alphabet what you want to remove    :-    ')
# d=''
# e=0

#  **************************   (Single)      Temperary   Removing           ***************************       #
# while e<len(a):
#     if x==a[e]:
#         print('',end='')
#     else:
#         print(a[e],end = '')
#     e=e+1


#  **************************  (Single)       permenant   Removing           ***************************       #
# for i in a:
#     if i==x:
#         pass
#     else:
#         d+=i
# print(d)

#   ****************************       (multiple)  Removing strimg   [PERMENANT]       ************************     #
# c=0
# j=len(x)
# for i in a:
#     if i in x:
#         c=c+1
#         pass
#     else:
#         d+=i
# print(d)




# i=1
# a=int(input('max number you want in your python?     :-   '))
# b=int((a/2)-0.5    )
# while i<=a:

###################################          FUN            ####################################################################
# a=int(input('enter your number'))
# b=a
# d=0
# while d<=a:
#     print('<'*b,':'*d, '!'*b,'@'*d,'#'*b,'$'*d,'%'*b,'^'*d,'&'*b,'*'*d,':'*b,'>'*d)
#     d=d+1
#     b=b-1

#********************************************************** 

# a=input('enter your word')
# a=set(a)
# print(a)
################################################################################################################################






#  ***************************************************************************************************************************
# 1 2 3 4 5                          *************   P  A  T  T  E  R  N   ************  
# 10 9 8 7 6
# 11 12 13 14 15
# 20 19 18 17 16
# 21 22 23 24 25
#    **************************************************************************************************************************

# a=int(input('enter you max number      :-   '))
# b=1
# c=1
# for i in range(1,a+1):
#     d=0
#     for j in range(1,a+1):
#         if i%2!=0:
#             print(b,end=' ')
#         elif i%2==0:
#             print((i*a)-d,end =' ')
            
#         b=b+1
#         d=d+1
#     print()
        
#************************************************************************************************************************
   
#********************************************************************************************************************

#       **************************     S  T  R  I   N   G     ***********************
# print('c:\1arry')

# txt='banana aarif banana'
# x=txt.center(90)
# print(x)
# print(len(x))

# txt = "Hello, welcome to my world"
# x = txt.endswith("d")
# if x== True:
# 	print('aarif is hero')


#    *****************************       L  I  S  T     *************************

# a=[12,43,5,2,1,3]
#******
#  a.sort()
#******
# a.reverse()
# print(a)

# a=[12,43,5,2,1,3]
#******
#  a.append(4)
# print(a)


# listA = ['Mon', 'Tue', 'Wed']
# listB = ['2 pm', '11 am','1 pm']
# listC = [1, 3, 6]
# # Given lists 
# print("Given list A: " ,listA)
# print("Given list B: " ,listB)
# print("Given list C: ",listC)
# # using + operator 
# res_list = listA + listB + listC
# # printing result  
# print("Combined list is : ",res_list)

# listA = ['Mon', 'Tue', 'Wed']
# listB = ['2 pm', '11 am','1 pm']
# listA.append(listB)
# print(listA)

# listA = ['Mon', 'Tue', 'Wed']
# listB = ['2 pm', '11 am','1 pm']
# listA.append(listB[:1])
# print(listA)

#    *****Done******
# listA = ['Mon', 'Tue', 'Wed']
# listB = ['2 pm', '11 am','1 pm']
# b=0
# while b<len(listB):
#     listA.append(listB[b])
#     b+=1
# print(listA)

#******
# a=[1,'soul',34,'Aarif',36,'Ar Ra']
# a.insert(1,'facke')
# print(a)

#******
# a=[1,'soul',34,'Aarif',36,'Ar Ra']
# a.remove(a)
# print(a)

# ******
# a=[1,24,42,'asd','dfg']
# b=['soul','ArRa']
# a.pop(3)
# print(a)

# ******
#this is based on *acci Range*
# a=['z','x','w','a','b','c']
# b=[1,2,3,4,5,22,32,4221]
# print(min(b))
# print(max(a))



#########################################################################################
#                                     M E E T      C L A S S
#########################################################################################
# x=3
# print('hello') if False else print('world') if False else print('I am hero')

# x=5
# print('even') if x%2==0 else print('odd')
# print('1 red') if x==1 else print('2 red') if x==2 else print('all are red')

# x=5
# if x%2==0:
#     if True:
#         print('hello')
#     else:
#         print('world')
# else:
#     if False:
#         print('Hello')
#     else:
#         print('World')

# x=5
# if x==1:
#     print('one apple iss red')
# elif x==2:
#     print('two apples are red')
# elif x==3:
#     print('rest of all apples are red')
# else:
#     print('all are heros')
# if x==5:
#     print('red 5')
#####################################################################################################
######################################################################################################
















#parmeshwar question... number horizontal to vertical
#x=int(input('enter your number'))

#b=len(str(x))
#while b>1:
#			a=1
#			m=10
#			n=(m**(b-1))
#			while (n*a)<=x:
#				
#				
#				c=x%(n*a)
#				a=a+1
#				
#				b=len(str(c))
#				
#			print(a)

#print(c)



#a='A\ta\tr\ti\tf'
#print(a)



#a='muhammadsiddiq'
#b=a.index('q',0,10)
#c=a.index('siddiq')
#print(b)
#print(c)


#print(a.find(','))


#b=a[slice(0,8)]
#c=a[slice(10,17)]

#print(c+b)



#txt = "For only {price:.2f} dollars!"
#print(txt.format(price = 49))




###Pattern###

####
####
####
####
#apple=int(input('enter your number for pattern'))
#a=apple
#b=1
#while b<=apple:
#	print('*'*a)
#	b=b+1



#
##
###
####
#apple=int(input('enter your number for pattern'))
#b=1
#while b<=apple:
#	print('*'*b)
#	b=b+1



####
###
##
#
#apple=int(input('enter your number for pattern'))
#b=apple
#while b>=1:
#	print('*'*b)
#	b=b-1



			

#####
  ####
    ###
      ##
        #
#apple=int(input('enter your number for pattern'))
#a=apple
#b=0
#while b<apple:
#	print(' '*b,'*'*a)
#	b=b+1
#	a=a-1




         #
      ###
   #####
#######

apple=int(input('enter your number of base for pattern'))
b=int((apple/2) - 0.5)
a=1
while a<=apple:
	print(' '*b,'*'*a,' '*b)
	a=a+1
	b=b-1




#######
  #####
    ###
      #

#apple=int(input('enter your number of upper base for pattern'))
#b=0
#a=apple
#while a>0:
#	print(' '*b,'*'*a,' '*b)
#	b=b+1
#	a=a-2



#
##
###
####
#####
####
###
##
#


###     2  loop    ###

#apple=int(input('enter your number of middle'))
#b=1
#while b<=apple:
#	print('*'*b)
#	b=b+1
#c=apple-1
#while c>0:
#	print('*'*c)
#	c=c-1



###      1 loop     ###

#apple=int(input('enter your number of middle'))
#b=1
#c=apple
#while b<apple or c>0:
#	if b<apple:
#		print('*'*b)
#	elif c>0:
#		print('*'*c)
#		c=c-1
#	b=b+1


#     1 2 3 4 5
#      6 7 8 9 10
#      11 12 13 14 15
#      16 17 1819 20
#       21 22 23 24 25


#a=int(input('enter number'))
#b=1
#while b<=a*a:
#		print(b,end=' ')
#		if b%5==0:
#			print( )
#		b=b+1



# wrong
#a=int(input('enter number'))
#b=1
#d=1
#e=1
#while d<=a*a and b<a:
#	if d<=a*b:
		
		
		


# find least of squring sequence numbers
#      2      4      16     256       65536     ......    etc.

#a=int(input('enter your max number for least of squring sequence number '))
#d=2
#while d<=a:
#		print(d, end=' ')
#		d=d*d



# 2   4   8   16    32    64   .... etc

#a=int(input('enter number and get all least of sequence number'))
#d=2
#while d<=a:
#		print(d,end=' ')
#		d=d*2


# 1   3      6      10        15        21     28...     etc.


#a=int(input('enter your max number to get least sequence number'))
#d=1
#b=2
#while d<=a:
#	print(d,end=' ')
#	d=d+b
#	b=b+1 



#for row in range(0,7):
#	for col in range(0,5):
#		if row==0 and col in {1,2,3}:
#			print('*',end=' ')
#		elif row in

	
