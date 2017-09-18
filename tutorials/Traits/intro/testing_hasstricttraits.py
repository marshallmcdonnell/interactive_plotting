#!/usr/bin/env python  

from traits.api import HasStrictTraits, Float
from mock import Mock

class MyClass(HasStrictTraits):

    number = Float(2.0)

    def add_to_number(self, value):
        """ Add the value to `number`. """
        self.number += value

my_class = MyClass()

# Using my_class.add_to_number = Mock() will fail.
# But setting the mock on the instance `__dict__` works.
my_class.__dict__['add_to_number'] = Mock()

# We can now use the mock in our tests.
my_class.add_to_number(42)
print my_class.add_to_number.call_args_list
