PIZZATRON
Shiloh Chiu and Alex Boswell
CS1210
GITHUB REPO/VERSION HISTORY:
-https://github.com/shilohchiu/pizzatron

----- DESCRIPTION -----
Our program is inspired by the club penguin mini-game, Pizzatron, where the player is tasked with making a pizza based on a computer generated pizza. The player is scored on the pizza's accuracy. To honor the fact that our coursework this semester was done fully within Python’s command line, our program runs entirely in the command line as well, and visualized using ASCII art. We aimed to create a game that makes the most out of the simple building blocks and modules that we worked with in CS1210.
As the player “levels up”, more dictionary keys are unlocked.
At the end, the program outputs a .txt file that gives the user some of their stats, including 
the user’s score and the last pizza they made.

----- MODULES AND DEPENDENCIES -----

 
----- INSTRUCTIONS -----
(for running and testing the program)
The game itself is run in the file main.py. The game should be able to run all the way to its 
end without encountering any issues.

--- HOW WE TESTED OUR PROGRAM ---
To test our program, we relied on the line of code “if __name__ == “__main__” and the fact that 
we split our program into multiple different files. Essentially, our functions are separate from 
the main file and are instead imported into the main file. This allowed us to individually test 
each function in functions.py without running the entire program. For example, while working 
on our text engine, it would have been tedious to rerun the program in main.py to check if the 
speed the text engine was working was to our liking. Instead, we found it much easier to test 
the function itself in main.py to give it example strings that we predicted to be problematic 
without running the whole program in main.py. This allowed us to fix issues before they occurred, 
avoiding any nasty surprises while we were trying to code the main body of the program.

----- DEFECT LOG -----
Although this is not a coding defect per se, we did have an issue of the display of the ASCII 
art. Sometimes the output pizza would appear to be “jumbled” because the spacing of newly 
input characters was different than the default string supplied; the different lines of characters 
would not be lined up anymore.

----- WORK DISTRIBUTION -----
Our work was mostly done asynchronously. We decided divide the work by working on individual functions 
separately, but talked through the code with one another to ensure that neither of us would become 
confused with any conventions that we were using. For example, an issue We took advantage of the fact that GitHub allows you 
to resolve conflicts and save different version histories. When we did work in person together,
we did a lot of brainstorming ideas, pair programming, and rubber-ducking. We have multiple 
different python files that are imported into the actual 
working game. This allowed us to solve problems and issues faster and improve our 
code more efficiently. We did a good job at talking through our code and making sure there were 
no problems, and if we couldn’t figure out how to code something, we talked through what we were 
trying to achieve and the other person would try and implement it into our program.
We ran into some issues, such as trying to print things with special characters, but we quickly 
solved this issue using Stack Overflow and figuring out how to print the ASCII art without manually 
escaping each special character in the code. At first, we tried using the collaborative coding 
interface Replit, but we soon ran into problems using Replit (lag caused by cloud issues due to 
the collaborative editing process). We quickly changed plans and decided to pair-program on one 
computer within a local IDE. Eventually, we moved to GitHub to allow for online collaboration. 
This was very useful – neither of us had a very good understanding of using GitHub collaboratively, 
but after this project was a good introduction to how it works, and we became familiar with pushing, 
pulling, and resolving conflicts. All push/pull commit history is available via our GitHub link!

* ALEX *
    constants.py (building the topping dictionary, pizza string)
    functions.py (input_pizza(), replace_blank(), lst_to_str())
* SHILOH *
    constants.py (building the topping dictionary)
    wrote README.txt
    main.py (game intro, implementing functions)
    functions.py (generate_pizza(), str_to_lst(), fun_type(), score_pizza(), level_up(), write_stats())
----- CITATIONS -----
We were interested in putting color in the Python terminal to spice things up.
- https://www.javatpoint.com/how-to-print-colored-text-in-python

We encountered some problems printing the ASCII art and wanted to print the string without 
individually escaping each character.
- https://www.digitalocean.com/community/tutorials/python-raw-string 


- https://stackoverflow.com/questions/5852981/python-how-do-i-display-a-timer-in-a-terminal 

A brief introduction to the time module.
- https://codeinstitute.net/global/blog/how-to-wait-in-python/

I (Shiloh) used this source to make the text engine. I refined the code to make it more polished and suitable for our needs.
- https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line

Alex got the blank pizza ASCII art featured in our program from this site.
- https://ascii.co.uk/art/pizza