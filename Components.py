import numpy as np 
import matplotlib.pylab as plt

class Component(object):
    def __init__(self):
        self.diagram = ""
    def __repr__(self):
        return self.diagram
    def step(self):
        pass

class Power(Component):
    def __init__(self):
        self.diagram = "|||"
    def step(self, c_in):
        return 1


class Wire(Component):
    def __init__(self):
        self.diagram = "--->"
    def step(self, c_in):
        return c_in

class Resistor(Component):
    def __init__(self, R):
        self.R = R
        self.diagram = "-R->"
    def step(self, c_in):
        return c_in / self.R

class Switch(Component):
    def __init__(self, state0 = 0):
        assert state0 == 0 or state0 == 1
        self.state = state0
        if state0 == 0:
            self.close()
        else:
            self.open()
    def close(self):
        self.state = 1
        self.diagram = "-S->"
    def open(self):
        self.state = 0
        self.diagram = "-/->"
    def step(self, c_in):
        if self.state == 1:
            return c_in
        else:
            return 0

class Split(Component):
    def __init__(self):
        self.diagram = "---<"
    def step(self, c_in):
        return c_in, c_in

class Diode(Component):
    def __init__(self):
        self.state = 0
        self.diagram = "-|D-"
    def step(self, c_in):
        if c_in > 0:
            self.state = 1
            self.diagram = "->D<-"
        else:
            self.state = 0
            self.diagram = "-|D-"
        return c_in

class Ground(Component):
    def __init__(self):
        pass
    def __repr__(self):
        return "|/|"
    def step(self, c_in):
        return 0


class Circuit_series(object):
    def __init__(self, complist):
        self.comps = complist
    def step(self):
        current = 0
        for c in self.comps:
            current = c.step(current)
            print(c)
        print(current)


if __name__ == '__main__':
    w = Wire()
    r = Resistor(15)
    s = Switch(0)
    sp = Split()
    p = Power()
    g = Ground()
    d = Diode()

    lc = [p,w,r,d,w,r,w,s,d,w,g]
    circuit = Circuit_series(lc)
    i = 0
    while i < 10:
        circuit.step()
        i+=1
