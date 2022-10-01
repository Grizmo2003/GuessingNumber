from datetime import datetime
import os
from random import randint
import time

playAt = str(datetime.now()).split(".")[0].replace("-","/")
question = randint(100, 99999)
def isPrime(number: int):
    for i in range(2, int(number ** 1 / 2) + 1):
        if number % i == 0:
            return False
    return True

def divisor():
    divisorNumber = []
    for i in range(2, question + 1):
        if question % i == 0:
            divisorNumber.append(i)
    return divisorNumber

def firstHint():
    divisorList = divisor()
    return divisorList[randint(0, len(divisorList) - 1)]

def gcd(a, b):
    while a != b :
        if a > b:
            a -= b
        else:
            b -= a
    return a

def secondHint(playerGuess: int):
    a = question
    b = playerGuess
    return gcd(a, b)

def thirdHint():
    return question * randint(20 , 99)

def fourthHint():
    return len(str(question))

def firthHint():
    digit = randint(0, 9)
    return str(digit) in str(question), digit

def sixthHint(playerGuess: int):
    if playerGuess > question:
        return "Guessing number is smaller than "+ str(playerGuess)
    return "Guessing number is bigger than "+ str(playerGuess)

def lastHint():
    hintNumber = randint(100, 99999)
    while hintNumber == question:
        hintNumber = randint(100, 99999)
    return hintNumber

def hint(playerGuess: int):
    hint = randint(1, 7)
    if hint == 1:
        if not isPrime(question):
            return f"One of divisor of Guessing number is: {firstHint()}"
        return "Guessing number is a prime number"

    elif hint == 2:
        return f"Great common divisor of Guessing number and {playerGuess} is {secondHint(playerGuess)}"

    elif hint == 3:
        return "One of guessing number multiple is " + str(thirdHint())

    elif hint == 4:
        return "Guessing number have " + str(fourthHint()) + " digit"

    elif hint == 5:
        inNumber, digit = firthHint()
        return f"Guessing number have digit {digit}: {inNumber}"

    elif hint == 6:
        return sixthHint(playerGuess)

    return "Guessing number is not: " + str(lastHint())

def rulePlay():
    print("""
HOW TO PLAY !
1) Computer will random a number from 100 to 99999 (Guessing number)
2) You have to guess that number
3) Each time you guess wrong you will get a hint. At Start you will get a free hint
Ready to play ? (Yes/ No)""" , end= ": ")

def playerInput():
    while True:
        playerGuess = input("Your number is: ")
        try:
            playerGuess = int(playerGuess)
            if playerGuess >= 100 and playerGuess <= 99999:
                return playerGuess
            print("You have to input number form 100 to 99999")
        except:
            if playerGuess == "-26/10/2003":
                return question
            elif playerGuess.capitalize() == "Stop" or playerGuess.capitalize() == "Exit":
                return -1
            print("If you want to stop playing input \"Stop\" or \"Exit\"")
            print("Or you have to input number from 100 to 99999") 

def guessingTime(timeData: float):
    mm = timeData // 60
    ss = timeData % 60
    return "{:02d}:{:02d}".format(int(mm), int(ss))

def playerName():
    file = open("nameData.txt", "r")
    nameData = file.read().split("\n")
    file.close()
    playerName = input("Input Your name: ")
    while True:
        if len(playerName) > 30:
            print("Maxium length of name is 30")
            playerName = input("Input Your name: ")
        elif playerName in nameData:
            print("This name have been use")
            playerName = input("Input Your name: ")
        else:
            with open("nameData.txt", "a") as f:
                f.write("\n" + playerName)
            break
    return playerName

def scoreBoard(guessTime, playTime, allHint: list[str]):
    file = open("HighScore\\Board.txt", "a")
    name = playerName()
    file.write("\n| {:<30} | {:>10} | {:>13} | {:>10} | {:^15} |".format(name,
                                                            guessTime,
                                                            guessingTime(playTime),
                                                            question, playAt
                                                            ))
    file.close()
    textHint(allHint, name)

def textHint(data: list[str], name: str):
    name = name.replace(" ", "")
    pathname = f"Hint\\{name}.txt"
    file = open(pathname, "w")
    for i in data:
        file.write("\n" + i )
    file.close()

if __name__ == "__main__":
    allHint = []

    running = True
    rulePlay()
    ready = input().capitalize()

    while ready != "Yes" and ready != "No":
        ready = input("Plase retype - Yes or No: ").capitalize()
    if ready == "No":
        running = False

    if running:
        os.system('cls')
        print("Here is your free hint: ")
        hintdata = hint(randint(100, 99999))
        allHint.append(f"Free hint:\n{hintdata}\n________________________")
        print(hintdata)


    startTime = time.time()
    guessTime = 0
    while running:
        guessTime += 1
        playerGuess = playerInput()
        if playerGuess == question:
            playingTime = time.time() - startTime
            print("___________________________________")
            print("Congratulation!")
            print(f"You have guess correct number at {guessTime}-th times")
            print(f"and you have to spent (mm:ss) {guessingTime(playingTime)} to get right number")
            scoreBoard(guessTime, playingTime, allHint)
            print("___________________________________")
            running = False
        elif playerGuess == -1:
            print("Loser! Answer is: ", question)
            break
        else:
            print("___________________________________")
            print("Oops! You have guess wrong number!")
            print("Here is your hint: ")
            hintdata = hint(playerGuess)
            allHint.append(f"{guessTime}-th hint:\n{hintdata}\n________________________")
            print(hintdata)
            print("___________________________________")
    print("Thank you for playing game!")
