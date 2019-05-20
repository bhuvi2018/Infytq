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


#PF-Assgn-35

#Global variable
list_of_marks=[12,18,25,24,2,5,18,20,20,21]

def find_more_than_average():
    avg=0
    sum=0
    c=0
    for i in range(0,len(list_of_marks)):
        sum+=list_of_marks[i]
    avg=sum/len(list_of_marks)
    for i in range(0,len(list_of_marks)):
        if(avg<list_of_marks[i]):
            c+=1
    avg=c/len(list_of_marks)*100
    return avg

def sort_marks():
    list_of_marks.sort()
    return list_of_marks

def generate_frequency():
    listt=[]
    for i in range(0,26):
        c=0
        for j in range(0,len(list_of_marks)):
            if (list_of_marks[j]==i):
                c+=1
        listt.append(c)
    return listt

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())

#PF-Assgn-36
def create_largest_number(number_list):
    ans=""
    number_list.sort()
    for i in range(len(number_list)-1,-1,-1):
        ans+=str(number_list[i])
        an=int(ans)
    return an

number_list=[23,34,55]
largest_number=create_largest_number(number_list)
print(largest_number)


#PF-Assgn-37

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    sum=0
    for i in range(0,len(chocolates_received)):
        sum+=chocolates_received[i]
    return sum

def reward_child(child_id_rewarded,extra_chocolates):
    c=0
    if(extra_chocolates<1):
        print("Extra chocolates is less than 1")
    else:
        for i in range(0,len(child_id)):
            if(child_id[i]==child_id_rewarded):
                chocolates_received[i]+=extra_chocolates
                c=1
        if(c==1):
            print(chocolates_received)
        else:
            print("Child id is invalid")


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
    #print(chocolates_received)


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)


#PF-Assgn-38

def check_double(number):
    ss=[]
    kk=[]
    s=number
    k=number*2
    c=0
    if(len(str(s))==len(str(k))):
        while s!=0:
            t1=s%10
            s=s//10
            t2=k%10
            k=k//10
            ss.append(t1)
            kk.append(t2)
        ss.sort()
        kk.sort()
        for i in range(0,len(kk)):
                if(kk[i]==ss[i]):
                    c+=1
    else:
        return False

    if(c==len(ss)):
        return True
    else:
        return False

#Provide different values for number and test your program
print(check_double(125874))
