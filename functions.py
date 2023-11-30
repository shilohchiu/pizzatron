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
"""

def replace_blank(topping, pizza):
  lst = []
  # reads through the pizza and replaces 
  # each underscore with the topping
  for character in pizza:
    lst.append(character)

  for c in range(len(lst)):
    if lst[c] == '_' and lst[c - 1] == '(' and lst[c+1] == ')':
      lst[c] = topping

    empty = ''
    p = 0
    for _ in lst:
        empty += lst[p]
        p += 1

  return empty


    
# print(empty)


# def make_pizza():