#PF-Exer-30

def find_average(mark_list):
	total=0
	for i in range(0, len(mark_list)):
		total+=mark_list[i]
	marks_avg=total/len(mark_list)
	return marks_avg

m_list=[1,2,3,4]
print("Average marks:", find_average(m_list))


#PF-Assgn-40
def is_palindrome(word):
    l=word.lower()
    r=l[::-1]
    if(l==r):
        return True
    else:
        return False
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")


#PF-Assgn-41
def find_ten_substring(num_str):
    ret=[]
    for i in range(0,len(num_str)):
        sum=int(num_str[i])
        for j in range(i+1,len(num_str)):
            sum+=int(num_str[j])
            if(sum==10):
                ret.append(num_str[i:j+1])
    return ret[::-1]

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)


#PF-Assgn-42
def find_factors(num):
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    max=0
    for i in range(0,len(list_of_factors)):
        if(max<list_of_factors[i]and is_prime(list_of_factors[i],list_of_factors[i]-1)):
            max=list_of_factors[i]
    return max

def find_f(num):
    list_of_factors=find_factors(num)
    return find_largest_prime_factor(list_of_factors)

def find_g(num):
    g=find_f(num)+find_f(num+1)+find_f(num+2)+find_f(num+3)+find_f(num+4)+find_f(num+5)+find_f(num+6)+find_f(num+7)+find_f(num+8)
    return g

print(find_g(10))
