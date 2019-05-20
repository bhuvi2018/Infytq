#PF-Exer-26

def factorial(number):
    fact=1
    for i in range(1,number+1):
        fact*=i
    return fact
def find_strong_numbers(num_list):
    strong_num_list=[]
    for i in num_list:
        temp=i
        sum=0
        if(temp==0):
            continue
        else:
            while i!=0:
                num=i%10
                sum+=factorial(num)
                i=i//10
            if(sum==temp):
                strong_num_list.append(temp)
    return strong_num_list

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)


#PF-Exer-28
                                              
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    c1=0
    c2=0
    for i in match_tuple:
        if(i=="Team1"):
            c1+=1
        else:
            c2+=1
    if(c1>c2):
        return "Team1"
    elif(c1<c2):
        return "Team2"
    else:
        return "Tie"

#Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))
#print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))


#PF-Exer-29
def merge_lists(list1,list2):
    #Write your logic here
    new_merge_list=[]
    for i in range(0,len(list1)):
        new_merge_list.append(list1[i])
    for i in range(0,len(list2)):
        new_merge_list.append(list2[i])

    return new_merge_list
def sort_list(merged_list):
    #Write your logic here
    merged_list.sort()
    return merged_list

#Provide different values for list1 and list2 and test your program
merged_list=merge_lists(list1=[1,2,3,4,1] ,list2=[2,3,4,5,4,6])
print(merged_list)
sorted_merged_list=sort_list(merged_list)
print(sorted_merged_list)


#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    c=0
    for i in range(0,len(num_list)):
        for j in range(i+1,len(num_list)):
            if(num_list[i]+num_list[j]==n):
                c+=1
    return c
num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))
