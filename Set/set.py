

# Very important part of set constructor   * * * set() * * *
# a={1,2,3}
# a.clear()
# print(a)
# print(type(a))    # here we always get set() not  this {}   



# a={1,2,34,2,4,}
# b={'ArRa',12}
# a=a+b                                #Error- Unsupported operand type(s) for +: 'set' and 'set'
# a.append(b)                          ##Error- 'set' object has no attribute "append"
# print(a)

# for i in range(0,len(a)):                # Error-  "Set" object is not subscriptable
#     print(a[i])
### But
# for i in a:              #   ***   It is working   ***   #
#     print(i)

# a.add('ArRa')              #    ***     Add()  method .   it is used to add element in set.    ***    #
# print(a)

# a.update(b)                  #    ***  Update()   method  .  it is used to add set in current set.   ***   #
# print(a)
# ###We can Add any this which can be iterable...###
# c=['ArRa','Ar','Ra']
# a.update(c)
# print(a)


# Remove items from set.
# a={1,2,34,2,4,}

# a.remove(2)                             #if velue is not in veriable then it wiil give Error  ###
# a.remove(a[2])                          #TypeError: 'set' object is not subscriptable
# print(a)

# a.discard(34)                           # this also not accept index
# print(a)                                # if velue is not in veriable then it wiil not give Error  ###

# d=a.pop()
# print(d)
# print(a)              # Set don't accept index thats why we can't kow what element will Remove  ###

# a.clear()                #    Clear all element from Set
# print(a)      

# del a         #  del keyword will delet the set completely.  ###
# print(a)                #  NameError: 'a' is not defined.


###  Join two or more Sets.

# a={1,2,3,'ArRa'}
# b={'Ar','ArRa','Ra'}    ### this Union method return a new set with all items from both set.###
# c=a.union(b)              #  Always gives different index of values...
# d=b.union(a)              # this is also
# print(c,d)

# a.update(b)
# print(a)               #    ********   #


# Intersection of two Sets    *Only Duplicates* 

#if you wants change in you set.
# a.intersection_update(b)      #  this metod will keep only the items that are present in both  
# print(a)                      #  creat new Set.   ***

#   if you do not want to change your both Sets
# z=a.intersection(b)
# print(z) 



# Keep all but, NOT the Duplicates
# a={1,2,3,'ArRa'}
# b={'Ar','ArRa','Ra'} 

# if you wants changes in youor sets
# a.symmetric_difference_update(b)           # a veriable will Updated
# print(a)

#if you don't wants changes in  your sets
# z= a.symmetric_difference(b) 
# print(z)


#  Use of Difference() method
# a={1,2,3,'ArRa'}
# b={'Ar','ArRa','Ra'} 

#if you don't wants to change in sets
# z=a.difference(b)
# print(z)

#if you wants changes in your Sets
# a.difference_update(b)
# print(a)


# a={11,2,22,3,3,11}
# b=set(a)
# print(b)
# b=list(b)
# print(b)
# c=1+5j
# print(type(c))
# d=9
# a.update(d)
# print(a)

 
# using Clear() method in set and list is totally different 
# list1=[1,2,3,4,5,6]
# list1.clear()
# print(list1)

# a={}
# print(type(a))
# list1=[1,2,3,4,5,6]
# list1.clear()
# print (list1)

# set2=set()
# set1={1,2,3,4,5,6}
# # set1.clear()
# # print(set1)
# for i in set1:
#     set2.add(i)
# print(set2)