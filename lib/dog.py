#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:     
    def __init__(self, name="Doggo", breed="Mastiff"):
        self.set_name(name)
        self.set_breed(breed)

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name= name.title() if isinstance(name, str) and (0<len(name)<25) else print("Name must be string between 1 and 25 characters.")
            
    def get_breed(self):
        return self.breed
    
    def set_breed(self, breed):
        self.breed = breed if breed in APPROVED_BREEDS else print("Breed must be in list of approved breeds.")

