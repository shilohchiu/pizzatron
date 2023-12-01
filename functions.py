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

# def str_to_lst():


# def lst_to_str():


def replace_blank(topping, pizza):
  lst = []
  # reads through the pizza and replaces 
  # each underscore with the topping
  for character in pizza:
    lst.append(character)

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
  generated_pizza = []
  
  for character in pizza_template:
    generated_pizza.append(character)

  for i, topping in enumerate(picked_toppings):
    underscore_id = 1
    for c in range(len(generated_pizza)):
      
      if generated_pizza[c] == '_' and \
      generated_pizza[c - 1] == '(' \
      and generated_pizza[c+1] == ')':
        if len(picked_toppings) == 1 or i+1 == len(picked_toppings):
          choice = 1
        else:
          choice = random.random()

        

        if choice >= 0.5 or underscore_id == 1:
          generated_pizza[c] = topping# the current iteration of the topping
      # if it's the last topping, add one
      # the computer will check the user 
      # input to see if it's in the new list
        underscore_id += 1
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