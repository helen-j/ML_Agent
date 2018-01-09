#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:30:03 2018

@author: jef077
"""

''' ------------------------------------------------------------- ''' 
''' Parameters '''
MAXACTIONS    = 10
GAMMA       = 0.9


''' ------------------------------------------------------------- ''' 

class Agent:

    def __init__(self):
        '''Properties of the agent'''
        self.currentState = []
        self.currentAction = 0
        self.currentReward = 0
        self.qTable = {}            
        self.gamma = GAMMA
        self.agentStatus = 0
        self.agentGoal = []
        self.nextState = []
        self.actionsTaken = []
        self.turn = 0
        self.observeState()
        self.chooseAction()
        self.resetAgent()
        self.updateQValues()
        

    def observeState(self):
        raise NotImplementedError
        
        
    def chooseAction(self):
        self.actionsTaken.append(11)
        print(self.actionsTaken)
        

    def resetAgent(self):
        raise NotImplementedError
        
        
    def updateQValues(self):
        calculateQValues(self.qTable)

''' ------------------------------------------------------------- ''' 