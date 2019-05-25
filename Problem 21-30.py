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
