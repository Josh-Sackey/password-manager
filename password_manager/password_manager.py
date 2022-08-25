#importing the encryptor tool to encrypt and decrypt our data
import encryptor
master_pwd=input("what is the masterpassword? ") 
def add():
    platform=input("what platform does this account belong to? ")
    account_name= input("what is your account name? ")
    pwd= input("what is your password? ")
    #line to encrypt account name using master password
    encrypted_username=encryptor.encrypt(master_pwd, account_name)
    #a list of encrypted data is returned and this line is to convert back into a string and join them using '/'
    username='/'.join([str(item) for item in encrypted_username])
    #line to encrypt password using master password
    encrypted_password=encryptor.encrypt(master_pwd, pwd)
    #a list of encrypted data is returned and this line is to convert back into a string and join them using '/'
    password='/'.join([str(item) for item in encrypted_password])
    #open password.txt if it exist or create password.txt if it doesn't
    with open ("password.txt","a") as f:
        #append information in text separating each data with "|""
        f.write(platform +"|"+ username +"|"+ password +"\n")
    
def view():
    #Open password.txt and read data in it
    with open("password.txt","r") as f:
        #this line of code is to pick a line and split it up based on "|" and store it in the order of site, name and password
        for line in f.readlines():
            data= line.rstrip()
            site,name,passw=data.split("|")
            name= name.split("/")
            passw= passw.split("/")
            #this line of code is prepare data to be decrypted as decryption requires three variables
            #k_ord would be a list that would store master password in unicode and push it to encryptor.py
            k_ord=[]
            for letter in master_pwd:
                k_ord.append(ord(letter))
            # since this data was taken from the txt file, it is seen as a string, so we need to convert it back to an integer
            name= [int(x) for x in name] 
            # this is the line of code to decrypt data   
            decrypted_username= encryptor.decrypt(k_ord, name, master_pwd)
            username=''.join([str(item) for item in decrypted_username])

            passw= [int(x) for x in passw]    
            decrypted_password= encryptor.decrypt(k_ord, passw, master_pwd)
            password=''.join([str(item) for item in decrypted_password])
            
            #we can now print out our decrypted data in the format below
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