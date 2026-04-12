# class User:
#     def unique():
#         name: str = "sumit"
#         age: int = 25

# user = User()
# print(user.unique.name)     # code won't work

"""
Fix it...
"""
# Using instance attribute...
class User:
    def __init__(self, age, name):
        self.age: int = age
        self.name: str = name

user_1 = User(25, "Amit")
user_2 = User(24, "Sumit")

print(user_1.name)
print(user_2.name)

"""
Return value from function
"""
class Car:
    def unique(self):
        name: str = "Maruti"
        model: int = 200

        return name, model

car_1 = Car()
name, model = car_1.unique()
print(name)

"""
Return an object/dict
"""
class Bus:
    def unique(self):
        return {"name": "chunmun", "model": "407"}
    
bus = Bus()
print(bus.unique()["name"])