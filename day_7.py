#PF-Tryout ex 33

def guess_number(number_in_mind):
     # remove pass and write your logic here
     if(number_in_mind<5):
         print ('Number is low')
     elif(number_in_mind>5):
         print ('Number is high')
     else:
         print('You have got it right!!!')
#use the print statements given below wherever applicable
#print ('Number is low')
#print ('Number is high')
#print ('You have got it right!!!')

#Provide different values for number_in_mind and test your program
guess_number(4)


#PF-Exer-34
def find_number_of_combination(number_of_flavours):
    total_combination=0
    total_combination=2**number_of_flavours #power(**)
    return total_combination

number_of_combination=find_number_of_combination(6)
print(number_of_combination)


#PF-Exer-35

def count_names(name_list):
    count1=0
    count2=0
    for i in range(0,len(name_list)):
        if(name_list[i].endswith("at") and name_list[i].find("at")!=0):
            count1+=1
        if(name_list[i].count("at")!=0):
            count2+=1
    #start writing your code here
    #Populate the variables: count1 and count2

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print("_at -> ",count1)
    print("%at% -> ",count2)


#Provide different names in the list and test your program
name_list=[Hat, Cat, Rabbit, Matter]
count_names(name_list)


#PF-Assgn-46

def nearest_palindrome(number):
    f=True
    while(f):
        number+=1
        s=str(number)
        s1=s[::-1]
        if(s==s1):
            f=False
    return number

number=12300
print(nearest_palindrome(number))


#PF-Assgn-47
def encrypt_sentence(sentence):
    sentence=sentence
    s=""
    list=[]
    list=sentence.split(" ")
    for i in range(0,len(list)):
        if((i+1)%2!=0):
            a=list[i]
            list[i]=a[::-1]
        else:
            v=""
            c=""
            for j in list[i]:
                if(j=="a" or j=="e" or j=="i" or j=="o" or j=="u"):
                    v+=j
                else:
                    c+=j
            list[i]=c+v
    for i in range(0,len(list)):
        s+=list[i]
        if(i!=len(list)-1):
            s+=" "
        
    return s

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
