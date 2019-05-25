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
