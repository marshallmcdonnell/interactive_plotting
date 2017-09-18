#!/usr/bin/env python

from traits.api import (Adapter, HasTraits, Interface, List, provides,
                        register_factory, Str, Supports)

class IPrintable(Interface):
    def get_formatted_text(self, n_cols):
        """ Return text formatted with the given number of columns. """

class PrintQueue(HasTraits):
    # This is the key part of the example: we declare a list of
    # items that provide or can be adapted to IPrintable
    queue = List(Supports(IPrintable))

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, printable):
        self.queue.append(printable)

    def print_next(self):
        printable = self.queue.pop(0)

        # The elements from the list are guaranteed to provide
        # IPrintable, so we can call the interface without worrying
        # about adaptation.
        lines = printable.get_formatted_text(n_cols=20)

        print '-- Start document --'
        print '\n'.join(lines)
        print '-- End of document -\n'

class TextDocument(HasTraits):
    """ A text document. """
    text = Str

@provides(IPrintable)
class TextDocumentToIPrintable(Adapter):
    """ Adapt TextDocument and provide IPrintable. """

    def get_formatted_text(self, n_cols):
        import textwrap
        return textwrap.wrap(self.adaptee.text, n_cols)


# ---- Application starts here.

# Register the adapter.
register_factory(TextDocumentToIPrintable, TextDocument, IPrintable)

# Create two text documents.
doc1 = TextDocument(text='very very long text the will bore you for sure')
doc2 = TextDocument(text='once upon a time in a far away galaxy')

# The text documents can be pushed on the print queue; in the process,
# they are automatically adapted by Traits.
print_queue = PrintQueue()
print_queue.push(doc1)
print_queue.push(doc2)

while not print_queue.is_empty():
    print_queue.print_next()
