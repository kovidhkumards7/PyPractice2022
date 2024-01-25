# print("Hello KOVIDH, What's up yo?")
# a = "hdrhf reghes"
# b = 'f'
# c = 3.1458755416851325156456132515684798
# d = "gderhjtfr jret ygestg es tg"
# e = a + " " + d
# print(type(a))
# print(a)
# print(b)
# print(c)
# print(e)


# age = 23
# age += 1
# print(age)
# print("ur age is " + str(age))


# height = 2503.5645626
# print(height)
# print(type(height))
# print("ur height is " + str(height) + "cm")


# a = False
# b = True
# print(a)
# print(a or b)


# a , b , c = 1 , "fcryvy" , 45.151
# x = y = z = 3
# print( x , y , z )
# print( a , b , c )
# a , z = z , a
# print(a)
# print(z)


# name = "KOVIDH KUMAR D S"
# print(len(name))
# print(name.split())
# print(name.find("U"))
# print(name.count('K'))
# print(name.lower())
# print(name.upper())
# print(name.replace('K','Z'))
# print(name.isalpha())
# print(name.isupper())
# print(name*7)


# x , y , z = 1 , 2.5486 , "8"
# print(type(x))
# print(type(y))
# print(type(z))
# print()
# x = str(x)
# print(type(x))
# y = int(y)
# print(type(y))
# z = float(z)
# print(type(z))


# a = input(str("Enter ur name"))
# print(type(a))
# print("hi " + a)
# b = float(input("ur age?"))
# print("ur age is " + str(b))
# print(type(b))
# print("Hello " + a + " u r " + str(b) + " years old")


# import math
# print(math.pi)
# print(round((math.pi)))
# print(math.floor(math.pi))
# print(math.ceil(math.pi))
# print(abs(math.pi))
# print(math.pow(math.pi,3))
# print(math.sqrt(256))
# print(max(456,484,4,54,52641666266,41541566,5))
# print(min(456,484,4,54,52641666266,41541566,5))


# a = "fdesgf ds gsegdsg etgdrfh yrhjtr"
# firstName = a[2:13:2]
# lastName = a[13::2]
# print(a)
# print(a[::-1])
# print(firstName)
# print(lastName)


# web = "http://google.com"
# web1 = "http://wikkioedia.com"
# s = slice(7,-4)
# print(web[s])
# print(s)
# print(web1[s])


# age = int(input("Enter age: "))
# if ( age >= 16 and age <= 20):
#     print("ur an teen")
# elif( age >= 20 ):
#     print("ur an adult")
# elif( age < 16 and age >= 12 ):
#     print("ur a infant")
# elif( age <= 12 and age >= 6 ):
#     print("ur an child")
# elif( age > 0 ):
#     print("ur a baby")
# elif( age == 0 ):
#     print("ur just born")
# elif( age < 0 ):
#     print("enter a valid age")


# name = ""
# while ( len( name ) == 0 ):
#     name = input("Enter ur name : ")
# print( "Hello " + str(name) )


# for i in range( 10 , 15 , 2 ):
#     print(i+1)


# for i in "HELLO KOVIDH KUMAR D S":
#     print( i, end = "  " )


# import time
# for s in range( 10 , 0 , -1 ):
#     print(s)
#     time.sleep(1)
# print("TIME'S UP YO, WAKE UP")


# rows = int(input("enter no of rows: "))
# columns = int(input("enter no of columns: "))
# symbol = input("enter symbol to be printed: ")
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end = " ")
#     print()


# n = int(input("enter number: "))
# b = 1
# c = input("Enter symbol: ")
# while( n > 0 ):
#     print(" " * n , end="")
#     print(c * b)
#     b = b + 1
#     n = n - 1


# n = int(input("enter number: "))
# b = 1
# c = input("Enter symbol: ")
# while( n > 0 ):
#     print(c * b)
#     b = b + 1
#     n = n - 1


# n = int(input("enter number: "))
# b = 1
# c = input("Enter symbol: ")
# print(" " * ( n + 1 ) + c)
# while( n - 1 > 0 ):
#     print(" " * n , end="")
#     print(c * b + c * b)
#     b = b + 1
#     n = n - 1


# while True:
#     name = input("Enter name: ")
#     if len(name) != 0:
#         break


# while True:
#     name = input("Enter name: ")
#     if name.isdigit():
#         continue
#     else:
#         break


# phoneNumber = "+91 9036310085"
# for i in phoneNumber:
#     if i.isdigit():
#         print(i, end="")
#     else:
#         continue


# phoneNumber = "+91 9036310085"
# for i in phoneNumber:
#     if i.isdigit():
#         print(i, end="")
#     else:
#         pass


# food = [ "pizza", "burger", "sandwich"]
# food[2] = "idli"
# food.append("kulfi")
# print(food)
# food.remove("kulfi")
# print(food)
# food.sort()
# print(food)


# food = [ "pizza", "burger", "sandwich"]
# drinks = ["tea", "coffee","badam milk"]
# dessert = ["ice cream", "payasa"]
# hotelList= food + drinks + dessert
# print("List concatenation")
# print(hotelList)
# print("List of Lists")
# hotelList = [food,drinks,dessert]
# print(hotelList)
# print(hotelList[0])
# print(hotelList[0][2])


# stu = ("bro",24,"male","bro")
# print(stu.count("bro"))
# print(stu.index(24))
# for i in stu:
#     print(i,end="    ")
# if "bro" in stu:
#     print()
#     print()
#     print("What's up yo, bro's here!")


# utensils = {"fork", "spoon","plates", "cups","bro"}
# stu = {"bro",24,"male","bro"}
# stu.update(utensils)
# dinnerTable = utensils.union(stu)
# print(utensils.difference(stu))
# # utensils.add("pan")
# # utensils.remove("cups")
# print(dinnerTable)
# for i in utensils:
#     print(i)


# capitals = {"USA":"DC",
#             "INDIA":"NEW DELHI",
#             "UK":"LONDON",
#             "GERMANY":"BERLIN"}
# print(capitals["UK"])
# print(capitals)
# print(capitals.get("USA"))
# print(capitals.get("FRANCE"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# for i,j in capitals.items():
#     print(i+" - "+j)
# capitals.update({"RUSSIA":"MOSCOW"})
# capitals.update({"RUSSIA":"ukraine"})
# print(capitals)
# capitals.pop("RUSSIA")
# print(capitals)


# name = "kovidh kumar d s"
# print(name)
# if(name.islower()):
#     name = name.capitalize()
# print(name)
# name = name.upper()
# print(name)
# first_name = name[0:6]
# last_name = name[7:len(name)]
# print(first_name)
# print(last_name)
# ls = name.split()
# print(ls)
# na = []
# for i in ls:
#     for j in i:
#         na.append(j)
# print(na)


# import time
# def hello(a,b):
#     print("hello " + a + " " + b)
#     print("what's up yo")
# hello("john","albert")
# time.sleep(1)
# hello("sam","jones")
# fName = ["kovi" , "raj" , "tej"]
# lName = ["kumar" , "reddy" , "singh"]
# for i in range(len(fName)):
#     hello(fName[i],lName[i])
#     time.sleep(1)
#     print()


# def maths(a,b,op):
#     if op == "+":
#         return a+b
#     if op == "%":
#         return a%b
#     if op == "/":
#         return a/b
#     if op == "*":
#         return a*b
#     if op == "-":
#         return a-b
#     else:
#         print("improper operater selected")
#         return
# a = input("enter operator:  ")
# print(maths(7,10,a))


# def hi(fName, mName, lName):
#     print("hey " + fName + " " + mName + " " + lName)
# hi("KOVIDH", "KUMAR", "D S")
# hi(lName="ZSZFD", fName="HRFDEH", mName="RFHRT")


# print(round(abs(float(input("enter a number")))))


# def add(*args):
#     args = list(args)
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(add(3, 7, 45, 8, 89))


# def hi(**dict):
#     print("Hello ", end=" ")
#     for i in dict.keys():
#         print(dict[i], end=" ")
# hi(lName="ZSZFD", fName="HRFDEH", mName="RFHRT")


# a = 98418
# print(id(a))


# a = 486
# b = 485456
# print("the {} is fefgmsdk {} ergrf".format(a,b))
# print("the {1} is fefgmsdk {0} ergrf".format(a,b))
# print("the {c} is fefgmsdk {d} ergrf".format(c = 48541,d = 474))
# print("the {} is fefgmsdk {} ergrf".format(48541,474))
# print("the {} is fefgmsdk {:7} ergrf".format(48541,474))
# print("the {:.3f} is fefgmsdk {:.7f} ergrf".format(4.8541,4.549864674))


# import random
# a = random.randint(0,85)
# b = random.random()
# print(a)
# print(b)
# LIST = ["htfghfdg","grdsgfd","srdgds","sdef"]
# print(random.choice(LIST))
# cards = [1,2,3,4,5,6,7,8,9,"J","K","Q","A"]
# random.shuffle(cards)
# print(cards)


# try:
#     a = int(input("enter numerator"))
#     b = int(input("enter denomerator"))
# except ZeroDivisionError as e:
#     print("u can't divide by zero")
#     print(e)
# except ValueError as e:
#     print("u can't divide by anything else number")
#     print(e)
# except Exception as e:
#     print("something's wrong")
#     print(e)
# else:
#     print(float(a / b))
# finally:
#     print("this is right format of input")


# import os
# path = "C:\\Users\\Dell\\Desktop\\kk.txt"
# if os.path.exists(path):
#     print("file exist")
#     if os.path.isfile(path):
#         print("that is file")
#     elif os.path.isdir(path):
#         print("it is a directory")
# else:
#     print("file doesn't exist")


# try:
#     with open("C:\\Users\\Dell\\Desktop\\kk.txt") as file:
#         print(file.read())
#     print(file.closed)
# except FileNotFoundError as e:
#     print(e)


# try:
#     a = "   hdfhdgfgn mfjgn jdksngf"
#     with open("C:\\Users\\Dell\\Desktop\\kk.txt", "a") as file:
#         file.write(a)
#     with open("C:\\Users\\Dell\\Desktop\\kk.txt") as file:
#         print(file.read())
#     print(file.closed)
# except FileNotFoundError as e:
#     print(e)


# import shutil
# shutil.copyfile("C:\\Users\\Dell\\Desktop\\kk.txt","C:\\Users\\Dell\\Desktop\\copy.txt")


# import  os
# source = "C:\\Users\\Dell\\Desktop\\kk.txt"
# dest = "C:\\Users\\Dell\\Desktop\\test.txt"
# try:
#     if os.path.exists(dest):
#         print("there is already a file there")
#     else:
#         os.replace(source,dest)
#         print("file replaced")
# except FileNotFoundError as e:
#     print(e)


# import  os
# path = "C:\\Users\\Dell\\Desktop\\copy.txt"
# try:
#     os.remove("C:\\Users\\Dell\\Desktop\\copy.txt")
# except FileNotFoundError as e:
#     print(e)
#     print("file not found")


import cv2
img = cv2.imread("PHOTO.jpg", 0)
print(img)
cv2.imshow("image", img)
cv2.waitKey(10000)
# cv2.destryAllWindows()