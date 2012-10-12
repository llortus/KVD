class State(object):
    def __init__(self):
        pass

    def enter(self):
        '''
        Called when state is entered, for initialization.
        '''
        pass

    def exit(self):
        '''
        Called when state is exited, for cleanup.
        '''
        pass

    def reason(self, *args, **kwargs):
        '''
        Return new State instance to perform transition.
        '''
        pass

    def act(self, *args, **kwargs):
        '''
        Per-frame state behavior.
        '''
        pass


class StateMachine(object):

    def __init__(self, host, first_state=None):
        self.host = host
        self.current_state = first_state

    def transition(self, new_state):
        '''
        Cause FSM to transition to passed State instance.
        '''
        self.current_state.exit()

        self.current_state = new_state

        # provide state references to host object and fsm instance
        self.current_state.host = self.host
        self.current_state.fsm = self

        self.current_state.enter()

    def update(self, *args, **kwargs):
        if self.current_state: # only update if we have a state
            new_state = self.current_state.reason(*args, **kwargs)

            if new_state: # if reason provides new state
                # do transition
                self.transition(new_state)
            else:
                # otherwise act with current state
                self.current_state.act(*args, **kwargs)