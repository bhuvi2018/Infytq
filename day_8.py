#PF-Tryout EX 36
import re

flight_details="Good Evening, Welcome to British Airways. Your flight number is ba8004. Flight departure time is 16:45"

#This function returns the values in the search result
def printout(search_result):
    if(search_result!=None):
        return search_result.group()
    else:
        return "No Output"

search_result =re.search(r"British Airways",flight_details) 
#This will invoke the printout() and displays the search result values
print(printout(search_result))

search_result = re.search(r"16:45$",flight_details)
print(printout(search_result))

search_result = re.search(r"^G",flight_details) 
print(printout(search_result))

search_result =re.search(r"F.....",flight_details) 
print(printout(search_result))


print(re.sub(r"ba(\d{4})",r"BA\1",flight_details))
                                          


#PF-Exer-38
#This verification is based on string match.
import math

num1=36
num2=7
num3=18

calc =lambda x,y: (x%y)+(x-y)
print(calc(num1,num2))

square_root = lambda x:math.sqrt(x)
print(square_root(num3))

square_root2= lambda x:math.sqrt(x)
print(square_root2(num3))


#PF-Exer-39
#This verification is based on string match.

principal_amount=4000
duration=12
rate_of_interest=13

simple_interest = lambda x,y,z:(x*y*z)/100

if(simple_interest(principal_amount,duration,rate_of_interest)>1000):
    print("Platinum Member")
else:
    print("Gold Member")
    
    
#PF-Exer-40
#This verification is based on string match.

num1=20
num2=30

div =lambda x,y:x+y

if(div(num1,num2)%10)==0:
    print("Divisible by 10")
else:
    print("Not Divisible by 10")

    
#PF-Exer-41
#This verification is based on string match.

def sum_all(function, data):
    sum=0
    for i in data:
        if(function(i)==1):
            sum+=i
    return sum

list_of_nos=[100,200,300,500,1040]

greater =lambda x: x>10

divide = lambda s: s%10==0 and s<=100

range_of_values = lambda s: s>=25 and s<=50


#Use the below given print statements to display the output
# Also, do not modify them for verification to work
print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))


#PF-Assgn-52 "ERROR"

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    sum=0
    if(filter_func==None):
        for i in list_of_num:
            sum+=i
    else:
        s=[]
        s=filter_func(list_of_num)
        for i in s:
            sum+=i
    return sum

def even(data):
    ev=[]
    for i in data:
        if(i%2==0):
            ev.append(i)
    return ev

def odd(data):
    od=[]
    for i in data:
        if(i%2!=0):
            od.append(i)
    return od

sample_data = range(1,11)

print(sum_of_numbers(sample_data,None))
