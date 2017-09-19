#!/usr/bin/env python

# cached_prop.py -- Example of @cached_property decorator
from traits.api import HasPrivateTraits, List, Int,\
                                 Property, cached_property

class TestScores ( HasPrivateTraits ):

    scores  = List( Int )
    average = Property( depends_on = 'scores' )

    @cached_property
    def _get_average ( self ):
        s = self.scores
        print "Computing..."
        return (float( reduce( lambda n1, n2: n1 + n2, s, 0 ) )
                 / len( s ))


math_test = TestScores(scores=[80,77,99,85])
print math_test.scores
print math_test.average
print math_test.average
math_test.scores.append(55)
print math_test.average

