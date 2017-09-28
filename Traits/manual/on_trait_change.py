#!/usr/bin/env python


from traits.api import *


class Employee(HasTraits):
    name = Str
    sick_days = Int

class Department(HasTraits):
    name = Str
    employees = List(Employee)

class Corporation(HasTraits):
    name = Str
    departments = List(Department)

    # Define a corporate 'whistle blower' method:
    @on_trait_change('departments:employees.sick_days')
    def sick_again(self, object, name, old, new):
        print '%s just took sick day number %d for this year!' % (
              object.name, new)


# Create some sample employees:
millie = Employee(name='Millie', sick_days=2)
ralph = Employee(name='Ralph', sick_days=3)
tom = Employee(name='Tom', sick_days=1)
slick = Employee(name='Slick', sick_days=16)
marcelle = Employee(name='Marcelle', sick_days=7)
reggie = Employee(name='Reggie', sick_days=11)
dave = Employee(name='Dave', sick_days=0)
bob = Employee(name='Bob', sick_days=1)
alphonse = Employee(name='Alphonse', sick_days=5)

# Create some sample departments:
accounting = Department(name='accounting',
                        employees=[millie, ralph, tom])

sales = Department(name='Sales',
                   employees=[slick, marcelle, reggie])

development = Department(name='Development',
                         employees=[dave, bob, alphonse])

# Create a sample corporation:
acme = Corporation(name='Acme, Inc.',
                   departments=[accounting, sales, development])

# Now let's try out our 'reporting' system:
slick.sick_days += 1
reggie.sick_days += 1
