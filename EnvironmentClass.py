"""
Created on Tue Jan 9th 2018
@author: Helen Jeffrey
Code@

"""


class Environment:


    def __init__(self):

        # Properties of the environment
        self.currentStateVector = []
        self.previousStateVector = []

    def state_transition(self):

        raise NotImplementedError

    def update_state(self, newAction):

        raise NotImplementedError

    def acheived_goal(self):

        raise NotImplementedError

    def state_action_dim(self):

        raise NotImplementedError



# ---------------------------------------------------------------------