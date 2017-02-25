#!/usr/bin/env python


class BaseAgent(object):

    """
    The base of all agents.
    """

    @property
    def parameters(self):
        """ Provides access to all learnable parameters of the agent. """
        return None

    def act(self, state):
        """ Returns an action to be taken. """
        raise NotImplementedError()

    def learn(self, state=None, action=None, reward=None, next_state=None, done=None):
        """ Given (s, a, r, s') tuples, does the necessary to compute the update. """
        pass

    def new_episode(self, terminated=False):
        """ Indicates to the agent that a new episode is about to start."""
        pass

    def done(self):
        """ Tells whether the agents needs to continue training. """
        return False

    def updatable(self):
        """ Returns whether the agent is ready to be updated. """
        return False

    def update(self, update):
        """ Applies the update to the parameters. """
        for p, u in zip(self.parameters(), update):
            p.data.add_(u)

    def get_update(self):
        """ Returns the parameter update from local experience."""
        return None

    def set_gradients(self, gradients):
        """ Sets gradients of the parameters. """
        for p, g in zip(self.parameters(), gradients):
            p.grad.data.set_(g)
