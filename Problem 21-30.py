'''
Write a python function to print the given number of diagonal lines of stars.
Sample input: 5

Expected output: 
* 
.* 
..* 
...* 
....* 
Note: Setting the end parameter of the print function to empty string prevents the issuing of the new line.
Example: print(".",end="") will maintain the cursor in the same line after displaying "."
'''

#PF-Tryout 22
def diagonal_stars(number):
   #start writing your code here
    for i in range(0,number):
        for j in range(i):
            print(".",end="")
        print("*")

number=6    
diagonal_stars(number)


#PF-Prac-23
def divisible_by_sum(number):
    temp=number
    sum=0
    while(number>0):
        rem=number%10
        number=number//10
        sum+=rem
    if(temp%sum==0):
        return True
    else:
        return False


#PF-Prac-24
def find_gcd(num1,num2):
    if(num2==0): 
        return num1
    else:
        return find_gcd(num2,num1%num2)

num1=45
num2=9
print(find_gcd(num1,num2))


#PF-Prac-25
def list_of_count(word_list):
    count_list=[]
    for i in word_list:
        count_list.append(len(i))
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))


#PF-Prac-26
def check_occurence(string):
    string=string.lower()
    c=string.count("mat")
    cc=string.count("jet")
    if(c==cc):
        return True
    else:
        return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))


#PF-Prac-27
def check_for_ten(num1,num2):
    if(num1==10 or num2==10 or num1+num2==10):
        return True
    else:
        return False
    
print(check_for_ten(10,9))


#PF-Tryout 28
def sing_99_bottles():
   for i in range(99,0,-1):
        print(i,end="")
        print(" bottles of beer on the wall, ",end="")
        print(i,end="") 
        print(" bottles of beer.")
        print("Take one down, pass it around, ",end="")
        print(int(i-1),end="")
        print(" bottles of beer on the wall.")
   
sing_99_bottles()


#PF-Prac-29
def exchange_list(number_list):
    #start writing your code here
    d=len(number_list)
    a=len(number_list)//2
    b=a//2+a
    k=0
    for i in range(a,b):
        c=number_list[i]
        number_list[i]=number_list[d-k-1]
        number_list[d-k-1]=c
    for i in range(a):
        temp=number_list[i]
        number_list[i]=number_list[i+a]
        number_list[i+a]=temp
    return number_list

    
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))
