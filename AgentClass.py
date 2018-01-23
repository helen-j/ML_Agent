"""
Created on Tue Jan 9th 2018
@author: Helen Jeffrey
Code@

"""
import random
import numpy as np
# =========================
# Parameters
# =========================

MAXACTIONS = 10
GAMMA = 0.9

POSSIBLE_ACTIONS = [ 1,2,3,4 ]
#        "Scan the Network",
#        "Scan the Computer",
#        "Scan for open Ports",
#        "Copy File to start folder"
#        ]

# ---------------------------------------------------------------------
class Agent:
    # =========================
    # Initialise agent
    # =========================

    def __init__(self, agent_info):
        self.name = agent_info["name"]
        self.epsilon = agent_info["epsilon"]  # exploration probability

        # Properties of the agent
        self.currentState = []
        self.currentAction = 0
        self.currentReward = 0


    def chooseAction(self, currentState):
        # Method to select the next action based on the currentState

        self.actionsTaken.append(11)
        print(self.actionsTaken)

        #    print(currentState)
        if (currentState == 1):
            print("  RED --> ", currentState)

        elif (currentState == 2):
            print("BLUE  --> ", currentState)

        # return actionToTake
        return random.choice(POSSIBLE_ACTIONS)


    def __init__(self, agent_info):
        self.name = agent_info["name"]
        self.epsilon = agent_info["epsilon"]  # exploration probability

    def get_action(self, state, brain, env):
        # Explore actions
        def explore_actions_allowed(state, env):
            actions_explore_allowed = env.allowed_actions(state)
            return actions_explore_allowed
        # Choose highest value action
        def argmax_Q_actions_allowed(Q, state, env):
            actions_allowed = env.allowed_actions(state)
            Q_s = Q[state[0], state[1], actions_allowed]
            actions_Qmax_allowed = actions_allowed[np.flatnonzero(Q_s == np.max(Q_s))]
            return actions_Qmax_allowed

        # Perform epsilon-greedy selection
        if random.uniform(0, 1) < self.epsilon:
            actions_explore_allowed = explore_actions_allowed(state, env)
            return np.random.choice(actions_explore_allowed)
        else:
            actions_Qmax_allowed = argmax_Q_actions_allowed(brain.Q, state, env)
            return np.random.choice(actions_Qmax_allowed)


    def resetAgent(self):
        # This method resets the state / actions to the default state.
        # That is:  <00000000>
        currentState = '00000000'
        return currentState


    def getRewards(self):
        # This method calculated the reward for a given action
        return 0


    def neuralNetworkMagic(self):
        # This method calculated the reward for a given action
        # Returns the highest activation value from the NN
        return 0


# ---------------------------------------------------------------------