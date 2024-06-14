#!/usr/bin/python3

# Import tools

import os

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from StylePy import *

# Make instancies

# Graphical Interface
class StylerWindow(Gtk.Window):

    def __init__(self):

        # Set helpful vars

        self.path = '.'

        self.file_content = ''

        self.authors = []

        self.author = 'anonymous'

        # Set Windows basics

        super().__init__(title = 'Styler - finds to the author')

        self.set_size_request(500, 300)

        self.widgets = [
                            Gtk.Label(label = 'Identify Possible Author'), # Index 0
                            Gtk.Entry(placeholder_text = 'File Path'), # Index 1
                            Gtk.Entry(placeholder_text = 'Possible Authors'), # Index 2
                            Gtk.Button(label = 'Analize'), # Index 3
                            Gtk.Label(label = 'The Author is:\n\n\t(...)') # Index 4
                        ]

        # Set the cointaner and adds widgets and it to the window

        container = Gtk.VBox()

        container.set_spacing(22)

        for widget in self.widgets:

            container.add(widget)

        self.add(container)

        # Set Windows Events
        self.widgets[3].connect('clicked', self.analize)
        

    # Set Windows Actions
    def analize(self, event):
        '''
            Look for the more likely author of the text of file
        '''
        # Get Path
        self.path = self.widgets[1].get_text()
        # Save content of file path

        file = open(self.path, 'r')

        lines = file.readlines()

        for content in lines:

            self.file_content += content.replace('\n', '')

        file.close()
        # Get list of authors
        self.authors = self.widgets[2].get_text().split(',')
        # Get Which of them is the autor
        for possible in self.authors:
            # Reduce calls to win velocity
            possible = possible.strip()
            # Make new abstraction like Abstractor instance
            analizer = Abstractor('authors.csv', possible)
            # Analize
            if (analizer.could_write(self.file_content.lower())):
                self.author = possible
                # Update label only when the author has been founded
                self.widgets[4].set_text('The file author is "%s".' % self.author)
            else:
                self.author = 'anonymous'
        # Give Feedback to the user
        print('\nAnalizyng Text in the file "%s": ' % self.path, event, '\n')

        return event

# Main Program

if (__name__ == '__main__'):

    view = StylerWindow()
    # Show the view
    view.show_all()
    # Exec the window
    print('\n')
    # Keep safe for the possible failures
    try:
        Gtk.main()
    except:
        view.close()
        print('\tWINDOW CLOSED\n')
        # Ends of the program
        os.system('exit 0')
