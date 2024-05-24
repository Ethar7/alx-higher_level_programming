#!/usr/bin/python3
"""this is module doc"""


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
        Retrieves a dict representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to dic.
                If None, all attributes are included.

        Returns:
            dict: A dictionary containing the specified attri, values.
        """
        if attrs is None:
            return self.__dict__
        else:
            valid_attrs = [attr for attr in attrs if hasattr(self, attr)]
            return {attr: getattr(self, attr) for attr in valid_attrs}

    def reload_from_json(self, json):
        """
        Replaces all attri of the Student instance based on the provided dic.

        Args:
            json (dict): A dictionary containing attribute names and values.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
