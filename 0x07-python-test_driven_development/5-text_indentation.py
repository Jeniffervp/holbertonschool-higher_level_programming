#!/usr/bin/python3
"""text_indentation - print a text with 2 new lines after this character:.?:"""


def text_indentation(text):
    """
    Recibe a string to be replace chracters
    the first to evaluate is if the text are a string
    te second is replace every character for a new line
    finally print
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        new = text.replace(".", ".\n\n")
        new = new.replace(":", ":\n\n")
        new = new.replace("?", "?\n\n")
        new = new.replace("\n\n ", "\n\n")
        
        print(new)
