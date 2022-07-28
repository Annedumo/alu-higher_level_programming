#!/usr/bin/python3
"""class my_list that inherits from list"""


class MyList(list):
    """class MyList inherits 
    properties of class list
    """
    def print_sorted(self):
        print(sorted(self)) 
