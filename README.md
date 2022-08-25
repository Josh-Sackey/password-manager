welcome to my repository which contains three python files:
    password_manager.py
    encryptor.py
    scrapbook.py

password_manager.py
    the purpose of this code is to take information from the user and encrypt it, store it and later decrypt it at users request.
    This is done by taking a master password from the user and using that password to encrypt the rest of the data that the code would request.
    this code requests for four things:
        master password - To encrypt and decrypt all other data.
        platform -  To help organize all data e.g. facebook, instagram, or any other platform. This 
                    would not be encrypted
        username -  first information that would be encrypted as this would be the username
                    to login into the mentioned platform
        password -  last information that would be encrypted. This is your account password

    In running this code, you would be asked to add or view data. Add data would ask for the information above and run it through another python code "encryptor.py" then store in a txt file in an encrypted format. this file is named password.txt within the code and there is a txt file in this repository that you can review to have a fair understanding. The code of line to encrypt data is " *encryptor.encrypt(master_pwd, account_name)* ".

    By selecting view data, the line of code would take the master password to decrypt all the data stored in the txt file and print it out for the user.

    detailed information about the code had been made available within the code in the form of comments. Feel free to check it out if you want to work on this code.

encryptor.py
    the purpose of this code is to encrypt and decrypt any data provided a key is given to the code to encrypt the data. it can be used anywhere encryption and decryption is needed. an example of its usage can be found in *password_manager.txt*
    kindly review code to get details in the form of comments to understand the code.

scrapboook.py
    the file is there to serve two functions:
        this is for testing any random code before implementing it in the general code.
        this is for pulling out lines of code from the general code that is causing issues and testing it in an isolated environment.

I hope you find this code useful and feel free to reach out on any ways to make this code better.

