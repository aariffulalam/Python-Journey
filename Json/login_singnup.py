# login signup


def fnc():
    
    dict1={}
    dict2={}
    dict3={}
    
    import json
    want=int(input("""for signup press - 1 \n for login press - 2""" ))
    # roll=int(input("enter your Roll number:  "))

    
    if want==1:
        Fname=input("enetr your first name:  ")
        Lname=input("enter your last name:  ")
        email=input("enter your email adderss:  ")
        password=input("enter your password:  ")
        try:
            fp= open("/home/ng/Desktop/Aarif_alam/lsup.json","r") 
            data3=json.load(fp)
            # print(data3)
            # print(type(data3))
            roll=len(data3["student"])+1
            # print(roll)
            # print(type(roll))
            # print(int(roll))


            dict3["Fname"]=Fname
            dict3["Lname"]=Lname
            dict3["email"]=email
            dict3["password"]=password

            data3["student"][roll]=dict3
            # print(data3)
            # print(type(data3))
    
            fp=open("/home/ng/Desktop/Aarif_alam/lsup.json","w")
            data1=json.dump(data3,fp,indent=3)
            fp.close()
        except:
            fp= open("/home/ng/Desktop/Aarif_alam/lsup.json","w") 
            
            roll=1
            dict3["Fname"]=Fname
            dict3["Lname"]=Lname
            dict3["email"]=email
            dict3["password"]=password

            dict2[roll]=dict3

            dict1["student"]=dict2
            # print(dict1)
            # print(type(dict1))

            
            data1=json.dump(dict1,fp,indent=3)
            fp.close()

    elif want==2:


        fp=open("/home/ng/Desktop/Aarif_alam/lsup.json","r")
        data2=json.load(fp)
        # # print(data2)
        # # print(type(data2))

        no=0
        a=data2
        # # print(data2)
        # # print(a["student"])
        # # print(type(data2))


        email1=input("enter your email adderss:  ")
        # print(email1)
        # print(type(email1))
        password1=input("enter your password:  ")
        # print(password1)
        # print(type(password1))
        # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

        for j in range(1,len(a["student"])+1):
            i=a["student"][str(j)]["email"]
            j=a["student"][str(j)]["password"]
            # print(i)
            # print(type(i))
            # print(j)
            # print(type(j))

            if email1 == i:
                if  password1==j:
                    print("yes your data is is exist")
                    break
                else:
                    no+=1
            else:
                no+=1
        if no==len(data2["student"]):
            print("Login first")
    

fnc()

        






    

# # print(True or False)

# # import json
# # fp= open("/home/ng/Desktop/Aarif_alam/lsup.json","r")
# # data1=json.load(fp)
# # print(data1)
# # print(type(data1))


# # a=dict1.items()
# # print(a)

# # dict1["student"][2]="akash"
# # print(dict1)
# # # print(dict1["student"])
# # # print(dict1["student"][1])
# # # dict1["student"]="aarif"
# # # print(dict1["student"])
# # dict1["student"][1]="aariffffffff"
# # print(dict1)

# # j=1
# # print(str(j))
# # print("j")