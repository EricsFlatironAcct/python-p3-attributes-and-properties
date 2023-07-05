#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Bob", job="Admin"):
        self.set_name(name)
        self.set_job(job)

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        if isinstance(name, str) and (0<len(name)<25):
            self.name = ' '.join(name.capitalize() for name in name.split(" "))
        else: 
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self.job

    def set_job(self, job):
        self.job = job if job in APPROVED_JOBS else print("Job must be in list of approved jobs.")