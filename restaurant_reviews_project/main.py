from customer import CustomerRepository
from restaurant import RestaurantRepository
from review import ReviewRepository

# Create sample instances
customer1 = CustomerRepository.create("John", "Doe")
customer2 = CustomerRepository.create("Jane", "Smith")

restaurant1 = RestaurantRepository.create("Tasty Burgers")
restaurant2 = RestaurantRepository.create("Pasta Paradise")

ReviewRepository.create(customer1, restaurant1, 4)
ReviewRepository.create(customer2, restaurant1, 5)
ReviewRepository.create(customer2, restaurant2, 3)

# Test methods
print("Customers:")
for customer in CustomerRepository.all():
    print(customer.full_name())

print("\nRestaurants:")
for restaurant in RestaurantRepository.all():
    print(restaurant.name)

print("\nReviews for", restaurant1.name)
for review in ReviewRepository.all():
    if review.restaurant == restaurant1:
        print(f"{review.customer.full_name()}: {review.rating}")
