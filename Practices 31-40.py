#PF-Prac-31
def sum_of_elements(num_list,number):
    a=len(num_list)
    result_sum=0
    for i in range(1,a-1):
        if(num_list[i-1]!=number and num_list[i+1]!=number and num_list[i]!=number):
            result_sum+=num_list[i]
    if(num_list[1]!=number and num_list[0]!=number):
        result_sum+=num_list[0]
    if(num_list[a-2]!=number and num_list[a-1]!=number):
        result_sum+=num_list[a-1]
    return result_sum
      
num_list=[1,2,1,2]
number=2
print(sum_of_elements(num_list, number))

#PF-Prac-32
def check_squares(number):
    for i in range(1,10000):
        for j in range(i+1,10000):
            if(i*i + j*j ==number):
                return True
    return False


number=68
print(check_squares(number))


#PF-Prac-37
def sum_of_list(num_list):
    if(len(num_list)>1):
        return num_list[0] + sum_of_list(num_list[1:])
    else:
        return num_list[0]
num_list=[44,23,77,11,89,3]
result=sum_of_list(num_list)
print("Sum of the elements:",result)


#PF-Prac-38
def build_index_grid(rows, columns):
    result_list=[]
    s=""
    for i in range(0,rows):
        for j in range(0,columns):
            if(i==0 and j==0):
                s=s+"["
            if(j==0):
                s=s+"["
            s=s+"'"+str(i)+","+str(j)+"'"
            if(j!=(columns-1)):
                s=s+","
            if(j==(columns-1) and j==(columns-1) and i!=(rows-1)):
                s=s+"],"
            if(j==(columns-1) and i==(rows-1)):
                s=s+"]]"
        result_list.append(s)
        s=""
    return result_list

rows=4
columns=3
result=build_index_grid(rows,columns)
print("Rows:",rows,"Columns:",columns)
print("The matrix is:",result)
for i in result:
    print(i)
