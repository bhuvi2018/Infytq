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
