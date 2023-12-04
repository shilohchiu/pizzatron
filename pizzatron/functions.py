"""
All the major functions our game relies on.
----------------replace_blank()----------------
- takes two arguments (topping and the pizza) 
and replaces the underscores in the second 
argument to have the topping.
- returns the modified verson of the second
argument
-----------------write_stats()-----------------
- writes a .txt file to the user's computer that
shows them the stats of their game when the user
finishes the game
----------------level_up()----------------
- allows more dictionary keys to be unlocked and prints
what level you are currently on and also the dictionary keys and what they are represented as symbolically.
- if level != 1 then the computer will tell you the number of points you had on each round (calculated in the score pizza function)
----------------generate_pizza()----------------
- generates a new pizza + prints it out the screen
asking the user to recreate it (uses the random 
generator)
- takes the list of unlocked toppings as an argument
----------------score_pizza()----------------
- used with replace_blank, will take the user
input and give a score out of 10 based on 
game parameters
"""
# test

import random
import constants as con
import time
import sys
import math

def str_to_lst(str):
  lst = []
  for char in str:
    lst.append(char)
  return lst

def lst_to_str(lst1):
    str1 = ""
    for char1 in lst1:
        str += char1
    return str1

def replace_blank(topping, pizza):
  lst = str_to_lst(pizza)

  for c in range(len(lst)):
    if lst[c] == '_' and \
    lst[c - 1] == '(' and lst[c+1] == ')':
      lst[c] = topping

    new_pizza = ''
    p = 0
    for _ in lst:
        new_pizza += lst[p]
        p += 1

  return new_pizza

def input_pizza():
    user_pizza = str_to_lst(con.PIZZASTR)
    toppingnum = 1
    while '(_)' in lst_to_str(user_pizza):
        newtop = input("What will you make for topping #" + str(toppingnum) + "?")
        for v in user_pizza:
            if user_pizza[v] == '_' and user_pizza[v-1] == '(':
                user_pizza[v] = newtop
            break
        print(lst_to_str(user_pizza))

def generate_pizza(unlocked_toppings, pizza_template):
  picked_toppings = []
  for _ in range(random.randint(1,len(unlocked_toppings))):
    i = random.choice(unlocked_toppings)
    if i not in picked_toppings:
      picked_toppings.append(i)


  generated_pizza = str_to_lst(pizza_template)

  for i, topping in enumerate(picked_toppings):

    for c in range(len(generated_pizza)):
      
      if generated_pizza[c] == '_' and \
      generated_pizza[c - 1] == '(' \
      and generated_pizza[c+1] == ')':
        if i == (len(picked_toppings)-1):
          generated_pizza[c] = topping
        else:
          choice = random.random()
          if choice >= 1 / len(picked_toppings) * (i+1):
            generated_pizza[c] = topping
    
  new_pizza = ''
  p = 0
  for _ in generated_pizza:
      new_pizza += generated_pizza[p]
      p += 1
  print(picked_toppings)
  for i, topping in enumerate(picked_toppings):
    if topping not in generated_pizza:
      picked_toppings.pop(i)
  print(picked_toppings)

  return new_pizza

def level_up(level, available_toppings):
  level += 1
  name = ''
  symbol = ''
  new_toppings = con.LEVELS[level]
  # print(new_toppings)
  for key, info in new_toppings.items():
    # print(key)
    # print(info)
    if key == "name":
      name = info
    elif key == "symbol":
      symbol = info
    if name and symbol:
      available_toppings[name] = symbol
      name = ''
      symbol = ''
  fun_type("-------------------------------")
  fun_type(f"WELCOME TO LEVEL {level} OF PIZZATRON")
  fun_type("-------------------------------")
  # print(available_toppings)
  while True:
    fun_type("Would you like to be reminded of which toppings are available? "\
             "If you select n, only new unlocked toppings will be shown to you.")
    show_all = input("(y/n)\n")
    if show_all.upper() == "Y":
      fun_type("Here is a list of all toppings you have unlocked.")
      for name, symbol in toppings.items():
        fun_type(f"The topping {name} is represented by the symbol {symbol}.")
        break
    elif show_all.upper() == "N":
      for key, info in new_toppings.items():
        if key == "name":
          name = info
        elif key == "symbol":
          symbol = info
        if name and symbol:
          fun_type(f"The topping {name} is represented by the symbol {symbol}.")
          name = ''
          symbol = ''
      break
    else:
      fun_type("Please only type y or n as inputs! ")

# def y_n_input():


def score_pizza(made_pizza):
  made_pizza_lst = str_to_lst(made_pizza)

def fun_type(str):
  n = 0
  for i, char in enumerate(str):
    sys.stdout.write(char)
    n += 1
    sys.stdout.flush()
    time.sleep(1/((i**.5+1)*5))
    if n > 79 and char == " ":
      n = 0
      sys.stdout.write("\n")
      sys.stdout.flush()
  sys.stdout.write("\n")
  time.sleep(.75)

if __name__ == "__main__":
  toppings = {}
  level_up(0, toppings)