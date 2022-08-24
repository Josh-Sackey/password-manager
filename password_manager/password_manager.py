import encryptor
master_pwd=input("what is the masterpassword? ") 
def add():
    platform=input("what platform does this account belong to? ")
    account_name= input("what is your account name? ")
    pwd= input("what is your password? ")
    encrypted_username=encryptor.encrypt(master_pwd, account_name)
    username='/'.join([str(item) for item in encrypted_username])
    encrypted_password=encryptor.encrypt(master_pwd, pwd)
    password='/'.join([str(item) for item in encrypted_password])
    with open ("password.txt","a") as f:
        f.write(platform +"|"+ username +"|"+ password +"\n")
    
def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data= line.rstrip()
            site,name,passw=data.split("|")
            name= name.split("/")
            passw= passw.split("/")
            k_ord=[]
            for letter in master_pwd:
                k_ord.append(ord(letter))
            name= [int(x) for x in name]    
            decrypted_username= encryptor.decrypt(k_ord, name, master_pwd)
            username=''.join([str(item) for item in decrypted_username])

            passw= [int(x) for x in passw]    
            decrypted_password= encryptor.decrypt(k_ord, passw, master_pwd)
            password=''.join([str(item) for item in decrypted_password])
            
            print("Platform:",site,"\nAccount Name:",username,"\nPassword:",password,"\n")

while True:
    mode=input("would you like to add a password or view your password list (view/add)? press q to quit. ").lower()
    if mode== "q":
        print("your data is safe here. \nBye")
        break
    if mode=="add":
        add()
    elif mode== "view":
        view()
    else:
        continue