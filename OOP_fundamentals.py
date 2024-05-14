# OOP Fundamentals
# 1. City Infastructure Management System
"""Objective:
The aim of this assignment is to apply the concepts of Object-Oriented 
Programming in Python to build a simulated City Infrastructure 
Management System. This system will incorporate classes, objects, 
methods, and data structures to manage different aspects of a city, 
such as buildings, traffic, and events.
"""
# Task 1: Vehicle Registration System
"""Problem Statement: Create a Python class Vehicle with attributes 
registration_number, type, and owner. Implement a method update_owner 
to change the vehicle's owner. Then, create a few instances of Vehicle 
and demonstrate changing the owner. Code Example: Provide a basic 
structure for the Vehicle class without methods.
"""
"""class Vehicle:
def init(self, reg_num, type, owner):
self.registration_number = reg_num
self.type = type
self.owner = owner
"""
"""Expected Outcome: Completion of the Vehicle class with the 
update_owner method and a demonstration script showing the creation 
of Vehicle objects and updating their owners.
"""
class Vehicle:
    def __init__(self, reg_number, make, model, year, owner):
        self.reg_number = reg_number
        self.make = make
        self.model= model
        self.year = year
        self.owner = owner
    def change_owner(self, owner):
        self.owner = owner
        print(f"The new owner is {owner}")
my_info = Vehicle("TX1235", "Toyota", "Camry", 2011, "Chris Nicki")
print(my_info.owner)
print(my_info.year)
print(my_info.make)
my_info.change_owner("John Johnson")


# Task 2: Event Management System Enhancement
"""Problem Statement: Extend an existing Event class by adding a feature to keep track of the number 
of participants. Implement a method add_participant that increases the count and a method 
get_participant_count to retrieve the current count.
"""
"""Code Example: Basic Event class without participant tracking.
class Event:
def init(self, name, date):
self.name = name
self.date = date
"""
class Event:
    def __init__(self, name, guests):
        self.name = name
        self.guests = guests
        self.participants = []
    def add_participant(self, participant ):
        print(f"We've added {participant} to the event!")
        self.participants.append(participant)
        self.guests += 1
    def remove_participant(self, participant):
        print(f"We've removed {participant} from the event!")
        self.participants.append(participant)
        self.guests -= 1
party = Event("Chris Nicki", 30)
print(party.name)
party.add_participant("Hank")
print(party.guests)  
party.add_participant("John")
print(party.guests)
party.remove_participant("Hank")
print(party.guests)