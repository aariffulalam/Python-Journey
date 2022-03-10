
# fobj=open("student.txt",'w')
# # name=input('enter your name  :  ')
# fobj.write("akshay")
# fobj.close()
# print('i am done  ') 
   
# fobj=open('student.txt','r')
# v=fobj.read()
# fobj.close()
# print(v)



# * * * * * * * * * * * * ** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# 1 Iss text ko people1-exercise.txt ke naam ki file mein save karo.
# Ab apne code se iss file ko kholo aur fir, uske saare contents ko print karo.

# Write
# data1=['rishabh - meerut','imtiyaz - delhi','nilima - cochin','rati - shimla','ayishah - delhi','raghu - shimla','naseer - kanpur',
# 'karthikeyan - delhi','salma - jaipur','pankaj - delhi','brijesh - delhi','govind - delhi','puneet - shimla','siddhi - delhi',
# 'suman - jaipur','rajeev - shimla','mohinder - delhi','rajendra - jaipur','priyanka - shimla','neela - delhi','sashi - jaipur',
# 'sarika - delhi','deepti - shimla','harshad - delhi','trishna - raipur','pradeep - jaipur','sekhar - delhi','nand - delhi',
# 'anoop - delhi','balwinder - tokyo']
# fobj=open("people1-exercise.txt",'w')
# fobj.writelines(data1)
# fobj.close()
# Read
# fobj=open("people1-exercise.txt",'r')
# v=fobj.read()
# fobj.close()
# print(v)

# loop
#Write
# fobj=open("people1-exercise.txt",'w')
# for i in range(10):
#     name=input('enter your name  : ')
#     place=input('enter your place   : ')
#     combine=name+'-'+place+'\n'
#     fobj.write(combine)
# fobj.close()
# Read
# fobj=open("people1-exercise.txt",'r')
# v=fobj.read()
# fobj.close()
# print(v)



# 2 Aapne jo pichle question mein (Question 1) file download kari hai, usko read karke usme number of lines count kar ke 
# print karein. Aapne sirf uss file ki number of lines Count karne ka code likhna hai. Hint: Har \n ke baad nayi
# line shuru hoti hai. Aap yeh use ke nayi line ka ko pehchan sakte ho.

# Write
# data1=['rishabh - meerut','\n','imtiyaz - delhi','\n','nilima - cochin','\n','rati - shimla','ayishah - delhi','\n',
# 'raghu - shimla','\n','naseer - kanpur','\n','karthikeyan - delhi','\n','salma - jaipur','\n','pankaj - delhi','\n',
# 'brijesh - delhi','\n','govind - delhi','\n','puneet - shimla','\n','siddhi - delhi','\n','suman - jaipur','\n','rajeev - shimla','\n',
# 'mohinder - delhi','\n','rajendra - jaipur','\n','priyanka - shimla','\n','neela - delhi','\n','sashi - jaipur','\n',
# 'sarika - delhi','\n','deepti - shimla','\n','harshad - delhi','\n','trishna - raipur','\n','pradeep - jaipur','\n',
# 'sekhar - delhi','\n','nand - delhi','\n','anoop - delhi','\n','balwinder - tokyo','\n']
# fobj=open("people1-exercise.txt",'w')
# fobj.writelines(data1)
# fobj.close()
# # Read 
# fobj=open("people1-exercise.txt",'r')
# v=fobj.readlines()
# c=0
# for i in v:
#     c+=1
#     print(i)
#     print(c)
# fobj.close()
# print(v)
# print('here is th totl element   ',c)



# 3 Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam 
#   ki file mein nayi line mein daalo. Aapki list yeh rahi:

#write
# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# fobj=open("question3.txt",'w')
# for i in banks_list:
#     fobj.write(i+'\n')
# fobj.close()
# Read
# fobj=open("question3.txt",'r')
# v=fobj.read()
# fobj.close()
# print(v)
# print(type(v))



# 4 Iss text ko question3.txt ke naam ki file mein save karo. Iss file mein dhyaan se dekhoge toh ek insaan ka naam 
#   aur ek sheher ka naam milegaYeh sheher woh sheher hai jisme woh insaaan rehta hai. Ab aapne ek aisa code likhna hai jo: 
#   1. Delhi mein rehne waale logon ko ek alag file mein daale. Delhi waali file ka naam "delhi.txt" hona chaiye. 
#   2. Shimla mein rehne waale logon ko ek alag file mein daale. Shimla waali file na naam "shimla.txt" hona chaiye 
#   3. Aur saare log jo delhi aur shimla mein nahi rehte, unko ek alag file mein daale. Iss file ka naam "others.txt" hona chaiye
# data1=[['rishabh', 'meerut'],
# ['imtiyaz' ,'delhi'],
# ['nilima' , 'cochin'],
# ['rati ' ,'shimla'],
# ['ayishah',  'delhi'],
# ['raghu ','shimla'],
# ['naseer ' ,'kanpur'],
# ['karthikeyan',  'delhi'],
# ['salma ' ,'jaipur'],
# ['pankaj ' ,'delhi'],
# ['brijesh' , 'delhi'],
# ['govind ' ,'delhi'],
# ['puneet ' ,'shimla'],
# ['siddhi ' ,'delhi'],
# ['suman ' ,'jaipur'],
# ['rajeev ' ,'shimla'],
# ['mohinder ' ,'delhi'],
# ['rajendra ', 'jaipur'],
# ['priyanka ', 'shimla'],
# ['neela ' ,'delhi'],
# ['sashi ' ,'jaipur'],
# ['sarika ', 'delhi'],
# ['deepti'  ,'shimla'],
# ['harshad ', 'delhi'],
# ['trishna' , 'raipur'],
# ['pradeep' , 'jaipur'],
# ['sekhar' , 'delhi'],
# ['nand ' ,'delhi'],
# ['anoop ' ,'delhi'],
# ['balwinder',  'tokyo']]



# data1=['rishabh - meerut','imtiyaz - delhi','nilima - cochin','rati - shimla','ayishah - delhi',
# 'raghu - shimla','naseer - kanpur','karthikeyan - delhi','salma - jaipur','pankaj - delhi',
# 'brijesh - delhi','govind - delhi','puneet - shimla','siddhi - delhi','suman - jaipur','rajeev - shimla',
# 'mohinder - delhi','rajendra - jaipur','priyanka - shimla','neela - delhi','sashi - jaipur',
# 'sarika - delhi','deepti - shimla','harshad - delhi','trishna - raipur','pradeep - jaipur',
# 'sekhar - delhi','nand - delhi','anoop - delhi','balwinder - tokyo']
# fobj=open('question3.txt','w')
# for i in data1:
#     fobj.writelines(i)
# fobj.close
# fobj=open('question3.txt','r')
# v=fobj.readlines()
# print(v)
# fobj=open('question3.txt','r')
# v=fobj.read()
# print(v)
# for i in 


# # write
# fobj=open('question3.txt','w')
# fobj.writelines(data1)
# fobj.close()
# fobj=open('question3.txt')
# v=fobj.read()
# print(v)
# fobj=open('question3.txt')
# for i in data1:
#     fobj.write(i+',')
# fobj.close()
# fobj=open('question3.txt','r')
# v=fobj.readlines()
# print(v)
# for i in data1:
#     fobj.writelines(i+'\n')
# fobj.close()
# # read
# fobj=open('question3.txt','r')


# c=0
# fobj=open('question3.txt','r')
# for i in fobj:
#     print(i)
#     print(c)
#     print(type(i))
#     c+=1


# fobj=open('question3.txt','w')
# fobj.writelines(data1)
# v=fobj
# print(fobj)
# fobj1=open("delhi.txt",'a')
# fobj2=open("shimla.txt",'a')
# fobj3=open("others.txt",'a')
# for i in data1:
#     if i[1]=='delhi':
#        fobj1.write(i[0])
#     elif i[1]=='shimla':
#         fobj2.write(i[0])
#     else:
#         fobj3. 

