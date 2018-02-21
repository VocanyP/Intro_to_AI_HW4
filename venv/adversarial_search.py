import sys
import re
import ast
import numpy
from math import sqrt
from game import Game
import game

'''
load initial parameters
initialize the parameters

begins the game
'''
import action_process

def mean(list):

    #########################################
    ######### YOUR CODE GOES HERE ###########
    #########################################


def stdDeviation(list):

    #########################################
    ######### YOUR CODE GOES HERE ###########
    #########################################


def print_stats(deals, faceUpCards, legalActions):
    
    # Calculate the mean and standard deviation for faceUpCards #
    #########################################
    ######### YOUR CODE GOES HERE ###########
    #########################################
    
    # Calculate the mean and standard deviation for legalActions #
    #########################################
    ######### YOUR CODE GOES HERE ###########
    #########################################

    print("Statistics over "+str(deals)+" games:")
    print(" --- Face-up cards --- ")
    print("\t\tAverage: " + ", ".join([str(item) for item in faceUpC_mean]))
    print("\t\tStandardDeviation: " + ", ".join([str(item) for item in faceUpC_std]))
    print("")

    print(" --- Legal actions --- ")
    print("\t\tAverage: " + ", ".join([str(item) for item in legalA_mean]))
    print("\t\tStandardDeviation: " + ", ".join([str(item) for item in legalA_std]))
    print("")


def EmpiricalValues(deals):
    """
    This function computes and prints out the mean and std deviation of 'n' random games
    """
    global noOfFaceUpCardsPerGame, noOfLegalActionsPerGame
    noOfFaceUpCardsPerGame = []
    noOfLegalActionsPerGame = []

    for i in range(deals):
        print("\n\nDeal %d" % i)
        newGame = Game()
        firstPlayer = newGame.firstPlayer() # choosing randomly the first player

        if firstPlayer == "player" :
            dealer = newGame.computer
        else:
            dealer = newGame.player

        tableCanBeSwept = newGame.checkIfInitialTableCanBeSwept()

        if tableCanBeSwept:
            newGame.sweepTheTable(dealer)

        newGame.run(firstPlayer)

        noOfFaceUpCardsPerGame.append(newGame.noOfFaceUpCardsPerPlay) # this stores the number of face up cards per play
        noOfLegalActionsPerGame.append(newGame.noOfLegalActionsPerPlay) # this stores the number of legal actions per play

    print_stats(deals, noOfFaceUpCardsPerGame, noOfLegalActionsPerGame)

def testMiniMaxSearchOnTestFile(testfile):
    newGame = Game()
    F = open(testfile, "r")  # leave this file in the folder where you run the code from or modify the path accordingly
    correct = 0
    for line in F: # loading data from file
        finallist = []

        split = line.split("##")
        split[0] = ast.literal_eval(split[0])
        split[1] = ast.literal_eval(split[1])
        split[2] = ast.literal_eval(split[2])
        split[4] = ast.literal_eval(split[4])

        newGame.table = split[0]
        newGame.player.hand = split[1]
        newGame.computer.hand = split[2]

        if split[3] == 'player':
            firstPlayer = newGame.player
        else:
            firstPlayer = newGame.computer

        newGame.player.collected = []
        newGame.computer.collected = []
        newGame.computer_sweep = 0
        newGame.player_sweep = 0
        finallist = newGame.run(firstPlayer);

        if finallist == split[4]:
            correct += 1
        else:
            print("This test case failed: " + line)

    print("FinalScore: " + str(correct))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        testFile = "TestCases.txt"
        testMiniMaxSearchOnTestFile(testFile)

    else:
        noOfDeals = #### initialize the number of deals #####
        print("Computing the empirical average and standard deviation for " + str(noOfDeals) + " deals")
        EmpiricalValues(noOfDeals)




