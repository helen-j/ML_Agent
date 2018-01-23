"""
Created on Tue Jan 9th 2018
@author: Helen Jeffrey
Code@

"""

import timeit
import random
import AgentClass
import EnvironmentClass
import NeuralNet

#import neat-python

# =========================
# Parameters
# =========================

MAXACTIONS  = 1000
MAXTURNS    = 1000
GAMMA       = 0.9

agentList   = [1,2]

possibleRedActions = [ 1,2,3,4,5,6,7,8,9
#        "Scan the Network>",
#        "Scan the Computer>",
#        "Scan for open Ports>",
#        "Copy File to start folder>",
#        "Shutdown Computer>"
             ]

completedActions = []

qTable = [1,5,21,12,18,1,2,156,4,"asdf"]


# ---------------------------------------------------------------------

def main():
    # =========================
    # Settings
    # =========================

    start = timeit.timeit()

    # =========================
    # Set up environment, agent
    # =========================

    redAgent = AgentClass.Agent()
    computer = EnvironmentClass.Environment()

    # =========================
    # Train agent
    # =========================

    for x in range(MAXTURNS):

        for x in agentList:
            ''' 1. Check state '''

            ''' 2. Choose action '''
            a = random.choice(possibleRedActions)

            ''' 3. Perform Action '''
            completedActions.append([x, redAgent.chooseAction(x)])

            ''' 1. Check state '''

            ''' 4. Get Reward '''

    #        calculateQValues(red.qTable)


    end = timeit.timeit()
    print(end - start)


# =========================
if __name__== "__main__":
    main()