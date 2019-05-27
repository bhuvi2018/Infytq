#PF-Assgn-57
def check_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, number))
    
def rotations(num):
    rotated = []
    m = str(num)
    for i in m:
        rotated.append(int(m))
        m = m[1:] + m[0]
    return rotated

def get_circular_prime_count(limit):
    counter = 0 

    for number in range(1, limit):
        if all(check_prime(number) for number in rotations(number)): 
            counter += 1 
    return counter
#Provide different values for limit and test your program
print(get_circular_prime_count(1000))
