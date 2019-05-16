num = input();
count = 0;
number = int(num)
for i in range(1, number+1):
    if number%i == 0:
        count += 1
    i += 1
if count==0:
    print(number,"is a prime number.")
else:
    print(count)
