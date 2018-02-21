import ast
import itertools

def actions(table, hand):
    '''
    :param table - the cards on the table:
    :param hand - the cards on the player's hand:
    :return: list of all possible actions given the Game table and the player's hand
    '''
    finalList = []

    for hCard in hand:
        xMatches = []
        yMatches = []
        doubles =  []
        x, y = hCard # storing the pip counts on the current card in the hand

        for tCard in table: # for each card on the table
            if x in tCard:
                xMatches.append(tCard) # store the cards on the table that contain x
            elif y in tCard and not x == y: # avoid storing the same card twice
                yMatches.append(tCard) # store matches with y
            elif x == y and tCard[0] == tCard[1]:
                doubles.append(tCard) # storing the doubles only if hcard is a double

        finalXList = []
        finalYList = []
        finalDoublesList = []

        if len(doubles) > 0: # if there are doubles stored
            # generate all the combinations of doubles and store only those that have the sum % 5 = 0
            for L in range(1, len(doubles) + 1):
                for dCombination in itertools.combinations(doubles, L): # check each combination of doubles
                    sum = x
                    for currentDouble in list(dCombination):
                        sum += currentDouble[0]
                    if sum % 5 == 0:
                        # this is a legal action using doubles
                        finalDoublesList.append([hCard] + list(dCombination)) #

        if len(xMatches) > 0: # if there were cards on the table that matched x from hcard
            # generates all the combinations of cards that matched x
            for L in range(1, len(xMatches) + 1):
                for xCombination in itertools.combinations(xMatches, L):
                    sum = y
                    for curr in list(xCombination):
                        # print list(xCombination)
                        currX, currY = curr # the pip counts

                        if currX == x:
                            sum += currY
                        else:
                            sum += currX
                    if sum % 5 == 0:
                        # this is a legal action using matches with x on hcard
                        finalXList.append([hCard] + list(xCombination))

        if len(yMatches) > 0: # if there were cards on the table that matched y from hcard
            # generates all the combinations of cards that matched y
            for L in range(1, len(yMatches) + 1):
                for yCombination in itertools.combinations(yMatches, L):
                    sum = x
                    for curr in list(yCombination):
                        # print list(xCombination)
                        currX, currY = curr # the pip counts

                        if currX == y:
                            sum += currY
                        else:
                            sum += currX
                    if sum % 5 == 0:
                        # this is a legal action using matches with y on hcard
                        finalYList.append([hCard] + list(yCombination))

        # store all the possible legal actions using hCard
        finalList = finalList + finalXList + finalYList + finalDoublesList
        finalList.append([hCard])
    
    print(finalList)

    return finalList

def sortLists(listOfLegalAction):
    finallist = []
    for legalAction in listOfLegalAction:
        temp = []
        for domino in legalAction:
            temp = temp + [sorted(domino)]
        finallist = finallist + [sorted([tuple(x) for x in temp])]

    return sorted(finallist)


def testLegalActionGeneration(table, hand, testcase):
    legalActions = actions(table,hand) # generating all the legal actions given the table and the hand
    legalActions = sortLists(legalActions) # sorting the list of legal actions
    testcase = sortLists(testcase) # sorting the list of legal actions in the test case

    if legalActions == testcase:
        return True

    return False


if __name__ == "__main__":
    F = open("TestCases_legalActions.txt","r")# leave this file in the folder where you run the code from or modify the path accordingly
    correct =0
    for line in F:
        split = line.split("##")
        split[0] = ast.literal_eval(split[0])
        split[1] = ast.literal_eval(split[1])
        split[2] = ast.literal_eval(split[2])
        if testLegalActionGeneration(split[0],split[1],split[2]):
            correct += 1
        else:
            print("This test case failed: "+ line)

    print("FinalScore: "+ str(correct))
