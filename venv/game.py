'''
This is a Game class
'''
from random import shuffle
from agent import Agent
import random
import minimax

def count_fives(list):
    '''
    Counts no. of 5 dominoes in the list
    '''
    count = 0
    for domino in list:
        if 5 in domino:
            count += 1

    return count

def is_pair_match(t1, t2):
    '''
    checks if t1 and t2 has one value in common and the sum of other digits is multiple of 5
    '''
    x, y = t1 # integers on domino t1
    Flag = False

    if x not in t2 and y not in t2: # if the integers on t1 do not appear in t2 => there is no match
        return False
    else:
        if x in t2: # if x appears on t2
            if t2[0] == x:
                elem = t2[1] # elem = the other integer on domino t2 besides x
            else:
                elem = t2[0]

            if (elem + y) % 5 == 0: # checks the sum of e and y
                Flag = True
            else:
                Flag = False
        else: # if y appears on t2
            if t2[0] == y:
                elem = t2[1] # elem = the other integer on domino t2 besides x
            else:
                elem = t2[0]

            if (elem + x) % 5 == 0: # checks the sum of e and x
                Flag = True
            else:
                Flag = False

    return Flag

def checkIfAllDominoesCanBeCollected(dominoes):
    '''
        checks if all the dominoes can be collected
        all dominos have one value in common and sum of others is multiple of 5
    '''
    x, y = dominoes[0]

    sumXMatches, sumYMatches = y, x # sum1 is for x matches => so we initialize with y;
    xMatches, yMatches = 1, 1 # number of dominoes that matched x or y

    for i in range(1, len(dominoes)): # for each domino on the table except the first one
        currDomino = dominoes[i]
        if x in currDomino: # if the current domino contains integer x
            xMatches += 1 # we found a match with x

            if currDomino[0] == x:
                elem = currDomino[1] # elem = the other integer on the current domino besides x
            else:
                elem = currDomino[0]

            sumXMatches = sumXMatches + elem # sum up elem

        if not x == y and y in currDomino:
            yMatches += 1 # we found a match with y

            if currDomino[0] == y:
                elem = currDomino[1] # elem = the other integer on the current domino besides y
            else:
                elem = currDomino[0]

            sumYMatches = sumYMatches + elem # update the sum

        if x == y and currDomino[0] == currDomino[1]: # if the first domino is a double and the current domino is a double - doubles are considered matches
            xMatches += 1 # mark a match with x
            yMatches += 1 # mark a match with y
            sumXMatches = sumXMatches + currDomino[0] # update the sum
            sumYMatches = sumYMatches + currDomino[0] # update the sum


    if xMatches == len(dominoes) and sumXMatches % 5 == 0: # if all the dominoes are matched using x and the sum respects the rule
        return True # all the dominos are matches

    elif yMatches == len(dominoes) and sumYMatches % 5 == 0: # if all the dominoes are matched using y and the sum respects the rule
        return True

    else:
        return False

def checkTwoPairs(table):
    '''
     checks if table can be swept before the game starts - if there are 2 pairs of dominoes that match
    '''

    pairs_list = [] # the list of dominoes that match the first domino on the table
    no_pair_list = [] # the list of dominoes that do not match the first domino on the table

    firstDomino = table[0]
    for j in range(1, len(table)): #for each doino on the table, except the first one
        currDomino = table[j]

        if is_pair_match(firstDomino, currDomino): #if we find a match with the first domino on the table
            pairs_list.append(currDomino) # add the current domino in the pair list
        else:
            no_pair_list.append(currDomino)

    if len(pairs_list) == 0: # if no domino can be matched with the first domino on the table
        return False # the table cannot be swept

    elif len(pairs_list) == 1: # if only 1 domino matched the first domino on the table
        return is_pair_match(no_pair_list[0], no_pair_list[1]) # check the match between the remaining 2 dominoes that were not paired

    elif len(pairs_list) == 3: # all dominoes were paired with the first domino
        if is_pair_match(pairs_list[0], pairs_list[2]) or is_pair_match(pairs_list[0], pairs_list[1]) or is_pair_match(pairs_list[1], pairs_list[2]):
            return True
        else:
            return False

    else: # we have 2 pairs with the first domino and 1 card unpaired
        if is_pair_match(no_pair_list[0], pairs_list[0]): # check if the unpaired card can be matched with 1 paired card
            return True
        elif is_pair_match(no_pair_list[0], pairs_list[1]):
            return True
        else:
            return False

class Game:

    def __init__(self):
        self.noOfLegalActionsPerPlay = []
        self.noOfFaceUpCardsPerPlay = []
        hand = []

        for i in range(0, 7): # generating the whole set of dominoes, represented as - (0,0), (0,1), ..., (6,6)
            for j in range(i,7):
                hand.append((i, j))

        shuffle(hand) # shuffling the whole set of dominoes
        self.table = hand[:4]  # initializing table dominoes - there are 4 pieces of domino on the table at the beginning
        self.player = Agent(hand[4:7], 'player')  # player dominoes - getting 3 pieces
        self.computer = Agent(hand[7:10], 'computer')  # computer dominoes - getting 3 pieces
        self.player_sweep = 0  # no. of player sweeps
        self.computer_sweep = 0  # no. of computer sweeps
        self.picked_last = ""  # one who picks last i.e., Agent.role("computer" or "player")

    def firstPlayer(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return self.computer
        else:
            return self.player


    def get_enemy(self, agent):
        '''
        if agent.role == "player":
            return self.computer
        else:
            return self.player
        '''
        :param agent:
        :return: opponent of the agent


    def isGameOver(self):
        '''
        check if this a terminal state
        :return: true/false
        '''
        if len(self.computer.hand) == 0 and len(self.player.hand) == 0:
            return True

        return False

    def print_board(self, agent):
        '''
        Prints out the game state
        '''
        opponent = self.get_enemy(agent)
        print("After " + str(agent.role) + "'s action ---------- ")
        print("Table: " + str(self.table))
        print("Computer_sweeps: " + str(self.computer_sweep) + " and  Player_sweeps: " + str(self.player_sweep))
        print(str(agent.role) + "'s hand: " + str(agent.hand))
        print("Cards " + str(agent.role) + " collected: " + str(agent.collected))
        print(str(opponent.role) + "'s hand: " + str(opponent.hand))
        print("Cards " + str(opponent.role) + " collected: " + str(opponent.collected) + "\n\n")

    def makeMove(self, card, tableCardsToCollect, agent):
        '''
        checks if the action is valid
        if action is Discard - remove card from agent hand and add it to the game table
        if action is Take - remove card from agent hand and add to_collect to the agent collected.
        and check if there is a sweep and increment sweep to the agent.
        :param card:
        :param tableCardsToCollect:
        :param agent:
        :return:
        '''

        if len(tableCardsToCollect) == 0:  # if there is no card on the table that matches the card in the agent's hand (card)
            self.table.append(card)  # the player puts the card on the table
            if agent.role == 'player':
                self.player.hand.remove(card)
            else:
                self.computer.hand.remove(card)
        else:  # if there are cards on the table that can be collected by the agent using card
            if agent.role == 'player':
                self.player.collected.extend([card] + tableCardsToCollect)  # puts the card with the others from the table in the collected stack
                self.player.hand.remove(card)  # removes the card from hand and put it in the collected stack
            else:
                self.computer.collected.extend([card] + tableCardsToCollect)
                self.computer.hand.remove(card)

            for tableC in tableCardsToCollect:
                self.table.remove(tableC)  # removes the collected cards from the table
            if len(self.table) == 0:  # if the table remains empty, it is a sweep
                if agent.role == 'player':
                    self.player_sweep += 1
                else:
                    self.computer_sweep += 1

    def computeScore(self, agent):
        '''
        computes the utility of a state
        :param agent:
        :return: an integer score.
        '''
        play_score = 0
        comp_score = 0

        if not len(self.table) == 0:  # if there are cards left on the table
            if self.picked_last == 'player':  # the last player who collected cards from the table gets the remaining cards
                self.player.collected += self.table
            else:
                self.computer.collected += self.table
            self.table = []

        if len(self.player.collected) > len(self.computer.collected): # the player who collected more cards receives an extra point
            play_score += 1
        elif len(self.player.collected) < len(self.computer.collected):
            comp_score += 1

        play_score += count_fives(self.player.collected) + self.player_sweep
        comp_score += count_fives(self.computer.collected) + self.computer_sweep

        if agent.role == 'player':
            print("\n\n\n")
            return play_score - comp_score
        else:
            print("\n\n\n")
            return comp_score - play_score


    def checkIfInitialTableCanBeSwept(self):

        if checkTwoPairs(self.table) or checkIfAllDominoesCanBeCollected(self.table):
            return True

        return False

    def sweepTheTable(self, dealer):
        if dealer.role == 'player': # mark a sweep for the dealer
            self.player_sweep += 1
        else:
            self.computer_sweep += 1

        dealer.collected.extend(self.table) # the dealer collects all the dominoes on the table
        self.table = [] # the table remains empty

    def run(self, agent):
        '''
        This function specifies the framework for the play -
        changing turns and continuing the game with provided search.
        '''
        self.noOfLegalActionsPerPlay=[]
        self.noOfFaceUpCardsPerPlay=[]

        sequence_of_actions = [] # initializing the sequence of actions
        opponent = self.get_enemy(agent) # getting the opponent

        print("*********************************\nInitial Table: " + str(self.table)) # shows the dominoes on the initial table
        print(str(agent.role) + " is playing first")
        print(str(agent.role) + "'s hand: " + str(agent.hand)) # shows the initial dominoes in the current player's hand
        print("Dominos " + str(agent.role) + " collected: " + str(agent.collected)) # shows the cards collected by the current player
        print(str(opponent.role) + "'s hand: " + str(opponent.hand)) # the dominoes on the opponent's hand
        print("Dominos " + str(opponent.role) + " collected: " + str(opponent.collected)) # shows the cards collected by the opponent

        print("*********************************\n\n")

        while not self.isGameOver():
            best_action = minimax.minimax(self, agent) # identifying the best action according to the search algorithm
            print("main_action1: " + str(best_action))

            if len(best_action) > 1: # picked_last = the last player who performed an action
                self.picked_last = agent.role

            self.makeMove(best_action[0], best_action[1:], agent) # the agent performs the best option
            self.noOfFaceUpCardsPerPlay.append(len(self.table))
            self.print_board(agent) # prints the board after the move
            sequence_of_actions.append(best_action)

            # if the game is not over => switch to the other player
            if not self.isGameOver():
                best_action = minimax.minimax(self, opponent) # identifying the best action according to the search algorithm
                print("main_action2: " + str(best_action))

                if len(best_action) > 1:
                    self.picked_last = agent.role

                self.makeMove(best_action[0], best_action[1:], opponent)
                self.noOfFaceUpCardsPerPlay.append(len(self.table))
                self.print_board(opponent)
                sequence_of_actions.append(best_action)
            else:
                break

            #print("Number of times legal actions generation was executed=%d" % globals.countLegalActionsGenerationExecution)

        print("Score of the Max at the end:" + str(self.computeScore(agent)))
        print("sequence of actions played:" + str(sequence_of_actions))
        return sequence_of_actions


