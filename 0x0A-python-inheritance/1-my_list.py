#!/usr/bin/python3
"""
This module contains class MyList.
"""


class MyList(list):
    """
    MyList inherits from list, and contains
    method print_sorted.
    """

    def print_sorted(self):
        """
        print_sorted sorts the MyList and
        prints it.
        """

        sortedList = self.copy()
        sortedList.sort()
        print(sortedList)
