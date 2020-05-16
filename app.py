from flask import Flask, jsonify, request
import sys
import time
import numpy as np
import random
import os


# initialize our Flask application
app= Flask(__name__)

@app.route("/codenames", methods=["GET"])
def generate_codenames():
    context = {}
    context["board"] = play_codenames()
    response = jsonify(**context)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/boggle", methods=["GET"])
def generate_boggle():
    context = {}
    context["board"] = play_boggle()
    response = jsonify(**context)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------BOGGLE------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #


DICE = [
        ['Z', 'N', 'H', 'R', 'N', 'L'],
        ['A', 'O', 'O', 'T', 'T', 'W'],
        ['K', 'P', 'S', 'A', 'F', 'F'],
        ['T', 'O', 'I', 'E', 'S', 'S'],
        ['V', 'D', 'L', 'Y', 'E', 'R'],
        ['N', 'G', 'A', 'E', 'E', 'A'],
        ['S', 'H', 'O', 'A', 'P', 'C'],
        ['X', 'L', 'R', 'D', 'E', 'I'],
        ['N', 'H', 'Qu', 'I', 'U', 'M'],
        ['O', 'U', 'T', 'M', 'I', 'C'],
        ['S', 'U', 'N', 'I', 'E', 'E'],
        ['W', 'T', 'V', 'H', 'E', 'R'],
        ['W', 'E', 'N', 'H', 'E', 'G'],
        ['L', 'E', 'T', 'R', 'T', 'Y'],
        ['T', 'I', 'D', 'S', 'T', 'Y'],
        ['A', 'O', 'O', 'B', 'B', 'J'],
        ]


def clear():
    os.system("clear")


def prompt():
    prompt = "Play a round? (y/n): "
    response = input(prompt)
    return response


def get_command():
    """Prompt for and returns a command."""
    yes = set(["yes", "y"])
    no = set(["no", "n"])

    response = ""
    while response not in yes and response not in no:
        response = prompt()
    return response


def generate_permutation(num_dice=16):
    "Return a permutation of the ints from 0 to 15."""
    return np.random.permutation(list(range(0, num_dice)))


def print_board(permuted_letters):
    qu_column = -1
    if 'Qu' in permuted_letters:
        qu_index = permuted_letters.index('Qu')
        qu_column = qu_index % 4
    print("\n")
    col = 0
    for letter in permuted_letters:
        if col % 4 == qu_column and letter != 'Qu':
            print("", sep=' ', end=' ', flush=False)
        print(letter, sep=' ', end=' ', flush=False)
        if col % 4 == 3:
            print("")
        col += 1

def start_timer():
    t = 180
    intervals = set([180, 150, 120, 90, 60, 30, 15,
                     10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    print("\nBEGIN!")
    while t > 0:
        if t in intervals:
            print(t, sep=' ', end=' ', flush=True)
        time.sleep(1)
        t -= 1
    clear()
    print("TIME!")
    
    delay = 3
    time.sleep(delay)


def play_boggle():
    """Run a thread that plays boggle."""
    # First, generate and print board
    # Sample one letter from each die
    letters = []
    for die in DICE:
        letters.append(random.sample(die, 1)[0])
    num_dice = 16
    perm = generate_permutation()
    permuted_letters = [letters[p] for p in perm]

    formatted_board = []
    row = []
    counter = 1
    for letter in permuted_letters:
        row.append(letter)
        if counter % 4 == 0:
            formatted_board.append(row)
            row = []
            counter = 0
        counter += 1
    return formatted_board



# ------------------------------------------------------------------------------------------------ #
# --------------------------------------------CODENAMES------------------------------------------- #
# ------------------------------------------------------------------------------------------------ #

def play_codenames():
    print("hello")

#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)