# -*- coding: utf-8 -*-
class Flight():
    def __init__(self, total_passengers):
        self.total_passengers = total_passengers
        self.passengers = []
    
    def add_passenger(self, name):
        if self.open_seats() == 0:
            return False

        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.total_passengers - len(self.passengers)
    
flightA = Flight(3)

#print(flightA.total_passengers)

persons = ["Harry", "Ron", "Hermione", "Neville"]
for person in persons:
    success = flightA.add_passenger(person)
    if success:
        print(f"added {person} to flight successfully")
    else :
        print(f"no seat for {person}")