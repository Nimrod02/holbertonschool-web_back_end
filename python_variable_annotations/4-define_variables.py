#!/usr/bin/env python3
"""module 4 - define_variables
"""


a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"


def define():
    """defin and annotate variables

    Returns:
        int, float, bool, str:
        return the type of each varibles
    """
    return a, pi, i_understand_annotations, school
