#!/usr/bin/env python

from traits.api import *
from traitsui.api import *
from pyface.api import *

global_count = 0

class Model(HasTraits):
    
    title = Str

class TNode(TreeNodeObject):

    model = Instance(Model())

    kids = List

    icon = Str # Special named trait which is listened by the Tree for icon changes.

    label = Str

    def _label_default(self):
        return str('label')

    def __repr__(self):
        return self.label
    
    def tno_get_label(self, node):
        #return self.label
        return ""

    def tno_has_children(self, node):
        return True

    def tno_get_children(self, node):
        return list(self.kids)

    def tno_get_icon(self, node, state):
        if self.model.title == 'example_equation_1':
            return 'equation_example_1.png'
        elif self.model.title == 'example_equation_2':
            return 'equation_example_2.png'
        elif self.model.title == 'Root':
            return 'rooted.png'
        else:
            return '<group>'

class ObjectTNode(ObjectTreeNode):

    # List of nodes this object applies to
    node_for = [ TNode ]

    # Name of trait for children
    children='kids'


class TView(HasTraits):
    root = Instance(TNode)
    sel = Instance(TNode)
    button = Event

    traits_view = View(
                      Group(
                          Item('root', 
                              editor=TreeEditor(
                                  nodes=[
                                      ObjectTNode(),
                                  ],
                                  selected = 'sel',
                                  hide_root=False,
                                  auto_open=2,
                                  editable=False,
                                  icon_size=(30,30),
                              ),
                          ),
                          show_labels=False,
                      ),
                      resizable=True,
    )

m1 = TNode(
        model=Model(title='example_equation_1',
                    children=['cat','dog','pet']),
        label='Eq. 1',
)

m2 = TNode(
        model=Model(title='example_equation_2',
                    children=['pig', 'cow'],),
        label='Eq. 2',
)

tree = TView(root= TNode(model=Model(title='Root'), kids=[m1, m2]) )

tree.configure_traits()

