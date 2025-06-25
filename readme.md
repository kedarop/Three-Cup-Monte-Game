# **Three-Cup Monte Game**

This repository contains a simple Python implementation of the classic "Three-Cup Monte" game. The primary goal of this project is to demonstrate how multiple functions can interact, return objects to each other, and combine to create a cohesive game logic.

## **🎯 Game Concept**

The game begins with three cups, one of which discreetly hides a "red ball" (represented by a capital 'O'). The cups are then "shuffled" (their positions are randomized). The user's objective is to guess the correct location of the ball after the shuffle.

In this simple version, the shuffling process itself is not visually displayed to the user, making the guess purely random.

## **✨ Features & Learning Points**

* **Function Interaction:** Demonstrates how different functions can call each other and pass data (lists, integers) back and forth.  
* **List Manipulation:** Utilizes Python's built-in random.shuffle function to randomize list elements.  
* **Custom Function Creation:** Shows how to wrap a built-in function to add custom behavior (like returning the shuffled list).  
* **User Input Handling:** Implements a loop to ensure valid user input for guessing.  
* **Conditional Logic:** Uses if/else statements to check the player's guess.

## **🎲 How to Play**

1. The game initializes three "cups" (a Python list) with one "ball" ('O').  
2. The "cups" are secretly shuffled.  
3. You will be prompted to guess the position of the ball (0, 1, or 2).  
4. The game will tell you if your guess was correct. If wrong, it will reveal the final positions of the cups.

## **🏗️ Project Structure & Core Components**

The game logic is broken down into several functions, typically defined at the top of the script, with the main game flow at the bottom.

### **1\. Shuffling a List in Python**

Python's random module provides a shuffle function that modifies a list in place.

from random import shuffle

example\_list \= \[1, 2, 3, 4, 5\]  
shuffle(example\_list)  
print(example\_list) \# The list 'example\_list' is now rearranged

### **2\. Creating a Custom Shuffle Function**

To make the shuffle functionality more versatile by having it return the shuffled list, we create a wrapper function:

from random import shuffle

def shuffle\_list(mylist):  
    """  
    Shuffles a given list in place and then returns the modified list.

    Args:  
        mylist (list): The list to be shuffled.

    Returns:  
        list: The shuffled list.  
    """  
    shuffle(mylist)  
    return mylist

### **3\. Setting Up the Game List**

Our game uses a simple list of three strings: two empty strings and one capital 'O' representing the ball.

game\_list \= \['', 'O', ''\]

### **4\. Handling Player Input**

A function player\_guess() prompts the user for their guess, ensuring that the input is one of the valid indices (0, 1, or 2). The input is then cast to an integer for list indexing.

def player\_guess():  
    """  
    Prompts the user to pick a number (0, 1, or 2\) and validates the input.

    Returns:  
        int: The validated integer guess.  
    """  
    guess \= ''  
    while guess not in \['0', '1', '2'\]:  
        guess \= input('Pick a number: 0, 1, or 2: ')  
    return int(guess)

### **5\. Checking the Player's Guess**

The check\_guess() function takes the shuffled list and the player's guess as arguments to determine if the guess was correct. It provides feedback to the user.

def check\_guess(mylist, guess):  
    """  
    Checks if the player's guess matches the ball's position in the list.

    Args:  
        mylist (list): The shuffled game list.  
        guess (int): The player's guessed index.  
    """  
    if mylist\[guess\] \== 'O':  
        print('Correct\!')  
    else:  
        print('Wrong guess\!')  
        print(f"The list was: {mylist}") \# Reveals the list if the guess was wrong

### **6\. Putting It All Together: The Game Script**

Finally, all the functions are combined to run the game sequence. Typically, function definitions are at the top of your Python file, and the main execution logic is at the bottom.

from random import shuffle \# Import at the top of your file

\# \--- Function Definitions (as shown above) \---

def shuffle\_list(mylist):  
    shuffle(mylist)  
    return mylist

def player\_guess():  
    guess \= ''  
    while guess not in \['0', '1', '2'\]:  
        guess \= input('Pick a number: 0, 1, or 2: ')  
    return int(guess)

def check\_guess(mylist, guess):  
    if mylist\[guess\] \== 'O':  
        print('Correct\!')  
    else:  
        print('Wrong guess\!')  
        print(f"The list was: {mylist}")

\# \--- Game Logic \---  
print("--- Welcome to Three-Cup Monte\! \---")

\# 1\. Set up the initial game list  
mylist \= \['', 'O', ''\]

\# 2\. Shuffle the list  
mixedup\_list \= shuffle\_list(mylist)

\# 3\. Get the player's guess  
guess \= player\_guess()

\# 4\. Check the guess  
check\_guess(mixedup\_list, guess)

print("--- Game Over \---")

## **🚀 Usage**

To run this game:

1. Save the combined Python code (with all functions and game logic) as a .py file (e.g., three\_cup\_monte.py).  
2. Open your terminal or command prompt.  
3. Navigate to the directory where you saved the file.  
4. Run the script using:  
   python three\_cup\_monte.py

## **📄 License**

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT). (You might want to create a LICENSE file in your repo later).
