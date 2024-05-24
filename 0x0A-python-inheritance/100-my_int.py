#!/usr/bin/python3
"""this is module documentation"""


class MyInt(int):
    """A rebellious integer class with inverted equality operators."""

    def __eq__(self, other):
        """Override the equality (==) operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality (!=) operator."""
        return super().__eq__(other)
