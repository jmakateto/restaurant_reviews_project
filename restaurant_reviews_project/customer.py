from review import Review

class Customer:
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"
