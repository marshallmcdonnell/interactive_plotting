#!/usr/bin/env python 

# code_editor.py -- Example of using code editors

import numpy as np
from traits.api import HasPrivateTraits, Code
from traitsui.api \
    import View, CodeEditor, Item
from traitsui.menu import NoButtons

class CodeEditorTest ( HasPrivateTraits ):

    three = Code

    view = View( Item('three'),
                 resizable = True )


if __name__ == '__main__':
    CodeEditorTest().configure_traits()
