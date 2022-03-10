# a=(1,)
# print(a)
# print(type(a))
# print(a[1])              #it is Tuple but in index 1 it don't have element s it will give us Error- Out of index

# a=(1,(1),True,'ar',1.2,1+5j)
# print(a)
# b=(1)
# a=a+b                       # an only concatenate tuple (not "int") TO TUPLE
# print(a)

# print(type(a))                 #   <class type(tuple)>
# a= (("apple", "banana", "cherry"))
# print(type(a))

# a=tuple(1)                # typeError- 'int' object is not iterable
# print(a)
# print(type(a))

# a = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")         #   slicing
# print(a[2:7:2])

# Convert the tuple into a list to be able to change it:
# a=('ArRa',3,6,9,'love ''you','so much')
# b=list(a)
# b[2]=36
# a=tuple(b)     # if ypu want any changes in your tuple then fist change into tuple
# print(a)

# b=a.clear()                        # Error object has no attribut "clear", "remove", "del" etc.
# print=(b)



######Paking in Tuple
# a=('Aarif','Pinku','Akash',"Rahul",'Vivek')       # Giving elements in one veriable it is called Paking.

# (Love,Soul,Suggetive,Support,Loyal)=a             #  Unpacking a Tuple.
# print(Love)
# print(Soul)
# print(Suggetive)
# print(Support)
# print(Loyal)

# print(*a)      # from using of star (  *   )    give output without any types of Brackets and one space.

# (Love,Soul,*Support)=a   # If the number of variables is less than the number of values, you can add an * to 
# print(Support)                       # the variable name and the values will be assigned to the variable as a list:
# print(type(Support))
# print(tuple(Support))

#
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

