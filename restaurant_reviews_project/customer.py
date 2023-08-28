class Customer:
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

class CustomerRepository:
    all_customers = []

    @classmethod
    def create(cls, given_name, family_name):
        customer = Customer(given_name, family_name)
        cls.all_customers.append(customer)
        return customer

    @classmethod
    def all(cls):
        return cls.all_customers
