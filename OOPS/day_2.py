#OOPR-Exer-6
#Start writing your code here
                                            
class Vehicle:
    def __init__(self):
        self.mileage=12
        self.fuel_left=6
    
    def identify_distance_that_can_be_travelled(self):
        if(self.fuel_left<=5):
            return 0
        else:
            return (self.fuel_left-5)*self.mileage
        
    def identify_distance_travelled(self,initial_fuel):
        initial_fuel-=self.fuel_left
        r=initial_fuel*self.mileage
        return r

s=Vehicle()
print(s.identify_distance_that_can_be_travelled())
print(s.identify_distance_travelled(35))


#OOPR-Assgn-10
class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        k=0
        s=[]
        self.list_of_call_objects=[]
        for i in list_of_call_string:
            s=i.split(",")
            CallDetail_k=CallDetail(s[0],s[1],s[2],s[3])
            self.list_of_call_objects.append(CallDetail_k)
        k+=1

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)


#OOPR-Assgn-12
#Start writing your code here
class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.__bill_amount=0
        
    def get_bill_id(self):
        return self.__bill_id
    
    def get_patient_name(self):
        return self.__patient_name
        
    def get_bill_amount(self):
        return self.__bill_amount
        
    def calculate_bill_amount(self,consultation_fees,quantity_list,price_list):
        self.__bill_amount=consultation_fees
        for i in range(0,len(quantity_list)):
            self.__bill_amount+=(quantity_list[i]*price_list[i])
    
b=Bill(20,"John")
p=[99,88,77,55]
q=[1,2,3,4]
c=100
b.calculate_bill_amount(c,q,p)
print(b.get_bill_id())
print(b.get_patient_name())
print(b.get_bill_amount())
