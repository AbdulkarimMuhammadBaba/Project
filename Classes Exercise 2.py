#9.5
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print (f"Restaurant name is {self.restaurant_name} restaurant and cuisine type is {self.cuisine_type}")
    def open_restaurant(self):
        print ("The restaurant is open")
    def set_number_served(self):
        print(f"The number of customers served is {self.number_served}")
    def increment_number_served(self, number):
        self.number_served+=number
        print (f"The number of customers served today is {self.number_served}")
            
restaurant=Restaurant("Chicken Republic","Asian Cuisine")
restaurant.set_number_served()
restaurant.number_served=20
restaurant.set_number_served()
restaurant.increment_number_served(200)


#9.6
class User:
    def __init__(self, first_name, last_name, age, marital_status, profession):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.marital_status=marital_status
        self.profession=profession
        self.login_attempts=0
    def describe_user(self):
        summary={"first_name":self.first_name, "last_name":self.last_name, "age":self.age, "marital_status":self.marital_status, "profession":self.profession}
        print (summary)
    def greet_user(self):
        print (f"Hello, {self.first_name}")
    def login_attemptz(self):
        print (self.login_attempts)
    def increment_login_attempts(self):
        self.login_attempts+=1
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts=self.login_attempts-self.login_attempts
        print (self.login_attempts)
        
user1=User("Abdul", "Abe", 21,"single","data analyst")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.login_attemptz()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.login_attemptz()