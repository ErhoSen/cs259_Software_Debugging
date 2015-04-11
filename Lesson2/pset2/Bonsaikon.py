#!/usr/bin/env python
# Simple Daikon-style invariant checker
# Andreas Zeller, May 2012
# Complete the provided code around lines 28 and 44
# Do not modify the __repr__ functions.
# Modify only the classes Range and Invariants,
# if you need additional functions, make sure
# they are inside the classes.

import sys
import math
import random

def square(x):
    return x * x

def square_root(x, eps = 0.00001):
    assert x >= 0
    y = math.sqrt(x)
    assert abs(square(y) - x) <= eps
    return y

print square_root(3)

# The Range class tracks the types and value ranges for a single variable.
class Range:
    def __init__(self):
        self.min  = None  # Minimum value seen
        self.max  = None  # Maximum value seen
    
    # Invoke this for every value
    def track(self, value):
        if self.min is None or value < self.min:
            self.min = value
        if self.max is None or value > self.max:
            self.max = value
            
    def __repr__(self):
        return repr(self.min) + ".." + repr(self.max)


# The Invariants class tracks all Ranges for all variables seen.
class Invariants:
    def __init__(self):
        # Mapping (Function Name) -> (Event type) -> (Variable Name)
        # e.g. self.vars["sqrt"]["call"]["x"] = Range()
        # holds the range for the argument x when calling sqrt(x)
        self.vars = {}
        
    def track(self, frame, event, arg):
        if event == "call" or event == "return":
            # YOUR CODE HERE. 
            # MAKE SURE TO TRACK ALL VARIABLES AND THEIR VALUES
            # If the event is "return", the return value
            # is kept in the 'arg' argument to this function.
            # Use it to keep track of variable "ret" (return)
            if event == "call":
                for var in frame.f_locals:
                    fun_name = frame.f_code.co_name
                    var_val = frame.f_locals[var]
                    if self.vars.get(fun_name, False):
                        if self.vars[fun_name].get(event, False):
                            if self.vars[fun_name][event].get(var, False):
                                self.vars[fun_name][event][var].track(var_val)
                            else:
                                self.vars[fun_name][event][var] = Range()
                                self.vars[fun_name][event][var].track(var_val)
                        else:
                            self.vars[fun_name][event] = {}
                            self.vars[fun_name][event][var] = Range()
                            self.vars[fun_name][event][var].track(var_val)
                    else:
                        self.vars[fun_name] = {}
                        self.vars[fun_name][event] = {}
                        self.vars[fun_name][event][var] = Range()
                        self.vars[fun_name][event][var].track(var_val)
            else:
                frame.f_locals["ret"] = arg
                for var in frame.f_locals:
                    fun_name = frame.f_code.co_name
                    var_val = frame.f_locals[var]
                    if self.vars.get(fun_name, False):
                        if self.vars[fun_name].get(event, False):
                            if self.vars[fun_name][event].get(var, False):
                                self.vars[fun_name][event][var].track(var_val)
                            else:
                                self.vars[fun_name][event][var] = Range()
                                self.vars[fun_name][event][var].track(var_val)
                        else:
                            self.vars[fun_name][event] = {}
                            self.vars[fun_name][event][var] = Range()
                            self.vars[fun_name][event][var].track(var_val)
                    else:
                        self.vars[fun_name] = {}
                        self.vars[fun_name][event] = {}
                        self.vars[fun_name][event][var] = Range()
                        self.vars[fun_name][event][var].track(var_val)

    def __repr__(self):
        # Return the tracked invariants
        s = ""
        for function, events in self.vars.iteritems():
            for event, vars in events.iteritems():
                s += event + " " + function + ":\n"
                # continue
                
                for var, range in vars.iteritems():
                    s += "    assert "
                    if range.min == range.max:
                        s += var + " == " + repr(range.min)
                    else:
                        s += repr(range.min) + " <= " + var + " <= " + repr(range.max)
                    s += "\n"
                
        return s

invariants = Invariants()
    
def traceit(frame, event, arg):
    invariants.track(frame, event, arg)
    return traceit

sys.settrace(traceit)
# Tester. Increase the range for more precise results when running locally
eps = 0.000001
for i in [3]:
    # r = int(random.random() * 1000) # An integer value between 0 and 999.99
    r = i
    try:
        z = square_root(r, eps)
    except:
        pass
    try:
        z = square(z)
    except:
        pass
sys.settrace(None)
print invariants
