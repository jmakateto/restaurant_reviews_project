# Restaurant Reviews Project

## Project Overview

This project is designed to manage restaurant reviews using a Yelp-style domain. It involves three main models: `Restaurant`, `Customer`, and `Review`. The relationships among them are as follows: A `Restaurant` has many `Reviews`, a `Customer` has many `Reviews`, and a `Review` belongs to both a `Customer` and a `Restaurant`.

## Models and Relationships

### Restaurant

- `Restaurant` has a many-to-many relationship with `Customer`.

### Customer

- `Customer` has a many-to-many relationship with `Restaurant`.

### Review

- `Review` belongs to a `Customer` and a `Restaurant`.

## Class Methods and Functionality

### Customer

- `__init__(self, given_name, family_name)`: Initialize a customer with given and family names.
- `full_name(self)`: Return the full name of the customer.

### Restaurant

- `__init__(self, name)`: Initialize a restaurant with a name.
- `name(self)`: Return the name of the restaurant.
- `reviews(self)`: Return a list of all reviews for the restaurant.
- `customers(self)`: Return a unique list of customers who have reviewed the restaurant.

### Review

- `__init__(self, customer, restaurant, rating)`: Initialize a review with a customer, restaurant, and rating.
- `customer(self)`: Return the customer object for that review.
- `restaurant(self)`: Return the restaurant object for that review.
- `all()`: Return a list of all reviews.
- `restaurants()`: Return a unique list of restaurants a customer has reviewed.
- `add_review(self, restaurant, rating)`: Create a new review associated with a customer and restaurant.

## Getting Started

1. Clone the repository:

   ```bash
   git clone
   cd restaurant-reviews-project
   python main.py
   ```

## Contributors

John Makateto

## License

This project is licensed under the MIT License.
