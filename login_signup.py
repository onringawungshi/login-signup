import json,os
user_input=input("enter a for sign-up and b for log-in:-")
if user_input=="a":
    username=input("Enter your name:-")
    def func_login_signup():
        password1=input("Enter your password:-")
        password2=input("Confirm  password:-")
        l,u,p,d=0,0,0,0
        for i in password1:  
            if (i.islower()): 
                l+=1 
            if (i.isupper()): 
                u+=1			 
            if (i.isdigit()):
                d+=1
            if i.isalnum():		
                p+=1	
        if (l>=1 and u>=1 and p>=1 and d>=1 or l+p+u+d==len(password1)):
            if password1==password2:
                if len(password1)>=6 and len(password1)<=10:
                    if(os.path.isfile('userdetails.json')):
                        file_name=open("userdetails.json","r+")
                        a=json.load(file_name)
                        for i in a["User"]:
                            if i["Username"]==username:
                                print("This user already exist")
                                break
                        else:
                                dic,d={},{}
                                dic["Username"]=username
                                dic["Password"]=password1
                                d["Description"]=input("Enter what you feel:-")
                                d["DOB"]=input("Date of birth:-")
                                d["Gender"]=input("Gender:-")
                                d["Hobbies"]=input("Hobbies:-")
                                dic["Profile"]=d
                                v=a["User"]
                                v.append(dic)
                                f=open("userdetails.json","w+")
                                json.dump(a,f,indent=4)  
                                f.close()
                                print("Signup Successful")
                                   
                    else:
                            
                            dic,li,d,di={},[],{},{}
                            dic["Username"]=username
                            dic["Password"]=password1
                            d["Description"]=input("Enter what you feel:-")
                            d["Dob"]=input("Date of birth:-")
                            d["Gender"]=input("Gender:-")
                            d["Hobbies"]=input("Hobbies:-")
                            dic["Profile"]=d
                            li.append(dic)
                            di["User"]=li
                            f=open("userdetails.json","w+")
                            json.dump(di,f ,indent=4)
                            f.close()
                            print("Signup Successful")

                else:
                    print("password length must be between 6 and 10")
            else:
                print("Password not match")
        else:
            print("must have atleast a digit,specail character,lowercase and an uppercase")
    func_login_signup()
elif user_input=="b":
    a=open("userdetails.json","r")
    f=json.load(a)
    d=input("Enter your user name:-")
    v=input("Enter your password:-")
    for i in f["User"]:
        if i["Username"]==d:
            if v == i["Password"]:
                print("login successful")
                print(i)
                break
            else:
                print("wrong password")
    else:
        print("wrong username")
else:
    print("Your enter wrong input") 