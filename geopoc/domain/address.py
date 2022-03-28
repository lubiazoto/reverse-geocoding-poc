class Address:

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Address):
            return self.street == other.street and self.number == other.number
        return False

    def __str__(self):
        """Overrides the default implementation"""
        return "Address["+self.street+", " + self.number + "]"

    def __init__(self, new_street, new_number):
        self.street = new_street
        self.number = new_number

