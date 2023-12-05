"""
PIZZATRON 3000
Shiloh Chiu and Alex Boswell
"""

import functions as fun
import time
import random
import constants as con

if __name__ == "__main__":
   level = 0
   total_score = 0
   toppings = {}
   symbols_lst = []

   fun.fun_type("----PIZZATRON: CS1210 FINAL PROJECT-----")
   fun.fun_type("Created by: Shiloh Chiu and Alex Boswell")
   while True:
      try:
         fun.fun_type("Hello! What's your name?")
         name = input("")
         break
      except ValueError:
         fun.fun_type("That's not a valid name!")
   name = name.capitalize()
   fun.fun_type(f"Welcome to Pizzatron, {name}!")
   fun.fun_type(f"Are you ready to make some pizzas, {name}?")
   while True:
      answer = input("(y/n)\n")
      if answer.upper() == 'Y':
         fun.fun_type(f"Great! Love your enthusiasm, "\
                      f"{name}. Let's get started.")
         break
      elif answer.upper() == 'N':
         fun.fun_type(f"Too bad! You're going to learn to make some"\
                      " pizzas anyways, {name}. Let's get started.")
         break
      else:
         fun.fun_type("Please input y or n as answers! ")
   fun.fun_type("Okay, let's go over the rules of how to make the pizza.")
   fun.fun_type("As you level up, you get to unlock new ingredients! "\
                "It's up to you to remember what ingredients are on "\
                "the pizza and to put all the toppings on the pizza.")
   fun.fun_type("The more pizza toppings you unlock, "\
                "the greater the possibility of complicated pizzas.")
   fun.fun_type("At the beginning of each level, you'll be shown a key of "\
                "the toppings and what each topping is represented as.")
   fun.fun_type("At the beginning of each round, the "\
                "computer will show you a pizza.")
   fun.fun_type("To recreate the pizza, just type the name of the topping, "\
                "one at a time. For example, if I want put an anchovy on "\
                "the pizza, I would just type 'anchovy' into the terminal.")
   fun.fun_type("Try to keep the ratio of the toppings consistent -- this "\
                "will impact your score!")
   fun.fun_type("When the pizza is completely full, we'll score your pizza "\
                "and tell you how accurate it is.")
   fun.fun_type("Once you reach the end of the game, we'll save a file "\
                "of your results to your computer.")
   fun.fun_type("You might wanna make your terminal full screen for this.")
   time.sleep(1)
   fun.fun_type("Okay, let's begin!")
   while True:
      if total_score > level * 4.0 or level == 0:
         lose = ''
         quit_ = ''
         level += 1
         win = fun.level_up(level, toppings)
         if win == False:
            rounds = 2
               
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
         else:
            break
      else:
         lose = True
         break

   if lose == True:
      fun.fun_type("Sorry, looks like you lost. ")
      fun.fun_type("Printing a file of your game stats to your current"\
                  " directory! This file is named pizzatron.txt")
      fun.fun_type("Quitting the game. Thanks for playing! ")
      time.sleep(1)
      fun.write_stats(made_pizza,"lost", total_score)
   elif win == True:
      fun.fun_type("CONGRATULATIONS! You have completed all levels of Pizzatron.")
      fun.fun_type("Printing a file of your game stats to your current"\
                  " directory! This file is named pizzatron.txt")
      fun.fun_type("Quitting the game. Thanks for playing! ")
      time.sleep(1)
      fun.write_stats(made_pizza,"won", total_score)
   """elif quit_ == True:
      fun.fun_type("Aw, looks like you chose to quit.")
      fun.fun_type("Printing a file of your game stats to your current"\
                  " directory! This file is named pizzatron.txt")
      fun.fun_type("Quitting the game. Thanks for playing! ")
      time.sleep(1)
      fun.write_stats(made_pizza,"quit", total_score)"""