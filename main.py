"""
PIZZATRON 3000
"""

import constants as con
import functions as fun
import random as rand

if __name__ == "__main__":
    # initializes the list of toppings (based on dictionary
    # toppings); changes as more toppings are available to 
    # the user
    toppings_list = []
    print(fun.replace_blank(con.TOPPINGS['anchovy'], con.CHEESEPIZZA))