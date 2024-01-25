# class Item:
#     pay_rate = 0.8 #discount of 20%
#     all = []
#     def __init__(self, name : str, price : float, quantity : int = 0):
#         #Run validations to the recieved args
#         assert price >= 0, f"price {price} is not > than or = to 0"
#         assert quantity >= 0, f"quantity {quantity} is not > than or = to 0"
#
#         #Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#         #actions to execute
#         Item.all.append(self)
#
#     def calculate_total_price(self):
#         return  self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
#
#     def instantiate_from_csv(self):
#
#
#     def __repr__(self):
#         return f"item('{self.name}',{self.price},{self.quantity})"
#
#
# print(Item.all)







# class phone:
#     def __init__(self, status, colour, cost):
#         print(status)
#         self.colour = colour
#         self.cost = cost
#     def call(self):
#         print("Making a call")
#     def game(self):
#         print("Playing game")
# k = phone("active", "Purple", 89000)
# k.call()
# k.game()
# print(k.colour)



# class emp:
#     def __init__(self, id : int, name : str, age : int, salary : int, gender : str):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.gender = gender
#     def empDetails(self):
#         print("id is : ", str(self.id))
#         print("name is : ", str(self.name))
#         print("age is : ", str(self.age))
#         print("salary is : ", str(self.salary))
#         print("gender is : ", str(self.gender))
# e = emp(4165, "gvdsg dsg sd", 21, 84654, "m")
# e.empDetails()



class auto:
    def __init__(self):
        print("inside parent class 1")
    def go(self):
        print("go auto")
class vehicle:
    def __init__(self, mileage, cost):
        print("ur in parent class 2")
        self.mileage = mileage
        self.cost = cost
    def details(self):
        print("this r the car details")
        print("mileage is : ",self.mileage)
        print("cost is : ",self.cost)
        print("color is : ",self.color)
        print("cc is : ",self.cc)
class car(vehicle, auto):
    def __init__(self, milege, cost, color, cc):
        super().__init__(milege, cost)
        self.color = color
        self.cc = cc
        print("ur in child class inheriting the parent class 1 n 2")
    def spec(self):
        print("3 cylinder car")
v1 = car(20, 5000, "white", 1000)
v1.details()
v1.spec()
v1.go()