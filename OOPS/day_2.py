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
