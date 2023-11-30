"""
All the major functions our game relies on.
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