#perfect number is a number whose divisors sum to the same number

n = int(input())
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")

    
#Perfect number bet an interval

llimit=int(input())
ulimit = int(input())

for n in range(llimit, ulimit + 1):
    sum = 0
    for divisor in range(1, n):
        if not n % divisor:
            sum += divisor
    if sum==n:
        print(n, "is a perfect number")
