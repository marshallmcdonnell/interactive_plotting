#!/usr/bin/env python 

# handler_override.py -- Example of a Handler that overrides
#                        setattr(), and that has a user interface
#                        notification method

from traits.api import HasTraits, Bool
from traitsui.api import View, Handler


# Controller
class TC_Handler(Handler):

    def setattr(self, info, object, name, value):
        Handler.setattr(self, info, object, name, value)
        info.object._updated = True

    def object__updated_changed(self, info):
        if info.initialized:
            info.ui.title += "*"

# Model
class TestClass(HasTraits):
    b1 = Bool
    b2 = Bool
    b3 = Bool
    _updated = Bool(False)

# View
view1 = View('b1', 'b2', 'b3',
             title="Alter Title",
             handler=TC_Handler(),
             buttons = ['OK', 'Cancel'])

tc = TestClass()
tc.configure_traits(view=view1)
