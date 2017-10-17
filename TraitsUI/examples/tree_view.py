#!/usr/bin/env python

from traits.api import *
from traitsui.api import *

global_count = 0

class TNode(TreeNodeObject):
    count = 0
    files = List
    label = Str
    something = Int
    icon = Int # Special named trait which is listened by the Tree for icon changes.
    def _files_default(self):
        return [TNode()]
    def _label_default(self):
        TNode.count += 1
        return str(TNode.count)
    def __repr__(self):
        return self.label
    
    def tno_get_label(self, node):
        return self.label

    def tno_has_children(self, node):
        return True

    def tno_get_children(self, node):
        return list(self.files)

    def tno_get_icon(self, node, state):
        global global_count
        global_count += 1
        print 'in tno_get_icon: node = ',self.tno_get_label(node)
        if global_count % 3:
            return '<group>'
        else:
            return 'img.png'

class TView(HasTraits):
    root = Instance(TNode)
    sel = Instance(TNode)
    button = Event

    traits_view = View(Group(
                      Item('root', editor=TreeEditor(
                            nodes=[ObjectTreeNode(node_for = [ TNode ],
                                   children='something',
                             )],
                        selected = 'sel',
                        hide_root=True,
                        auto_open=2,
                        editable=False,
                        ),
                     ),
                Item('button', editor=ButtonEditor(label='Click to change icon')),
                show_labels=False,),
                resizable=True,)

    def _button_fired(self):
        self.sel.icon += 1

m = TView(root=TNode(files=[TNode(),TNode(),TNode(),TNode()]))
m.configure_traits()

