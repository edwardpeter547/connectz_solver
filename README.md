# connectz_solver
The goal is to implement a game checker program for Connect Z. In Connect Z the concept of the traditional game of Connect Four is generalized to include playing frames of any size and a target lines of any length. When provided with a data file that describes a game of Connect Z your checker program should determine if that game was won, drawn or contains an error of some kind. The format of the data files and expected output is described in detail below.



# Programming Challenge: CONNECT Z GAME SOLVER.

This programming challenge is based on the classic game of Connect Four. In a traditional game of Connect Four, two players take turns to drop coloured counters into a vertical frame. The first player to achieve a horizontal, vertical or diagonal line of four or more counters of their own colour wins the game. Games can also result in a draw if the frame fills up with counters before either player can complete a line of four or more counters.

#### The Problem:
My goal is to implement a game checker program for Connect Z. In Connect Z the concept of the traditional game of Connect Four is generalized to include playing frames of any size and a target lines of any length. When provided with a data file that describes a game of Connect Z your checker program should determine if that game was won, drawn or contains an error of some kind.


## Solution Approach

#### Understanding Requirements:
My general Approach to solving problems like this is always first, understanding the problem and the solution domain.
In this case i am to, given a set of game configuration and set of moves as (input) in an ascii text file, determine the result of a connectz game.
connectz is a more scalable and robost implementation of the 
traditional connect 4 game. which has fixed configuration of 7x6 matrix
style game board and a fixed required winning move of 4 consecutive
linear moves either along the horizontal direction, vertical direction or the diagonal direction. i am to determine the following set of game conditions. given the input file.
    
    GAME CONDITION                      OUTPUT SPECIFICATION
    
* Draw condition                                0                  
* Win Condition for Player 1                    1
* Win Condition for Player 2.                   2
* Incomplete Game Condition                     3
* Illegal Continue                              4
* Illegal Row                                   5
* Illegal Column                                6
* Illegal Game                                  7
* Invalid File                                  8
* File Error                                    9

#### Solution Domain
I have approached this solution paying close attention to the input specification and the output requirement. 
i have broken down the solution into three (3) functional solution domains;

1 Successfully read input file and check all required input constraints

2 Analyze the Game Data read from the input file.

3 Generate and display Result for each of the game condition

####  Reading Input File: 
I implemented a ReadFile class that is responsible for all file handling operations. the ReadFile class gets the filename passed as a command line argument to the script, reads the content of the file and collaborates with other classes to handle other parts of the solution domain. 
I have also implemented within this domain a GameData class responsible for creating and managing the data structure to hold the game dimension read from the first line of the input file. this is the only data stored in memory during the ReadFile step. other data such as the player moves are not stored in memory to enhance performance and avoid the expensive overhead of storing an unexpected arbitrary large data in memory.

#### Analyze Inputs:
In the second step the content of the file is read line by line and ConnectZ class is responsible for analyzing and generating all the game conditions such as draw condition, win condition for player 1 and player 2. within this domain another class Utility is responsible for checking all constraints such as the case of an Ilegal Game, Illegal Column, Illegal Row, Illegal Continue, Incomplete etc. and generating the appropriate exit condition based on the constraint.

#### Displaying Result:
I have defined a Result class that has only one responsibility of accepting an Enum value representing a game condition, displays the game condition and exiting the program. The result class is only called when a particular game condition has been met and the program exits after displaying the result to the console.

#### Coding Style
The solution is built using python 3 and PEP8's coding convention.
i applied the use of certain best practices limited to the scope of
this project/solution such as the use of classes, classmethods, staticmethods, 
enums, list comprehensions, global constants for string literals, i have also avoiding the use of magic numbers where necessary to improve code readability.

#### Optimizations / Best Practices
I ensured i have used various best practices in my implementation to ensure that my code is optimal. ensuring that data is not stored in memory but data was read line by line from the input file.

I have also implemented an effective mathematical method
of computing diagonal of matrices to pick all the forward and backward diagonal elements to 
determine a diagonal win condition. since computing the diagonal win 
was abit more of an expensive task, i did the linear vertically and horizontally check 
first. this is very practical in cases where there is a hit on the
horizontal or vertical axis, so i don't have to compute the diagonal elements which were more expensive.

I employed good use of list comprehension in all my ilterations, to reduce code size and improve readability.

I defined various string constants and enum's to hold magic numbers. I also employed the use of classes and method to modularize code and abstract basic concepts. this improved my code redability.

I have written both method level documentation and employed comments where necessary to aid you in understanding how the pieces of my code work together. 

I have employeed good naming standards for variables, constants, classes etc strictly adhering to PEP8 conventions for name declaring and applying appropriate spacings.

#### Challenges:
I met a few challenge especially on deciding on the implementation details such as choosing the right data structure. a few other challenges was computing the win, draw conditions. since the requirement did not allow for any external libraries i found myself re-inventing the wheel which slowed down my development time.

#### Improvements:
I would love to write a generator script that accepts command line arguments needed to generate test cases for various conditions. the test cases and the corresponding result set can be stored in a database, this in turn can be feed into a Machine Learning Algorithm that can predict
game moves and expected results.


## Deployment

To deploy this project run

```bash
  pip install python3

```
Create  Virtual Environment Usin the Above Commands.

```bash
  python3 -m venv env

```

Activate Virtual Environment


```bash
  source env/Activate

```

## Running The Script

```python
python3 connectz.py inputfile.txt
```


## Running Tests

Paste the test data below for each of the test cases in an ascii test file and pass the file name as commandline argument to the python script for each of the test cases. below

Draw Condition
```bash
3 3 3
1
2
3
1
3
2
1
3
2

```
~~~
Expected Output: 0
~~~

Player 1 Win
```bash
3 3 3
1
2
1
2
1
```
~~~
Expected Output: 1
~~~

Player 2 Win
```bash
3 3 3
1
2
3
2
1
2
```
~~~
Expected Output: 2
~~~

Incomplete
```bash
3 3 3
1
2
3
1
```
~~~
Expected Output: 3
~~~

Illegal continue
```bash
3 3 3
1
2
1
2
1
2
```
~~~
Expected Output: 4
~~~

Illegal Row
```bash
3 3 3
1
2
2
1
1
2
2
```
~~~
Expected Output: 5
~~~

Illegal Column
```bash
3 3 3
1
2
3
4
```
~~~
Expected Output: 6
~~~

Illegal Game
```bash
3 3 4
1
2
3
1
3
2
1
3
2
2
```
~~~
Expected Output: 7
~~~

Invalid File
```bash
banana
```
~~~
Expected Output: 8
~~~


## Running Tests
I have created a simple python script 
## Author
#### Engr. Peter Goteh Yaanwa
- Github:[@edwardpeter547](https://www.github.com/edwardpeter547)
- LinkedIn: []()
- Twitter:  [@edwardpeter547](https://twitter.com/edwardpeter547)

