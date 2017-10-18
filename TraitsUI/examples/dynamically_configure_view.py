#! /usr/bin/env python

'Test case, showing solution to dynamically constructed view problem.'

from traits.api   import HasTraits, String
from traitsui.api import View, Item

class DynamicViewTester(HasTraits):
    'Dynamically construct its View, using default_traits_view().'

    def __init__(self, *args, **traits):
        super(DynamicViewTester, self).__init__(*args, **traits)

        # Here is where I'll parse the input file, constructing 'content' accordingly.
        content = []
        content.append(Item(label='Hello, World!'))
        content.append(Item(label='Goodbye, World.'))

        self._content = content

    def default_traits_view(self):
        view = View(
            title='Dynamically Assembled View',
            height=0.4,
            width=0.4,
        )
        view.set_content(self._content)
        return view

if(__name__ == '__main__'):
    DynamicViewTester().configure_traits()
