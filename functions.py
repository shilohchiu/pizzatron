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
- allows more dictionary keys to be unlocked
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
import constants

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
    user_pizza = str_to_lst(constants.PIZZASTR)
    toppingnum = 1
    while '(_)' in lst_to_str(user_pizza):
        newtop = input("What will you make for topping #" + str(toppingnum) + "?")
        for v in user_pizza:
            if user_pizza[v] == '_' and user_pizza[v-1] == '(':
                user_pizza[v] = newtop
            break
        print(lst_to_str(user_pizza))

def generate_pizza(unlocked_toppings, pizza_template):
  # takes the lst of unlocked pizza toppings
  # as an argument
  picked_toppings = [] # a list of toppings from the
              # unlocked list of pizza 
              # toppings
  for _ in range(random.randint(1,len(unlocked_toppings))):
    i = random.choice(unlocked_toppings)
    if i not in picked_toppings:
      picked_toppings.append(i)

  # return picked_toppings

  # picks random underscores and replaces them
  # with each of the symbols
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
            generated_pizza[c] = topping# the current iteration of the topping
      # if it's the last topping, add one
      # the computer will check the user 
      # input to see if it's in the new list
    
  new_pizza = ''
  p = 0
  for _ in generated_pizza:
      new_pizza += generated_pizza[p]
      p += 1

    # check and see if the list of toppings is
    # actually in the generated pizza
  print(picked_toppings)
  for i, topping in enumerate(picked_toppings):
    if topping not in generated_pizza:
      picked_toppings.pop(i)
  print(picked_toppings)

  return new_pizza

# def score_pizza(topping, made_pizza):
