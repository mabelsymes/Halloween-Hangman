import random
import time

def getHangmanWord():
    with open("hangman_words.txt") as file:
        words = file.read().splitlines()[0].split(",")
    return random.choice(words).lower().strip()

def printHangman(lives, solved):
    print("  _______")
    print("  |/    |")
    print("  |     " + ("O" if lives < 7 else ""))
    print("  |    " + ("/" if lives < 6 else "") + ("|" if lives < 5 else "") + ("\\" if lives < 4 else ""))
    print("  |     " + ("|" if lives < 3 else ""))
    print("  |    " + ("/" if lives < 2 else "") + " " + ("\\" if lives < 1 else ""))
    print("__|__")
    print()

def updateHangman(guess, answer, solved, lives, trickState):
    if guess in answer:
        for i in range(len(answer)):
            if answer[i] == guess:
                solved[i] = guess
    else:
        lives -= 1
        if trickState:
            print("Uh oh... you guessed wrong! You lose two lives! >:)")
            lives -= 1
    return solved, lives

def doTreat(answer, solved):
    while True:
        index = random.randint(0, len(answer) - 1)
        if solved[index] == "_":
            letter = answer[index]
            for pos in range(len(answer)):
                if answer[pos] == letter:
                    solved[pos] = letter
            break
    return solved

def trickOrTreat():
    print("Trick or treat!! Would you like to take a risk?\n\nIf you get a treat, all instances of one letter in the word shall be revealed.\n\nIf you get a trick, then if your next guess is wrong you will lose two lives! If you manage to guess right, however, play continues as normal.\n\nWhat will it be? Will you take the risk?")
    while True:
        risk = input("Enter 'y' or 'n' to choose:> ")
        if risk == 'n':
            print("Very well, playing it safe! Your next guess will be treated as normal 🎃")
            return "normal"
        elif risk == 'y':
            print()
            print("Taking a risk, are we? Let's see what you get...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print(".")
            time.sleep(1)
            if random.randint(1, 2) == 1:
                print("Trick!!! Mwahahahaha - you will lose two lives if you guess wrong! 😈")
                return "trick"
            print("Treat!!! Here's some candy - or chocolate if you prefer: 🍬🍫. In addition, all instances of one letter in the word shall be revealed! Which gift did you like better?")
            return "treat" 
        print("Looks like you typed it incorrectly... here's a ghost for your troubles: 👻")

answer = getHangmanWord()
solved = ["_"] * len(answer)
guessedLetters = []
lives = 7

message = "| Welcome to Halloween Hangman! You have seven lives to guess the spookily-themed word... Beware of tricks along the way! |"
banner = " " + "~" * (len(message)-2)
print(banner)
print(message)
print(banner)

while True:

    trickState = False
    printHangman(lives, solved)
    if lives <= 0:
        print("You lose! The word was " + answer + ".")
        break
    print("Guessed letters: " + ", ".join(guessedLetters))
    print("word: " + " ".join(solved))

    if random.randint(1, 5) == 1:
        print()
        result = trickOrTreat()
        if result == "trick":
            trickState = True
        elif result == "treat":
            solved = doTreat(answer, solved)
            print()
            print("Here is your treat :)")
            print("word: " + " ".join(solved))

    if solved == list(answer):
        print()
        print("You win! The word was " + answer + ".")
        break

    print()
    while True:
        guess = input("Guess a letter: ")
        if guess in guessedLetters:
            print("You have already guessed that letter!")
            continue
        break
    guessedLetters.append(guess)

    solved, lives = updateHangman(guess, answer, solved, lives, trickState)
    if solved == list(answer):
        print()
        print("You win! The word was " + answer + ".")
        break
    

        