class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

class ReviewRepository:
    all_reviews = []

    @classmethod
    def create(cls, customer, restaurant, rating):
        review = Review(customer, restaurant, rating)
        cls.all_reviews.append(review)
        return review

    @classmethod
    def all(cls):
        return cls.all_reviews
