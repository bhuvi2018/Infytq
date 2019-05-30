#PF-Prac-42
def maxvalue_in_column(pixel_grid):
    result_list = [0] * len(pixel_grid[0])
    for item in pixel_grid:
        temp = item
        for i in range(0,len(item)):
            if result_list[i]  < temp[i]:
                result_list[i] = temp[i]
    #start writing your code here
    return result_list

pixel_grid=[[ 4, 2, 3], 
            [16, 5, 0],
            [ 3, 200, 6], 
            [ 0, 10, 12]] 
pixel_grid1=[[ 4 ], 
             [ 16 ], 
             [ 3 ], 
             [ 0 ]]
pixel_grid2=[[ 4, 2, 3]]
pixel_grid3= [[6]] 

print("Pixel grid is:")
for i in pixel_grid:
    print(i)
output=maxvalue_in_column(pixel_grid)
print("The maximum values of each column are:",output)


#PF-Tryout 46

def doublePreceding (values):
    if len(values) > 0:
        previous = values[0]
        values[0] = 0
        for idx in range(1, len(values)):
            previous1 = values[idx]
            values[idx] = 2 * previous
            previous=previous1
    return values
    
print(doublePreceding([3,8,2]))


#46_hackerrank
b=input()
b=b.split(" ")
def double(v):
    if len(v) > 0:
        pre = int(v[0])
        v[0] = 0
        for i in range(1, len(v)):
            temp=int(v[i])
            v[i] = 2 * int(pre)
            pre = temp
    return v
bb=double(b)
for i in bb:
    print(i,end=" ")
