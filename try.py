

import numpy as np
import timeit
import random
import AgentClass
import EnvironmentClass
#import NeuralNet

#import neat-python

# =========================
# Parameters
# =========================

#MAXACTIONS  = 100
#MAXTURNS    = 100
#GAMMA       = 0.9

# agentList   = [1,2]

# possibleRedActions = [ 1,2,3,4,5,6,7,8,9
#        "Scan the Network>",
#        "Scan the Computer>",
#        "Scan for open Ports>",
#        "Copy File to start folder>",
#        "Shutdown Computer>"
#             ]

numstates   = 16
numactions  = 8
numtrials   = 100
initialState = [1,0,1,1]
finalState = [0,1,0,0]
completedActions = []
state = []
qtable = []
solved = False

#Initialize Q-Table with all zeros
qtable = np.zeros((numstates, numactions))  # array of zeros
print(qtable)
