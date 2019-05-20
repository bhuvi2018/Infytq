//PF-Exer-24
//This verification is based on string match.

package main
import ("fmt")
func main() {
    var num int=find_square(3);
    fmt.Println(num);
}

func find_square(i int)int {
    return i*i;
}


//JS-Exer-25

//Start writing your code here
function display(a){
    return a*(a+1)/2;
}

console.log(display(6));


#PF-Assgn-29
def calculate(distance,no_of_passengers):
    ticket=no_of_passengers*80
    dis=distance*7
    if(dis>ticket):
        return -1
    else:
        return ticket-dis
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))


#PF-Assgn-30

def encode(message):
    #Remove pass and write your logic here
    c=0
    s=message[0]
    ans=""
    for i in range(0,len(message)):
        if(message[i]==s):
            c+=1
        else:
            ans+=str(c)+s
            s=message[i]
            c=1
        if(int(i)==len(message)-1):
            ans+=str(c)+s
        
    return ans        
        
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCB")
print(encoded_message)


#PF-Assgn-31
def check_palindrome(word):
    rev=word[::-1]
    if(rev==word):
        return True
    else:
        return False
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
    
    
#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    c1=0
    c2=0
    c3=0
    for i in range(1,len(patient_medical_speciality_list),2):
        if(patient_medical_speciality_list[i]=='P'):
            c1+=1
        elif(patient_medical_speciality_list[i]=='O'):
            c2+=1
        elif(patient_medical_speciality_list[i]=='E'):
            c3+=1
    if(c1>c2 and c1>c3):
        speciality=medical_speciality['P']
    elif c2<c3:
        speciality=medical_speciality['E']
    else:
        speciality=medical_speciality['O']

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)


#PF-Assgn-33

def find_common_characters(msg1,msg2):
     #Remove pass and write your logic here
     ans=""
     c=0
     for i in range(0,len(msg1)):
         for j in range(0,len(msg2)):
             if(msg1[i]!=" " and msg1[i]==msg2[j]):
                  if(msg1[i] in ans):
                      continue
                  else:
                    ans+=msg1[i]
                    c=1
     if(c==0):
        return -1
     return ans
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)+


