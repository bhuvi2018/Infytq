#PF-Assgn-22
def find_leap_years(given_year):
    count=0
    list_of_leap_years=[None]*15
    
    # Write your logic here
    while(count<15):
        if(given_year%4==0):
            if(given_year%100==0):
                if(given_year%400==0):
                    list_of_leap_years[count]=given_year
                    count+=1
                    given_year+=1
                else:
                    given_year+=1
            else:
                list_of_leap_years[count]=given_year
                count+=1
                given_year+=1
        else:
            given_year+=1
        
    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)


#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    c=0
    #Write your logic here
    for i in range(0,len(reqd_gems)):
        for j in range(0,len(price_list)):
            if(gems_list[j]==reqd_gems[i]):
                bill_amount+=price_list[j]*reqd_quantity[i]
                c+=1
    if(c!=len(reqd_gems)):
        bill_amount=-1
    if(bill_amount>30000):
        bill_amount-=(bill_amount*5/100)
        
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)


#PF-Assgn-24
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    #Write your logic here
    for i in range(0,3):
    #Use the following messages to return the result wherever necessary
        if(num1+num2<=num3):
            return failure
            break
        if(num1+num3<=num2):
            return failure
            break
        if(num2+num3<=num1):
            return failure
            break
        return success

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)

#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    c=0

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    for i in range(0,heads+1):
        if(i*2+(heads-i)*4==legs):
            chicken_count=i
            rabbit_count=heads-i
            print(chicken_count,rabbit_count)
            c=1
    if(c==0):
        print(error_msg)
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(38,131)


import turtle           # allows us to use the turtles library
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle() 
alex.shape("turtle")    


alex.color("green")    
alex.right(60)         
alex.left(60)          
alex.circle(50)        
#draws circles
for counter in range(1,4):
    alex.circle(20*counter)
  
alex.color("blue")    
alex.right(120)         
alex.left(0)          
alex.circle(50)        
#draws circles
for counter in range(1,4):
    alex.circle(20*counter)
   
alex.color("red")    
alex.right(120)         
alex.left(0)          
alex.circle(50)        
#draws circles
for counter in range(1,4):
    alex.circle(20*counter)

#Write the logic to create the given pattern
#Refer the statements given above to draw the pattern


#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    if(num1>=num2):
        return max_num
    list=[]
    c=0
    
    # Write your logic here
    for i in range(num1,num2+1):
        if(i>=10 and i<=99):
            if(i%3==0 and i%5==0):
                list.append(i)
                c=1
    if(c==0):
        return max_num
    else:
        return list[-1]

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    if(num1>=num2):
        return max_num
    list=[]
    c=0
    
    # Write your logic here
    for i in range(num1,num2+1):
        if(i>=10 and i<=99):
            if(i%3==0 and i%5==0):
                list.append(i)
                c=1
    if(c==0):
        return max_num
    else:
        return list[-1]

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)


#PF-Exer-15

def find_sum_of_digits(number):
    sum_of_digits=0
    #Write your logic here
    while(number>0):
        rem=number%10
        number=number//10
        sum_of_digits+=rem
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(4521)
print("Sum of digits:",sum_of_digits)


//PF-Exer-16

num1=5
num2=10

//Write your code here
if(num1>num2)
{
    min=num2
}else
{
    min=num1
}
while(true)
{
    if(min%num1==0 && min%num2==0)
    {
        console.log(min);
        break
    }
    min++
}


#PF-Exer-18

def get_count(num_list):
    count=0

    # Write your logic here
    for i in range(0,len(num_list)-1):
        if(num_list[i]==num_list[i+1]):
            count+=1
    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))
