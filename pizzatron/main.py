"""
PIZZATRON 3000
Shiloh Chiu and Alex Boswell
"""

import functions as fun
import time

if __name__ == "__main__":
   level = 0
   score = 0
   toppings = {} # <-- name : symbol
   # initializes the list of toppings (based on dictionary
   # toppings); changes as more toppings are available to 
   # the user
   fun.fun_type("----PIZZATRON: CS1210 FINAL PROJECT-----")
   fun.fun_type("Created by: Shiloh Chiu and Alex Boswell")
   while True:
      try:
         name = input("Hello! What's your name?\n")
         break
      except ValueError:
         fun.fun_type("That's not a valid name!")
   name = name.capitalize()
   fun.fun_type(f"Welcome to Pizzatron, {name}!")
   while True:
      answer = input(f"Are you ready to make some pizzas, {name}? (y/n)\n")
      if answer.upper() == 'Y':
         fun.fun_type(f"Great! Love your enthusiasm, "\
                      f"{name}. Let's get started.")
         break
      elif answer.upper() == 'N':
         fun.fun_type(f"Too bad! You're going to learn to make some"\
                      " pizzas anyways, {name}. Let's get started.")
         break
      else:
         fun.fun_type("Please input y or n as answers! ")
   fun.fun_type("Okay, let's go over the rules of how to make the pizza.")
   fun.fun_type("As you level up, you get to unlock new ingredients! "\
                "It's up to you to remember what ingredients are on "\
                "the pizza and to put all the toppings on the pizza "\
                "within a set amount of time. The more pizzas you make, "\
                "the more complicated the pizzas get! ")
   fun.fun_type("At the beginning of each level, you'll be shown a key of "\
                "the toppings and what each topping is represented as.")
   fun.fun_type("At the beginning of each round, the "\
                "computer will show you a pizza.")
   fun.fun_type("To recreate the pizza, just type the name of the topping, "\
                "one at a time. For example, if I want put an anchovy on "\
                "the pizza, I would just type 'anchovy' into the terminal.")
   fun.fun_type("When the pizza is completely full, we'll score your pizza "\
                "and tell you how accurate. it is.")
   fun.fun_type("Once you reach the end of the game, we'll save a file "\
                "of your results to your computer. ")
   time.sleep(1)
   fun.fun_type("Okay, let's begin!")
   # display LEVEL 1 and print the list of dictionaries
   fun.level_up(level, toppings)
   # generate a pizza
   # each level has the same number of rounds as the level # 