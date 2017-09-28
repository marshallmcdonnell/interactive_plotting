#!/usr/bin/env python 

# override_default.py -- Example of overriding a default value for
#                        a trait attribute in a subclass
from traits.api import HasTraits, Range, Str

class Employee(HasTraits):
    name = Str
    salary_grade = Range(value=1, low=1, high=10)

class Manager(Employee):
    salary_grade = 5

employee = Employee()
manager = Manager()

print employee.salary_grade
print manager.salary_grade
