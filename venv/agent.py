'''
This is an Agent class
'''
class Agent:
    def __init__(self, hand, role):
        self.hand = hand  # dominos in the agent's hand
        self.collected = []  # the agent's collected dominos
        self.role = role  # the agent's role - "player" or "computer"
