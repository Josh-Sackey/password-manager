#create an empty list to house key in unicode
k_ord=[]
#create an empty list to house value in unicode
v_ord=[]
#create an empty list to house summation of k_ord and v_ord
sum_list=[]
#define a function to ensure both variables are the same lengths
def match(list1,list2, key):
    #note we use key as third parameter because we only allow the key to change and not the value
    #if they are same length break out
    if len(list1)==len(list2):
        return
    #if they are not the same length execute this line
    for letter in key:
        #insert letters from key into list1 in order and check if lengths match
        list1.append(ord(letter))
        if len(list1)==len(list2):
            break
    #if after a the full key word has been added once, check if list 1 is still less than list and run match if true.
    if len(list1) < len(list2):
        match(list1,list2, key)

#define a function to encrypt data using some key and value       
def encrypt(key,value):
    #clear all list used before use
    k_ord.clear()
    v_ord.clear()
    sum_list.clear()
    #iterate through key and insert unicode form of letter in list
    for letter in key:
        k_ord.append(ord(letter))
    #iterate through value and insert unicode form of letter in list
    for letter in value:
        v_ord.append(ord(letter))
    #if key list elements are less than value list elements, match them    
    if len(k_ord)<len(v_ord):
        match(k_ord,v_ord, key)
    #sum up the elements of both lists in incremental order
        for i in range(len(v_ord)):
            sum_list.append(k_ord[i] + v_ord[i])
        return sum_list   
    else:
        #if not, just go ahead and sum up the elements of both lists in incremental order
        count=0
        for i in range(len(v_ord)):
            sum_list.append(k_ord[i] + v_ord[i])
            count+=1
            if count==len(v_ord):
                break
        return sum_list

#define a function to decrypt data    
def decrypt(k_ord, v_ord, key):
    original_list=[]
    #if key list elements are less than value list elements, match them.
    if len(k_ord)<len(v_ord):
        match(k_ord,v_ord, key)
        #find the difference of both list elements in incremental order and append in original list
        for i in range(len(v_ord)):
            original_list.append(v_ord[i] - k_ord[i])
    # if key list elements are not less that value list elements, find the difference of both list elements in incremental order and append in original list    
    else:
        count=0
    
        for i in range(len(v_ord)):
            original_list.append(v_ord[i] - k_ord[i])
            if count==len(v_ord):
                break
            
    #convert the characters in original list back from unicode and append in play.
    play=[]
    for i in range(len(original_list)):
        play.append(chr(original_list[i]))
    
    return play

if __name__ == "__main__":
    key= input("Enter a key to encrypt your data: ")
    sum_list=[]
    k_ord=[]
    for letter in key:
        k_ord.append(ord(letter))

    value=input ("Enter data you wish to be encrypted: ")
    v_ord=[]

    for letter in value:
        v_ord.append(ord(letter))
    encrypted_data=encrypt(k_ord, v_ord)
    decrypted_data=decrypt(k_ord,sum_list,key)
    print("your encrypted data=",encrypted_data)
    print("your decrypted data=",decrypted_data)

