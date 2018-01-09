import os
import numpy as np
import random
import timeit
from agent import Agent
from matplotlib import pyplot as plt
import numpy as np

''' Parameters '''
MAXACTIONS  = 10
MAXTURNS    = 10
GAMMA       = 0.9

agentList = [1,2]

possibleRedActions = [ 1,2,3,4,5,6,7,8,9
#        "Scan the Network>",
#        "Scan the Computer>",
#        "Scan for open Ports>",
#        "Copy File to start folder>",
#        "Shutdown Computer>"
        ]

completedActions = []
qTable = [1,5,21,12,18,1,2,156,4,"scsazfsdgscfa"]

''' ------------------------------------------------------------- ''' 
def calculateQValues(qTable):
    
    print(qTable)
    


''' ------------------------------------------------------------- ''' 
def chooseAction(a, agent):
#    print(a, agent)
    if(agent==1):
        print("  RED --> ", a, agent)
    elif(agent==2):
        print("BLUE  --> ", a, agent)
    return a


''' ------------------------------------------------------------- ''' 



''' ------------------------------------------------------------- ''' 

def plotActions():
    fig_actions = plt.figure()
    plt_actions = fig_actions.add_subplot(111)
    counts, bins, patches = plt_actions.hist(
            completedActions, bins = 100, normed = False, color = 'g',linewidth=0)
#plt.gca().set_xlim(completedActions.min(), completedActions.max())
    plt.show()   


''' ------------------------------------------------------------- ''' 
start = timeit.timeit()

for x in range(MAXTURNS):
    
    
    for x in agentList:
        ''' 1. Check state '''
        
        
        
        ''' 2. Choose action '''
        a = random.choice(possibleRedActions)
        
        ''' 3. Perform Action '''
        completedActions.append([x,chooseAction(a,x)])
        
        ''' 1. Check state '''
        
        
        
        ''' 4. Get Reward '''
        
#        calculateQValues(red.qTable)
        
        

end = timeit.timeit()
print(end - start)
print( "all done at %.2f seconds" % end - start )
    
print(completedActions)
#plotActions()
 
        
red = Agent
#red.gamma
#print("1. ", red.gamma)



    