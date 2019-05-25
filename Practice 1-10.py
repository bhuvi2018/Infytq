#PF-Prac-1
def add_string(str1):
  #start writing your code here
  if(len(str1)>=3):
        if(str1.endswith("ing")):
            str1=str1+"ly"
        else:
            str1=str1+"ing"
  
  return str1

str1="com"
print(add_string(str1))


#PF-Prac-2
def bracket_pattern(input_str):
    c1=input_str.count("(")
    c2=input_str.count(")")
    if(input_str.startswith(")") or input_str.endswith("(")):
        return False
    elif (c1==c2):
        return True
    else:
        return False
    
input_str="(())("
print(bracket_pattern(input_str))


#PF-Prac-3

def create_new_dictionary(prices):
    new_dict={}
    for key in prices:
        if(prices[key]>200):
            new_dict.__setitem__(key, prices[key])
    
    return new_dict

prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))


#PF-Prac-4
def find_nine(nums):
    for i in range(0,len(nums)):
        if(nums[i]==9 and i<4):
            return True
    return False
    

nums=[1,9,4,5,6]
print(find_nine(nums))


#PF-Prac-5
def count_digits_letters(sentence):
    l=[]
    c1=0
    c2=0
    for i in sentence:
        if(ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122):
            c1+=1
        elif((ord(i)>=0 or ord(i)<=9) and not(i==" ")):            
            c2+=1
    l.append(c1)
    l.append(c2)
    return l

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))



#PF-Prac-6
def list123(nums):
    for i in range(0,len(nums)-1):
        if(nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
                return True
    return False

    
nums=[1,2,3,4,5]
print(list123(nums))
