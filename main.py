"""
PIZZATRON 3000
"""

import constants as con
import functions as fun
import time


if __name__ == "__main__":
    # initializes the list of toppings (based on dictionary
    # toppings); changes as more toppings are available to 
    # the user
    while True:
       try:
          name = input("Welcome! What's your name?\n")
          break
       except ValueError:
          print(fun.fun_type("That's not a valid name!\n"))
    time.sleep(.75)
    name = name.capitalize()
    fun.fun_type(f"Welcome to Pizzatron, {name}!\n")
    time.sleep(.75)
    while True:
      answer = input(f"Are you ready to make some pizzas, {name}? (y/n)\n")
      if answer.upper() == 'Y':
         fun.fun_type("Great! Let's get started.\n")
         break
      elif answer.upper() == 'N':
         fun.fun_type("Too bad! Let's get started.\n")
         break
      else:
         fun.fun_type("Please input y or n as answers! \n")
       
