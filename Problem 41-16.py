#PF-Tryout

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
