# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):

        if not isinstance(name, str):
            raise TypeError("Name is not a string.")

        if name == "":
            raise ValueError("Name is empty.")

        if not isinstance(birth, date):
            raise TypeError("Birth is not a date.")

        self.name = name
        self.birth = birth
        

    # Implement methods initials() and is_birthday() here
    def initials(self):
        """
        returns the initials of the person's name
        """

        nameList = list(self.name.split(" "))
        output = ""

        for i in nameList:
            output += i[0].upper()      

        return output
    # (see README.md for further details)

    def is_birthday(self):
        """
        returns true if today's date and the person's birthday matches. If not, returns false.
        """

        today = date.today()

        if (self.birth.day == today.day and self.birth.month == today.month):
            return True
        else:
            return False


