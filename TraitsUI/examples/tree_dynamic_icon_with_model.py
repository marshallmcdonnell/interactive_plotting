#!/usr/bin/env python
'''
This shows how to create a tree node that can set it icon based on
an attribute of the class it represents.
    i.e. the TModel class has a title which is used to set the
         tree node (TNode) icon image

Also, this shows how to integrate the TreeNodeObject and ObjectTreeNode
needed for this implementation with "regular" TreeNode of the tree.

We have the hierarchy:

-----------------
|Tree Structure |
-----------------

    Node      Class           represents Model
    --------  ---------       -----------------
    RootNode  TreeNode        RootModel
      |
    TNode     TreeNodeObject  TModel
      |
    LeafNode  TreeNode        LeafModel

'''


from traits.api \
    import HasTraits, Str, List, Any, Instance, DelegatesTo

from traitsui.api \
    import View, Group, Item, TreeEditor, \
    TreeNode, TreeNodeObject, ObjectTreeNode


# --------------------------------------------#
# Tree Node


class LeafModel(HasTraits):

    title = Str


class LeafNode(TreeNode):

    node_for = [LeafModel]

    label = 'title'

# --------------------------------------------#
# Tree Node Object


class TModel(HasTraits):

    title = Str

    kids = List(LeafModel)


class TNode(TreeNodeObject):

    model = Instance(TModel())

    kids = DelegatesTo("model")

    # Special named trait which is listened by the Tree for icon changes.
    icon = Str

    label = Str

    title2image = { 'img1' : 'img1.png',
                    'img2' : 'img2.png' }

    icon_path = './images/'

    def _label_default(self):
        return str('label')

    def __repr__(self):
        return self.label

    def tno_get_label(self, node):
        # return self.label
        return ""

    def tno_has_children(self, node):
        return True

    def tno_get_children(self, node):
        return list(self.model.kids)

    def tno_get_icon(self, node, state):
        if self.model.title in self.title2image:
            return self.title2image[ self.model.title ]
        else:
            return '<group>'

    def tno_get_icon_path(self, node):
        return self.icon_path


class ObjectTNode(ObjectTreeNode):

    # List of nodes this object applies to
    node_for = [TNode]

    # Name of trait for children
    children = 'kids'

    # List of objects that can be added as node
    add = [LeafNode]

# --------------------------------------------#
# Root class


class RootModel(HasTraits):

    title = Str

    tnodes = List(TNode)


class RootNode(TreeNode):

    node_for = [RootModel]

    label = 'title'

    children = 'tnodes'

    add = [LeafModel]

# --------------------------------------------#
# Tree


class Tree(HasTraits):
    root = Instance(RootModel, ())

    sel = Any

    TViewTreeEditor = TreeEditor(
        nodes=[
            RootNode(),
            ObjectTNode(),
            LeafNode(),
        ],
        selected='sel',
        hide_root=False,
        auto_open=2,
        editable=False,
        icon_size=(30, 30),
    )

    traits_view = View(
        Group(
            Item('root',
                 editor=TViewTreeEditor),
            show_labels=False,
        ),
        resizable=True,
    )

# --------------------------------------------#
# main


# leafs
lm1 = LeafModel(title='Bank1')
lm2 = LeafModel(title='Bank2')
lm3 = LeafModel(title='Bank3')
lm4 = LeafModel(title='Bank4')
lm5 = LeafModel(title='Bank5')

# my tnodes
tm1 = TModel(title='img1',
             kids=[lm1, lm2])

tm2 = TModel(title='img2',
             kids=[lm3, lm4, lm5],)

tn1 = TNode(model=tm1)
tn2 = TNode(model=tm2)

main = RootModel(title='main',
                 tnodes=[tn1, tn2],
                 )

tree = Tree(root=main)
tree.configure_traits()
'''
'''
