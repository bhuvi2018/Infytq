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
