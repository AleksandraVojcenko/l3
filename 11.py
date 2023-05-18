def j7():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} кухня {self.cuisine_type}.")
        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name}  принимает гостей")

    newRestaurant = Restaurant("Булочки", "домашняя")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def j8():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} кухня {self.cuisine_type}.")
    restaurant1 = Restaurant("Гастрит", "Больничная")
    restaurant2 = Restaurant("Язва", "Таблеточная")
    restaurant3 = Restaurant("Богодельня", "Домашняя")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
def j9():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} кухня {self.cuisine_type}.")
            print(f"Рейтинг ресторана: {self.rating}")
        def update_rating(self, new_rating):
            self.rating = new_rating
    restaurant1 = Restaurant("Ресторан ", "еда и на этом спасибо", 0.5)
    restaurant1.describe_restaurant()
    restaurant1.update_rating(1.7)
    restaurant1.describe_restaurant()


