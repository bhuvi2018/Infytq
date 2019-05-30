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
