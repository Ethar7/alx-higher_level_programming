#!/usr/bin/python3
"""this is the documentation module"""


def text_indentation(text):
    """
    Prints the given text with 2 new lines after each occurrence of '.', '?', and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove any leading or trailing spaces
    cleaned_text = text.strip()

    # Initialize an empty result string
    result = ""

    # Iterate through the cleaned text
    for char in cleaned_text:
        result += char
        if char in ".?:":
            result += "\n\n"  # Add 2 new lines after the character
        elif char != " ":
            result += " "

    print(result, end="")
