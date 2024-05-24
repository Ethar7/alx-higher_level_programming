#!/usr/bin/python3
"""this is a module doc"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with the given attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include in the dictionary.
                If None, all attributes are included.

        Returns:
            dict: A dictionary containing the specified attributes and their values.
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs}

    def reload_from_json(self, json):
        for attr, value in json.items():
            setattr(self, attr, value)

