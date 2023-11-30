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


# def score_pizza(topping, made_pizza):