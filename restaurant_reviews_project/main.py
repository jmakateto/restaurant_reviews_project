from customer import Customer
from restaurant import Restaurant
from review import Review

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Tasty Burgers")
restaurant2 = Restaurant("Pasta Paradise")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)
review3 = Review(customer2, restaurant2, 3)


print("Customers:")
for customer in [customer1, customer2]:
    print(customer.full_name())

print("\nRestaurants:")
for restaurant in [restaurant1, restaurant2]:
    print(restaurant.name)

print("\nReviews for", restaurant1.name)
for review in [review1, review2]:
    print(f"{review.customer.full_name()}: {review.rating}")
