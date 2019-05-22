#PF-Exer-30

def find_average(mark_list):
	total=0
	for i in range(0, len(mark_list)):
		total+=mark_list[i]
	marks_avg=total/len(mark_list)
	return marks_avg

m_list=[1,2,3,4]
print("Average marks:", find_average(m_list))


#PF-Assgn-40
def is_palindrome(word):
    l=word.lower()
    r=l[::-1]
    if(l==r):
        return True
    else:
        return False
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")

