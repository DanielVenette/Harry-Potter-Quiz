# Harry Potter Quiz Game

<img src="HP%20Screenshot.png" height="500" width="333">

Welcome to the Harry Potter Quiz Game! This is a fun and interactive trivia game made for fans of the Harry Potter series. Test your knowledge about the actors who brought the beloved characters from the series to life on screen.

## Table of contents
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [How to Play](#how-to-play)
- [Contributions](#contributions)
- [License](#license)

## How It Works
The Harry Potter Quiz Game fetches character data from the Harry Potter API, and presents it to the player in the form of a quiz. The game includes questions about the actors who portrayed the characters in the series, their images, and other related data. The game uses a Tkinter-based user interface with Gryffindor-themed colors, and includes multiple-choice answers for each question.

## Tech Stack
- Python
- Tkinter for the GUI
- requests library for API interactions

## Setup
Here are the steps to setup this project locally on your machine:

1. First, you will need Python installed on your computer. If you don't have it installed, you can download it [here](https://www.python.org/downloads/).
2. You will need git.  If you don't already have it, you can download and install it [here](https://git-scm.com/downloads).
3. Clone this repository to your local machine. You can do this by running the following command in your terminal:
    ```bash
    git clone https://github.com/DanielVenette/Harry-Potter-Quiz.git
    ```
4. Navigate into the project directory:
    ```bash
    cd Harry-Potter-Quiz
    ```
5. Install the required dependencies with pip:
    ```bash
    pip install -r requirements.txt
    ```
6. Run the game:
    ```bash
    python main.py
    ```

## How to Play
On running the game, you will be presented with the name of a character from the Harry Potter series. You will have to guess who portrayed this character in the films. You have four options to choose from for each question. The game keeps track of your score, and provides feedback after each question. Good luck!

## Contributions
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the terms of the MIT license.
