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















    # Deep Q-Learning Algorithm
    #
    # Initialise replayActions (D)
    # Initialise action-value table Q with random weights
    #
    # observe initial state (s)
    #
    # repeat
    #   select an action (a)
    #       with a probability of G? select a random action (a)
    #       OR select
    #   do action (a)
    #   observe reward (r)
    #   observe new state (s')
    #   store <s, a, r, s'> in replayActions (D)
    #
    #   sample random transitions <ss, aa, rr, ss'> from replayActions (D)
    #   calculate target for each minibatch transition (tt)
    #       if ss' is terminal state then tt = rr
    #       otherwise tt = rr + ymax a' Q(ss', aa,)
    #   train the Q network using (tt - Q(ss, aa)) as loss
    #
    #   s=s'
    #
    # until terminated

#state numbers reflect computer e.g., first might be firewall active?
initialState = [1,0,1,1]
finalState = [0,1,0,0]

1000




[0,1,1,0]
900



[0,1,1,1]
810




state=[]
Qtable=#array of zeros
solved = False

def updateState(action):
    #change state vector
    #based on action
    if state[action] ==1:
        state[action]==0
    else:
        state[action]==1

def checkSolved():
    if (state == finalState):
        solved=True
        return 1000
    else
        return 0

def initializeState():
    state=initialState
    solved=False

def explore(agent):
    initializeState()


    counter=0
    while (not solved):
        currentAction = agent.randomAction()
        updateState(currentAction)
        checkSolved()

        counter=counter+1

        #agent.reward = (calculateQ())


        ####Q learning formula Q(s,a) = Rimm + GAMMA*Q(s,a)-1


def exploit(agent):
    initializeState()

    counter = 0
    while (not solved):
        currentAction = agent.bestAction(qtable)
        updateState(currentAction)
        immreward = checkSolved()
        agent.reward = (calculateQ(immreward))

        counter = counter + 1
    pass

#main
numtrials=100
agent a()
for i in numtrials:
    if i%2==0:
        explore(agent)
    else:
        exploit(agent)







