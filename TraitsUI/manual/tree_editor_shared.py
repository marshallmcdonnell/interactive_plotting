#!/usr/bin/env python

from traits.api \
    import HasTraits, Str, Regex, List, Instance
from traitsui.api \
    import View, TreeEditor, TreeNode, Group, Item

# DATA CLASSES

class Employee ( HasTraits ):
    name  = Str( '<unknown>' )
    title = Str
    phone = Regex( regex = r'\d\d\d-\d\d\d\d' )

    def default_title ( self ):
        self.title = 'Senior Engineer'

class Department ( HasTraits ):
    name      = Str( '<unknown>' )
    employees = List( Employee )


class Company ( HasTraits ):
    name        = Str( '<unknown>' )
    departments = List( Department )
    employees   = List( Employee )

class Owner ( HasTraits ):
    name    = Str( '<unknown>' )
    company = Instance( Company )

# INSTANCES

jason = Employee(
     name  = 'Jason',
     title = 'Engineer',
     phone = '536-1057' )

mike = Employee(
     name  = 'Mike',
     title = 'Sr. Marketing Analyst',
     phone = '536-1057' )

dave = Employee(
     name  = 'Dave',
     title = 'Sr. Engineer',
     phone = '536-1057' )

susan = Employee(
     name  = 'Susan',
     title = 'Engineer',
     phone = '536-1057' )

betty = Employee(
     name  = 'Betty',
     title = 'Marketing Analyst' )

owner = Owner(
    name    = 'wile',
    company = Company(
        name = 'Acme Labs, Inc.',
        departments = [
            Department(
                name = 'Marketing',
                employees = [ mike, betty ]
            ),
            Department(
                name = 'Engineering',
                employees = [ dave, susan, jason ]
            )
        ],
        employees = [ dave, susan, mike, betty, jason ]
    )
)

# View for objects that aren't edited
no_view = View()

# SHARED EDITOR
my_shared_editor_pane = TreeEditor(shared_editor=True)

shared_tree_1 = TreeEditor(shared_editor = True,
                           editor = my_shared_editor_pane,
                           nodes = [ TreeNode( node_for  = [ Company ],
                                               auto_open = True,
                                               children  = 'departments',
                                               label     = '=Departments',
                                               view      = no_view,
                                               add       = [ Department ] ),
                                   ]
                           )
shared_tree_2 = TreeEditor(shared_editor = True,
                           editor = my_shared_editor_pane,
                           nodes = [ TreeNode( node_for  = [ Company ],
                                     auto_open = True,
                                     children  = 'employees',
                                     label     = '=Employees',
                                     view      = no_view,
                                     add       = [ Employee ] ),
                                   ]
                           )

# The main view
view = View(
           Group(
               Item(
                    name = 'company',
                    id = 'company',
                    editor = my_shared_editor_pane,
                    resizable = True ),
                orientation = 'vertical',
                show_labels = True,
                show_left = True, ),
            title = 'Company Structure',
            dock = 'horizontal',
            drop_class = HasTraits,
            buttons = [ 'Undo', 'OK', 'Cancel' ],
            resizable = True,
            width = .3,
            height = .3 )

owner.configure_traits()
