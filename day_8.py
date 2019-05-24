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
