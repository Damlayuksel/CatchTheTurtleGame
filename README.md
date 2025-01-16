# Turtle Game

This is a simple Turtle game where you have to click on randomly appearing turtles to score points before the time runs out. The game offers three difficulty levels: Easy, Medium, and Hard.

![Image](https://github.com/user-attachments/assets/d3c0f2de-d5a5-416c-b282-4d6511a960b5)

## Features
- Choose between three difficulty levels: Easy, Medium, and Hard.
- Click on the visible turtles to score points.
- The game has a countdown timer that ends when time runs out.
- Displays the score at the top of the screen.
- Fun and interactive!

## Game Rules
### Difficulty Levels: Choose between Easy, Medium, or Hard.
- **Easy**: Turtles are shown for 1 second, and the game lasts for 20 seconds.
- **Medium**: Turtles are shown for 0.5 seconds, and the game lasts for 15 seconds.
- **Hard**: Turtles are shown for 0.2 seconds, and the game lasts for 10 seconds.

### Scoring:
Click on the turtles when they appear on the screen to score points. Each turtle clicked adds one point to your score.

### Game Over:
The game ends when the countdown reaches zero.

## Installation
Make sure you have Python installed on your system. You'll also need the turtle module, which comes pre-installed with Python.

To play the game:
1. Clone or download the Python script (CatchTheTurtle.py) .
2. Run the script using Python.

## Code Explanation
### Setting up the screen:
We configure the Turtle screen with a pink background and a title "Turtle Game".

### Difficulty Settings:
We use a dictionary `difficulty_settings` to define the time for which turtles will appear and the total game time for each difficulty level.

### Game Functions:
- `setup_score_turtle()`: Sets up the score display at the top of the screen.
- `make_turtle(x, y)`: Creates a turtle at the given (x, y) coordinates and makes it clickable to increase the score.
- `set_turtles()`: Places multiple turtles on the screen.
- `hide_turtles()`: Hides all the turtles on the screen.
- `show_randomly()`: Randomly displays one turtle at a time, based on the difficulty level.
- `countdown()`: Displays the countdown timer and ends the game when the time reaches zero.
- `select_difficulty()`: Prompts the user to select a difficulty level.

## How to Play
1. **Start the Game**: Upon starting the game, you will be asked to select a difficulty level: Easy, Medium, or Hard.
2. **Click the Turtles**: When turtles appear on the screen, click on them to score points.
3. **Watch the Timer**: Keep an eye on the countdown timer. The game will end when the timer reaches zero.

## Game Controls
- **Mouse**: Click on the turtles that appear to score points.
- **Keyboard**: You can use the keyboard to input the difficulty level at the beginning.

## Enjoy the Game! 🎮
Happy playing and try to beat your high score!
