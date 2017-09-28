#!/usr/bin/env python

# transient_metadata.py -- Example of using 'transient' metadata
from traits.api import HasTraits, File, Any

class DataBase ( HasTraits ):
    # The name of the data base file:
    file_name = File

    # The open file handle used to access the data base:
    file = Any( transient = True )
