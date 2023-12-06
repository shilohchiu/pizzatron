"""
All the major constants our game relies on.
"""

LEVELS = {  1:
              {'name':'cheese',
              'symbol': '꒦'},
            2:
              {'name':'pepperoni',
               'symbol':'e'},
            3:
              {'name':'mushroom',
               'symbol': '𓋼'},
            4:
              {'name':'meatball',
               'symbol': "O"},
            5:
              {'name':'pineapple',
               'symbol': 'ߜ'},
            6:
              {'name':'bacon',
               'symbol': '฿'},
            7:
            {'name':'olive',
             'symbol': 'ʘ'},
            8:
            {'name':'jalapeno',
            'symbol': '⊛'},
            9:
            {'name':'anchovy',
            'symbol':'𓆟'},
            10:
            {'name':'basil',
            'symbol': 'φ'}
                }

PIZZASTR = r"""
                     _____
              __--~~~     ~~~--__
           ,/'   m%%%%%%%=@%%m   `\.
         /'  m%%%o(_)%%o%%o%%%o%%m  `\
       /'  %%@=%o%%%%o%%%o%%(_)o%%%%  `\
     /'  %(_)%%(_)%%%o%%%o%%%%=@(_)%%%o  \
    /  @=%%%o%%%%o%%%(_)%%o%%o%%%%o%%%o%  \
   /  %%%o%%%%=@%%%o%%%%@=%(_)%%=@%%(_)%o  \
  |  %%o%%%%o%%%=@%%(_)%%o%%%%o%%%%o%%o@%%  |
 |  %%%%(_)%%%%o%(_)o%%o%%%o%%%%o%%o%o@=%o%  |
 |  %%o%o%%o%%%%o%%o%%o%%%%=@%o(_)%%o%o%%%%  |
 |  %(_)%%%%(_)%=@%%%(_)o%%%o%%o%%@=%%(_)%%  |
 |  %%o%(_)%%%%%o%%%%%%=@%%(_)%%o%%%o%%%%%%  |
  |  %%o%%%%o%%%%(_)o%%%%o%o%%@=%(_)%%=@%%  |
   \  %@=%%o%(_)%%%%%o%(_)%%%o%%o%%o%%%%%  /
    \  %%(_)%%%=@%(_)%o%o%%(_)%o%(_)%@=%  /
     \. ~%%%o%%%%%o%o%=@%%o%%@=%%o%%o%% ,/
       \. ~o%%(_)%%%%%o%(_)%%o%(_)o%% ,/
         \_ ~%%o%=@%(_)%%o%%(_)%%~  ,/
           `\__~~~o%%%%o%%%%%~  __/'
               `~--.._____,,--~'
"""

CUSTOMER_INTRO = ["Guess what? We have a customer. ", 
                  "Here comes a customer!!! ", 
                  "A customer wants a pizza! "]

CUSTOMER_ORDER = ["This is the pizza they ordered. ", 
                  "They want a pizza like this: ", 
                  "Hopefully you can make their pizza. "]

STATS = ["----------------------------\n",
         "THANKS FOR PLAYING PIZZATRON\n",
         "----------------------------\n"
]

STARS = ["★","☆"]