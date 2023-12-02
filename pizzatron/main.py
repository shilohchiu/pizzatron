"""
PIZZATRON 3000
Shiloh Chiu and Alex Boswell
"""

import functions as fun


if __name__ == "__main__":
   # initializes the list of toppings (based on dictionary
   # toppings); changes as more toppings are available to 
   # the user
   fun.fun_type("----PIZZATRON: CS1210 FINAL PROJECT-----\n")
   fun.fun_type("Created by: Shiloh Chiu and Alex Boswell\n")
   while True:
      try:
         name = input("Hello! What's your name?\n")
         break
      except ValueError:
         fun.fun_type("That's not a valid name!\n")
   name = name.capitalize()
   fun.fun_type(f"Welcome to Pizzatron, {name}!\n")
   while True:
      answer = input(f"Are you ready to make some pizzas, {name}? (y/n)\n")
      if answer.upper() == 'Y':
         fun.fun_type(f"Great! Love your enthusiasm, {name}. Let's get started.\n")
         break
      elif answer.upper() == 'N':
         fun.fun_type(f"Too bad! You're going to learn to make some"\
                      " pizzas anyways, {name}. Let's get started.\n")
         break
      else:
         fun.fun_type("Please input y or n as answers! \n")
   fun.fun_type("Okay, let's go over the rules of how to make the pizza.\n")
   fun.fun_type("As you level up, you get to unlock new ingredients! It's "\
               "up to you to remember what ingredients are on the pizza and "\
               "to put all the toppings on the pizza within a set amount of "\
               "time. The more pizzas you make, the more complicated the pizzas "\
               "get! ")
   fun.fun_type("At the beginning of each level, you'll be shown a key of the toppings and what each topping is represented as.\n")
   fun.fun_type("At the beginning of each round, the computer will show you a pizza.\n")
   fun.fun_type("To recreate the pizza, just type the ")
