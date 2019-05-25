#PF-Prac-11
def find_upper_and_lower(sentence):
    #start writing your code here
    up=0
    lo=0
    for i in sentence:
        if(i>="a" and i<="z"):
            lo+=1
        if(i>="A" and i<="Z"):
            up+=1
    result_list=[]
    result_list.append(up)
    result_list.append(lo)

    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))


#PF-Prac-12
def generate_sentences(subjects,verbs,objects):
    sentence_list=[]
    for i in subjects:
        for j in verbs:
	        for k in objects:
	            sentence_list.append(i+" "+j+" "+k)
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))


#PF-Tryout
def find_five_digit():
    num2=0
    num3=0
    num4=0
    num5=0
    for i in range(9,-1,-1):
        num2=int(i-2)
        num3=int(num2-2)
        num4=int(num3-2)
        num5=int(num3)
        if(num3+num4+num5==i and num2+num3+num4+num5+i==19):
            break
    s=str(i)+str(num2)+str(num3)+str(num4)+str(num5)
    print(s)

find_five_digit()
