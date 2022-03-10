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
## *******
# listA.append(listB)                   #         ******Solve by Extend Method  
## ******
# listA.extend(listB)
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
# a.insert(1,'fack')
# print(a)

#******
# a=[1,'soul',34,'Aarif',36,'Ar Ra']
# a.remove(a[2])
# print(a)

# ******
# a=[1,24,42,'asd','dfg']
# b=['soul','ArRa']
# a.pop()                         # withot any number   *************    It will remove last element
# a.pop(3)
# print(a)

# ******
# a=['z','x','w','a','b','c']                              ##this is based on *acci Range*
# b=[1,2,3,4,5,22,32,4221]
# print(min(b))
# print(max(a))

# ******
# a=['a','z','x','w','a','b','c']
# b=a.index('a')               #   *****   It give us a first duplicate latter of index
# print(b)



# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]

# print ( type(magic_square))
# print (type(magic_square[0]))
# print (type(magic_square[1]))

# print (sum(magic_square[0]))
# print (sum(magic_square[1]))
# print (sum(magic_square[2]))

#********************************

# # Defining a list
# list = [{1, 2}, ('a'), ['1.1', '2.2']]

# # clearing the list
# print(list)
# list.clear()

# print('List:', list)

# a=[i for i in range(10)]              #****     1
# print(a)
# b=list(range(10))                   #****     2
# print(b)

# a='hello Aarif, i am God'            #**********    string to      L i s t       
# b=a.split()
# print(b)



######    **********                  Join all the content in the list into a String.
# a=['hello','world','python','is','awesome']           
# print(a)
# b=' '.join(a)
# b=''.join(a)
# b='-'.join(a)
# print(b)


# a = [[1,2,3],[4,5],[6],[7,8,9]]            #convert a list into a Flate List...
# a = [[1,[2],3],[4,5],[6],[7,8,9]]
# import itertools
# b=list(itertools.chain(*a))
# print(b)



# from itertools import count


# a=[1,2,2,2,2,3,3,4,]
# b=[i for i in a if a.count(i)>1]
# print(b)
# from itertools import count


# a=[1,2,2,2,2,3,3,4,]
# b=[i for i in a if a.count(i)>1]
# print(b)


# from itertools import count


# a=[1,2,2,2,2,3,3,4,]
# b=[i for i in a if a.count(i)>1]
# print(b)


# from itertools import count


# a=[1,2,2,2,2,3,3,4,]
# b=[i for i in a if a.count(i)>1]
# print(b)


###############
# #Tupple
# a=1,2,3,4
# print(type(a))
#*******
# # Set
# a=set()
# print(a)
# a=set('helloAarif')
# a=set((1,2,3,'set',2,'Aarif')) 
# a=set([1,2,3,'set',2,'Aarif'])
# print(a)
###############




#  *********************************************************************************************************
#  ******************                    Meraki Questions                             **********************
#  *********************************************************************************************************

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]

# print (len(students))
# print (len(marks))
#Dekho ki dono lists li length 6 hai. Inpe iterate karne ka code aise likhenge:
# length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
# counter = 0
# while counter < length:
    # print (students[counter] + str(marks[counter]))
    # print(students[counter],(marks[counter]))
    # print(int(students[counter]) +(marks[counter]))          # Error #
    # counter+=1



 #Find  how many elements in list without using of len function
# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
# c=0
# for i in numbers:
#     c+=1
# print(c)



# Code likho jo di gayi list mein jo number 20 se bade hai aur 40 se chote hai unhe count kare.
#  Aur firr unka count print kare.

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# b=0
# c=0
# for i in numbers:
#     if i>20 and i<40:
#         b+=1
#         c+=i
#         print(i)
# print(b)
# print(c)





# ************     Code likho jo iss list mein se maximum dhund kar ke print kare.       **********
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(max(numbers))
# max=numbers[0]
# for i in range(1,len(numbers)):
#     if numbers[i]>max:
#         max=numbers[i]
# print(max)

#                 ********       For   (Second Max number)          *********
# print(numbers)
# max=numbers[0]
# for i in range(1,len(numbers)):
#     if numbers[i]>max:
#         max=numbers[i]
# print('Max number of the list',max)
# for a in range(len(numbers)-1):
#     if max==numbers[a]:
#         numbers.remove(numbers[a])
# print(numbers)
# secondMax=numbers[0]
# for b in range(1,len(numbers)):
#     if numbers[b]>secondMax:
#         secondMax=numbers[b]
# print(secondMax)

#                        *********      While   (Second max numbers)         ********
# print(numbers)
# max=numbers[0]
# i=1
# while i <len(numbers):
#     if numbers[i]>max:
#         max=numbers[i]
#     i+=1
# print('Max number of the list',max)
# a=0
# while a<len(numbers):
#     if max==numbers[a]:
#         numbers.remove(numbers[a])
#     a+=1
# print(numbers)
# secondMax=numbers[0]
# b=1
# while b<len(numbers):
#     if numbers[b]>secondMax:
#         secondMax=numbers[b]
#     b+=1
# print(secondMax)



# ******* Code likho jo neeche di gayi lists ke items ko reverse order yaani ki ulta print kare.   *****
# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 
# print(places[::-1])
# places.reverse()
# a=list(reversed(places))
# print(a)
# print(places)











# Palindrome wo strings ya numbers hote hai jo ulta seedhe same hote hai.
# Jaise, NITIN. Nitin ko aap left se padho ya right se, nitin hi hai.Aise hi MOM bhi ek palindrome hai. 
# Code likho jo check kare ki kya list palindrome hai ya nahi. Aur print karo “Haan! palindrome 
# hai” agar hai. Aur “nahi! Palindrome nahi hai” agar nahi hai.
# Abhi ke liye iss list ko use kar ke code likh sakte ho:

# name=[ 'n', 'i', 't', 'i', 'n' ]
# name=list(input('enter what yu want'))
# print(name)
# naam=list(reversed(name))
# if naam==name:
#     print('It is palindrome')
# else:
#     print('Sorry it is not palindrom')






#       **********              B i n a r y   numbers ko decimal form mei karna hai           **********    

#    ***********     without using of List      ************
# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# binary_number=list(input('enter your numbers'))
# print(binary_number)
# b=0
# c=0
# i=0
# for i in binary_number[::-1]:
#     if i =='1':
#         c+=2**b
#     b+=1
# print(c)

#                       ***************** with using of List   ***************
# a = int(input("Enter the lenth of binory number :"))
# d = []
# for i in range (a):
#     vv =int(input("Enter your binary number :"))
#     d.append(vv)
# print(d)
# b=0
# c=0
# i=0
# y=0
# for i in d[::-1]:
#     if i==1 or i==0: 
#         if i ==1:
#             c+=2**b
#         elif i==0:
#             pass
#     else:
#         y+=1
#         break
#     b+=1
# if y==0:
#     print(c)
# else:
#     print('invalide number')




# ** Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers are not present in the second array.
# list1 = [1,2,3,4,5,6]
# a=list(list1)
# list2 = [2,3,1,0,6,7] 
# for i in list1:
#     for j in list2:
#         if i==j:
#             print(i)
#             # list1.remove(i)
#             a.remove(i)
# print('this are not match',a)



#    **** list ke sabhi numbers ko add akaro   ****
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
for i in range(0,len(marks)):
    for j in 

















