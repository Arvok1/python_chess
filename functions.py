from os import system, name
from sys import exit
from time import sleep

class functions():
    def line_break(self):
        pass 


    def clear_screen(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def index_2d(self, data, search):
        for i, e in enumerate(data):
            try:
                return i, e.index(search)
            except ValueError:
                pass
        raise ValueError("{!r} is not in list".format(search))

manyfunctions = functions()