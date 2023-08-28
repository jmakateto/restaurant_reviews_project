class Restaurant:
    def __init__(self, name):
        self.name = name

class RestaurantRepository:
    all_restaurants = []

    @classmethod
    def create(cls, name):
        restaurant = Restaurant(name)
        cls.all_restaurants.append(restaurant)
        return restaurant

    @classmethod
    def all(cls):
        return cls.all_restaurants
