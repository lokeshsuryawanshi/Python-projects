# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age??  "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill =  7
#     print("Youth tickets are $7.")
#   elif age >= 45 and age <=55:
#     print("Ride is on us.")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
#   want_photos = input("Do you want a photo taken? y or n ")
#   if want_photos == "y":
#     bill += 3
#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you have to grow taller before you can ride. ")


#*****************************************************************************************************************************************

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]

# #print(dirty_dozen)


# print(dirty_dozen[0])
# print(dirty_dozen[1])


# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])

#************************************************************************************************************************

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# vertical_column = int(position[0])
# horizontal_row = int(position[1])

# select_row = map[horizontal_row - 1]
# select_row[vertical_column-1] = "X"
# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

#****************************************************************************************************************************

# rock = '''
# Rock
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
# Papper
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
# Scissors
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇
# import random

# rps = [rock, paper, scissors]
# human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
# print(rps[human])

# print("Computer Choose: ")
# comp = (random.choice(rps))
# print(comp)

# if human == rock and comp == scissors:
#   print("You won")
# if human == paper and comp == rock:
#   print("You won")
# if human == scissors and comp == paper:
#   print("You won")
# if human == rock and comp == paper:
#   print("You loose")
# if human == paper and comp == scissors:
#   print("You loose")
# if human == scissors and comp == rock:
#   print("You loose")
# else:
#   print("Draw")
#****************************************************************************************************************
#for i in range (0 , 100): print(i)



# l = []
# n = int(input("Size of array: "))
# for i in range (0,n):
#   l.append(int(l[i]))
# print(l)

# x= input("emter a list of name :").split()
# print(x)

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if is_leap(year) and month == 2:
#       return 29
#   return month_days[month-1]
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
 
# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:   
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# year = int(input("Which year do you want to check?"))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")


#LEARNING TURTLE

# from turtle import Turtle, Screen 
# timmy = Turtle()
# timmy.shape("turtle")
# print(timmy)
# timmy.color("red")
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# timmy.forward(100)

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# print(table)