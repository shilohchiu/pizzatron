--- PIZZATRON ---
* also presented @ the CS fair! *
Shiloh Chiu and Alex Boswell
CS1210
GITHUB REPO/VERSION HISTORY:
-https://github.com/shilohchiu/pizzatron

----- DESCRIPTION -----
Our program is inspired by the club penguin mini-game, Pizzatron, 
where the player is tasked with making a pizza based on a random 
computer-generated pizza. The player is scored on their pizza's 
accuracy to the expected pizza. They are tasked with making 2 pizzas 
per level, and if their cumulative score is high enough, 
they pass to the next level. The difficulty of the game increases based 
on the complexity of the pizza that the user has to make. As the player 
“levels up”, more toppings are unlocked, and the possibility of generating 
a more complicated pizza increases. At the end, the program 
outputs a .txt file that gives the user some of their stats, including 
the user’s score, the last pizza they made, and whether they won or 
lost. We tried to add little things to spice up our project a little, 
like using a text engine or randomly generated messages from a 
defined constant list of messages. To honor the fact that our 
coursework this semester was done fully within Python’s command line, 
our program runs entirely in the command line as well and is visualized 
using ASCII art. We aimed to create a game that makes the most 
out of the simple building blocks and modules that we worked with 
in CS1210.

----- MODULES AND DEPENDENCIES -----
Our game only runs on modules that come in the Python package.
- time
- random
- sys
 
----- INSTRUCTIONS -----
(for running and testing the program)
The game itself is run in the file main.py. The game should be able to 
run to its end (if you level up enough; the game has 10 
levels) without encountering any issues and successfully 
write a .txt file of your stats and state whether you lost or won, and 
then terminate.

To play the game, simply run the game in the terminal and build 
the pizza using toppings that are available to you. This can be done 
by typing the name of the pizza topping when the blank pizza is 
displayed on the screen and you are prompted for a topping. Because the 
program writes to the current directory, please make sure before 
running the program that you are within the directory that the 
game is running in. This means that it will be easier for you to 
find the output file.

The score of your pizza is based on the ratio of correct toppings, 
if you missed any given toppings, or if you added toppings not 
ordered by the customer. Once you fail to meet the calculated 
number of points expected to pass to a certain level, you lose. 
If you successfully make all pizzas for every level (10 total levels) 
you will win. Either way, the program should write out a txt file.

As you level up, the possibility of getting a more complicated pizza 
will increase, but please note it is still possible to get a less 
complicated pizza at a higher level (i.e, a pizza with one kind of 
topping at level 8). This means the first two pizzas should be cheese 
pizzas because the only topping unlocked in level 1 is cheese.

To fully test our program, please lose purposefully and also try to 
win purposefully!

TO LOSE:
- To lose, you simply have to pass level one and then create 
"incorrect pizzas" after that level. For example, if at level 2 
I am given pizza that only has cheese as a topping, I would only 
put on pepperoni. I will keep making incorrect pizzas to 
"lose" and see if the program works as expected (terminates and 
writes a lose file.)

TO WIN:
- You win after unlocking all 10 possible toppings and making 
pizzas as correctly as possible. To do this, make all the pizzas 
that are given to you to the best of your ability. After the tenth 
level, the program should tell you that you have won and write a .txt 
file that tells you your stats.

--- HOW WE TESTED OUR PROGRAM ---
To test our program, we relied on the line of code “if __name__ == 
“__main__” and the fact that we split our program into multiple 
different files. Essentially, our functions are separate from 
the main file and are instead imported into the main file. 
This allowed us to individually test each function in functions.py 
without running the entire program. For example, while working 
on our text engine, it would have been tedious to rerun the program 
in main.py to check if the speed the text engine was working was 
to our liking. Instead, we found it much easier to test 
the function itself in test.py (a separate file that imports in 
functions.py) to give it example strings that 
we predicted to be problematic without running the whole program 
in main.py. This allowed us to fix issues before they occurred, 
avoiding any nasty surprises while we were trying to code the 
main body of the program. This was also useful for checking 
to see if the computer was generating pizzas correctly -- 
we were mostly checking to see if the function would return pizzas 
with blank spots or if the pizzas were becoming more complicated over 
time. We also used test.py to test out specific portions of the game, 
such as the introduction, ending, and playable content.

We chose not to include test.py in our final submissions because the 
code in that file is not necessary for our program.

We also used the print function to check if the functions were 
returning things as expected, changing lists as expected, scoring 
things correctly, etc.

We also ran the program ourselves from beginning to end 
using the directions given above to see if the program started 
and terminated as expected after we had finished writing the program.

----- DEFECT LOG -----
Something that we unfortunately did not account for is that the user 
can continue typing to the command line. This can mess up the input values, 
which is why the code validation appears to be faulty. If the user typed 
something while the computer was printing to the terminal, this 
value can accumulate without the user being aware of it. For example, 
if I type "y" into the command line but accidentally hit the keyboard 
while the computer is printing something, I may unknowingly submit 
a different value to the computer. Please refrain from typing on 
the keyboard unless you intend to input! Although this is not a coding 
defect per se, we did have an issue with the display of the ASCII art. 
Sometimes the output pizza would appear to be “jumbled” because the 
spacing of newly input characters was different than the default 
string supplied; the different lines of characters would not be lined up 
anymore.

We also fixed some bugs that are available to view on our repo.

----- WORK DISTRIBUTION -----
Our work was mostly done asynchronously. We decided to divide the work 
by working on individual functions separately but talked through 
the code with one another to ensure that neither of us would become 
confused with any conventions that we were using when we did work 
together in person. We took advantage of the fact that GitHub allows 
you to resolve conflicts and save different version histories. When 
we did work in person together, we did a lot of brainstorming ideas, 
pair programming, and rubber-ducking. We have multiple different Python 
files that are imported into the actual working game. This allowed us 
to solve problems and issues faster and improve our code more 
efficiently. We did a good job at talking through our code and making 
sure there were no problems, and if we couldn’t figure out how to code 
something, we talked through what we were trying to achieve, and the 
other person would try and implement it into our program.
We ran into some issues, such as trying to print things with special 
characters, but we quickly solved this issue using Stack Overflow and 
figuring out how to print the ASCII art without manually escaping each 
special character in the code. At first, we tried using the 
collaborative coding interface Replit, but we soon ran into problems 
using Replit (lag caused by cloud issues due to the collaborative 
editing process). We quickly changed plans and decided to pair-program 
on one computer within a local IDE for the rest of that session. 
We moved to GitHub to allow for online collaboration pretty early on 
in the project. This was very useful – neither of us had a very good 
understanding of using GitHub collaboratively, but this project 
was a good introduction to how it works, and we became familiar with 
pushing, pulling, and resolving conflicts. All push/pull commit history 
is available via our GitHub link! We both did work in creating/editing/
revising functions. We talked through many proposals for how we wanted 
our game to work. Some things we considered but did not make the 
final cut were making the text colored, having an option to quit, 
a timer, and a loading bar.

* ALEX *
    - constants.py (building the topping dictionary, pizza string)
    - functions.py (input_pizza(), replace_blank(), lst_to_str(),
                    topping_valid())
    - testing, final testing + editing, function revision, debugging
* SHILOH *
    - constants.py (building the topping dictionary, computer
                    generated output strings)
    - wrote README.txt
    - main.py (game intro, implementing functions, body of game)
    - functions.py (generate_pizza(), str_to_lst(), 
      fun_type(), score_pizza(), level_up(), write_stats(),
      add_new_symbols(), pick_toppings(), loading())
    - testing, final testing + editing, function revision
----- CITATIONS -----
We were interested in putting color in the Python terminal to 
spice things up.
- https://www.javatpoint.com/how-to-print-colored-text-in-python

We encountered some problems printing the ASCII art and wanted to 
print the string without individually escaping each character.
- https://www.digitalocean.com/community/tutorials/python-raw-string 

Sources referenced in displaying a timer.
- https://www.youtube.com/watch?v=Mp6YMt8MSAU
- https://stackoverflow.com/questions/5852981/python-how-do-i-display-a-timer-in-a-terminal 

A brief introduction to the time module.
- https://codeinstitute.net/global/blog/how-to-wait-in-python/

I (Shiloh) used this source to make the text engine. 
I refined the code to make it more polished and suitable for our needs.
- https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line

Alex got the blank pizza ASCII art featured in our program 
from this site.
- https://ascii.co.uk/art/pizza

Hieroglyphics/copy and paste ASCII characters:
- https://en.wikipedia.org/wiki/Template:Unicode_chart_Egyptian_Hieroglyphs
- https://copypastecharacter.com/all-characters