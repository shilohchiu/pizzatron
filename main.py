"""
PIZZATRON 3000
"""

import constants as con
import functions as fun

if __name__ == "__main__":
    # initializes the list of toppings (based on dictionary
    # toppings); changes as more toppings are available to 
    # the user
    toppings_list = ['cD', '𓆟', '฿']
    print(fun.generate_pizza(toppings_list,con.PIZZASTR))
    # print(fun.replace_blank(con.TOPPINGS['anchovy'], con.CHEESEPIZZA))