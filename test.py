"""testing functions individually"""
import functions as fun
# import threading
import time
import random
import constants as con
# write a function that writes out the 
# results of the user's game stats

# total accumulated points
# last made pizza
# name
# level #
def countdown():
    global topping_timer

    topping_timer = 3

    while topping_timer > 0 and restart == False:
        topping_timer -= 1
        time.sleep(1)
        print("hello")
    return False
    # true means that it has run out of time

if __name__ == "__main__":
    
    # testing the generating toppings to make sure it works correctly
    """level = 0
    total_score = 0
    
    
    toppings = {'cheese':'꒦','pepperoni':'e','mushroom': '𓋼','meatball':"O",'pineapple':'ߜ'}
    symbols_lst = ['꒦','e','𓋼',"O",'ߜ']


    # fun.add_new_symbols(toppings, symbols_lst)
    picked_toppings = fun.pick_toppings(symbols_lst)
    target = fun.generate_pizza(picked_toppings)

    print(picked_toppings)
    print(target)"""
    # trying out the time function
    """restart = False
    countdown_thread = threading.Thread(target = countdown)
    countdown_thread.start()

    answer = input("f\n")
    if answer:
        restart = True
        time.sleep(5)
        countdown_thread = threading.Thread(target = countdown)
        restart = False
        countdown_thread.start()
    answer = ''"""

    level = 0
    total_score = 0
    
    
    toppings = {'cheese':'꒦','pepperoni':'e','mushroom': '𓋼','meatball':"O",'pineapple':'ߜ'}
    symbols_lst = ['꒦','e','𓋼',"O",'ߜ']


    # fun.add_new_symbols(toppings, symbols_lst)
    picked_toppings = fun.pick_toppings(symbols_lst)
    target = fun.generate_pizza(picked_toppings)

    print(picked_toppings)
    print(target)

    while True:
      if total_score > level * 4.0 or level == 0:
         lose = ''
         quit_ = ''
         level += 1
         win = fun.level_up(level, toppings)
         # print(win)
         if win == False:
            # print(level)
            if level < 5:
               rounds = level
            else:
               rounds = 5
               
            for _ in range(rounds):
               fun.add_new_symbols(toppings, symbols_lst)
               picked_toppings = fun.pick_toppings(symbols_lst)

               target = fun.generate_pizza(picked_toppings)
               fun.fun_type("...")
               fun.fun_type(random.choice(con.CUSTOMER_INTRO))
               fun.fun_type(random.choice(con.CUSTOMER_ORDER))
               print(target)
               time.sleep(3)
               # allow the user to attempt to recreate the pizza
               fun.fun_type("Making the pizza dough...")
               time.sleep(.25)
               made_pizza = fun.input_pizza(toppings)
               # generate a pizza
               score = fun.score_pizza(target, made_pizza, picked_toppings)
               total_score += score
               print(score)
               print(total_score)
               """if score < 4.5:
                  lose = True 
                  break"""
         else:
            break # win == True
      else:
         lose = True
         break

    if lose == True:
      fun.fun_type("Sorry, looks like you lost. ")
      fun.fun_type("Printing a file of your game stats to your current directory! ")
      fun.fun_type("Quitting the game. Thanks for playing! ")
      time.sleep(1)
      fun.write_stats(made_pizza,"lose")
    elif win == True:
      fun.fun_type("CONGRATULATIONS! You have completed all levels of Pizzatron.")
      fun.fun_type("Printing a file of your game stats to your current directory! ")
      fun.fun_type("Quitting the game. Thanks for playing! ")
      time.sleep(1)
      fun.write_stats(made_pizza,"win")
    elif quit_ == True:
      fun.fun_type("Aw, looks like you chose to quit.")
      fun.fun_type("Printing a file of your game stats to your current directory! ")
      fun.fun_type("Quitting the game. Thanks for playing! ")
      time.sleep(1)
      fun.write_stats(made_pizza,"quit")
    else:
      print("restarting the loop! ")