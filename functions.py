"""
All the major functions our game relies on.

GUIDE: 
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
what level you are currently on and also the dictionary 
keys and what they are represented as symbolically.
- if level != 1 then the computer will tell you the 
number of points you had on each round (calculated in 
the score pizza function)
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

import random
import constants as con
import time
import sys

def str_to_lst(str):
  lst = []
  for char in str:
    lst.append(char)
  return lst


def lst_to_str(lst1):
    str1 = ""
    for char1 in lst1:
        str1 += char1
    return str1


def open_space(a, b, c):
  # returns True if the set of characters
  # is an an empty space in the pizza
  if b == '_' and a == '(' and c == ')':
    return True
  else:
    return False


def replace_blank(topping, pizza):
  lst = str_to_lst(pizza)

  for c in range(len(lst)):
    if open_space(lst[c-1] ,lst[c], lst[c+1]):
      lst[c] = topping

    new_pizza = ''
    p = 0
    for _ in lst:
        new_pizza += lst[p]
        p += 1

  return new_pizza

def topping_valid(userkey, topps):
  cur_key = userkey
  while cur_key not in topps:
    cur_key = input("Sorry, " + cur_key + " is not a valid pizza topping! Type a valid topping here: ")
  return topps.get(cur_key)

def input_pizza(toppings):
  user_pizza = str_to_lst(con.PIZZASTR)
  toppingnum = 1
  print(lst_to_str(user_pizza))
  while '(_)' in lst_to_str(user_pizza):
    newtop = input("What will you make for topping #" + str(toppingnum) + "? ")
    top_symbol = topping_valid(newtop.lower(), toppings)
    i1 = 1
    for v in user_pizza:
      if open_space(user_pizza[i1-1], user_pizza[i1], user_pizza[i1+1]):
        user_pizza[i1] = top_symbol
        break
      i1 += 1
            
    print(lst_to_str(user_pizza))
    toppingnum += 1
  return user_pizza

def add_new_symbols(toppings, symbols):
  for symbol in toppings.values():
    if symbol not in symbols:
      symbols.append(symbol)

def pick_toppings(unlocked_toppings):
  picked_toppings = []
  for _ in range(random.randint(1,len(unlocked_toppings))):
    i = random.choice(unlocked_toppings)
    if i not in picked_toppings:
      picked_toppings.append(i)
  return picked_toppings

def generate_pizza(picked_toppings):
  generated_pizza = str_to_lst(con.PIZZASTR)

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
  for i, topping in enumerate(picked_toppings):
    if topping not in generated_pizza:
      picked_toppings.pop(i)
  
  return new_pizza

def level_up(level, available_toppings):
  name = ''
  symbol = ''
  try:
    new_toppings = con.LEVELS[level]
  except KeyError:
    return True
  for key, info in new_toppings.items():
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
  while True:
    fun_type("Would you like to be reminded of which toppings are available? "\
             "If you select n, only new unlocked toppings will be shown to you.")
    show_all = input("(y/n)\n")
    if show_all.upper() == "Y":
      fun_type("Here is a list of all toppings you have unlocked.")
      for name, symbol in available_toppings.items():
        fun_type(f"The topping {name} is represented by the symbol {symbol}.")
      return False
    elif show_all.upper() == "N":
      fun_type("Here is a list of the new toppings you have unlocked.")
      for key, info in new_toppings.items():
        if key == "name":
          name = info
        elif key == "symbol":
          symbol = info
        if name and symbol:
          fun_type(f"The topping {name} is represented by the symbol {symbol}.")
          name = ''
          symbol = ''
      return False
    else:
      fun_type("Please only type y or n as inputs! ")
    time.sleep(2)

def score_pizza(target, made_pizza, picked_toppings):
  score = 5
  made_pizza_lst = str_to_lst(made_pizza)
  target_pizza_lst = str_to_lst(target)
  for topping in picked_toppings:
    if topping not in made_pizza_lst:
      score -= .2
  for char in made_pizza_lst:
    if char not in target_pizza_lst:
      score -= .2
  for topping in picked_toppings:
    expected = target_pizza_lst.count(topping)
    actual = made_pizza_lst.count(topping)
    score -= abs(1 - ( actual / expected ))
  return score

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

def write_stats(last_made_pizza, win_lose_quit, total_score, name):
  with open("pizzatron.txt", "w") as f:
    f.write(f"PIZZATRON STATS FOR {name}:\n")
    for line in con.STATS:
      f.write(line)
    f.write(f"YOU {win_lose_quit.upper()} THIS GAME!\n")
    f.write(f"Your score was {total_score}.\n")
    if last_made_pizza:
      f.write("This is your last made pizza:\n")
      for char in last_made_pizza:
        f.write(char)
    else:
      f.write("You didn't make any pizzas.")
    f.write("\nTHANK YOU FOR PLAYING PIZZATRON")

def loading(n):
  for _ in range(n):
    for char in r"""\|/—\|/—""":
      sys.stdout.write(char)
      n += 1
      sys.stdout.flush()
      sys.stdout.write("\b")
      time.sleep(.1)
  sys.stdout.write("\n")
  time.sleep(.75)

if __name__ == "__main__":
  loading(10)

