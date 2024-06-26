#!/usr/bin/python3
"""this is a module doc"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with attri.

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
            attrs (list, optional): List of attri names in dic
                If None, all attributes are included.

        Returns:
            dict: A dictionary containing the specified attri ,values.
        """
        if attrs is None:
            return self.__dict__
        else:
            valid_attrs = [attr for attr in attrs if hasattr(self, attr)]
            return {attr: getattr(self, attr) for attr in valid_attrs}
