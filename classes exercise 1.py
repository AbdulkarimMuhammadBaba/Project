#9.1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print (f"Restaurant name is {self.restaurant_name} and cuisine type is {self.cuisine_type}")
    def open_restaurant(self):
        print ("The restaurant is open")
            
restaurant=Restaurant("Chicken Republic","Asian Cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9.2
arestaurant=Restaurant ("Gusto","Italian cuisine")
brestaurant=Restaurant ("Hard-Rock-Cafe","Nigeria cuisine")
crestaurant=Restaurant ("Albarka","Arabian cuisine")
arestaurant.describe_restaurant()
brestaurant.describe_restaurant()
crestaurant.describe_restaurant()

#9.3
class User:
    def __init__(self, first_name, last_name, age, marital_status, profession):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.marital_status=marital_status
        self.profession=profession
    def describe_user(self):
        summary={"first_name":self.first_name, "last_name":self.last_name, "age":self.age, "marital_status":self.marital_status, "profession":self.profession}
        print (summary)
    def greet_user(self):
        print (f"Hello, {self.first_name}")
user1=User("Abdul", "Abe", 21,"single","data analyst")
user1.describe_user()
user1.greet_user()
user2=User("Abubakar", "Mugabe", 61,"single","football")
user2.describe_user()
user2.greet_user()
user3=User("Abbas", "Aminu", 321,"married","Doctors")
user3.describe_user()
user3.greet_user()