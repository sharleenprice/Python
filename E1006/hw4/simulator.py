"""
Created by Sharleen Price spp2122
"""

import random
import math
from matplotlib import pyplot as plt

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    
recovery_time = 4 # recovery time in time-steps
virality = 0.2    # probability that a neighbor cell is infected in 
                  # each time step                                                  

class Cell(object):
    
    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
        self.counter = 0                 # "I" (infected)
        
    def infect(self):
        # sets state to I
        self.state = "I"
        
        
    def process (self, adjacent_cells):
        mean = 3
        sd = 1
        num_death = random.random()
        
        if self.counter == recovery_time:
                self.state = "S"
                self.counter = 0
                
        if self.state == "I":
            prob_death = pdeath(self.counter, mean, sd)
            if num_death< prob_death:
                self.state = "R"
    
        if self.state == "I":
            self.counter += 1
            for i in range(len(adjacent_cells)):
                if adjacent_cells[i].state == "S":
                    rand_int = random.random()
                    if rand_int <= virality:
                        adjacent_cells[i].infect()
                        
class Map(object):
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell):
        self.cells[(cell.x,cell.y)]=cell
             
    def display(self):
        image = []
        for column in range(self.height+1):
            line =[]
            for row in range(self.width+1):
                if (column,row) in self.cells:
                    if self.cells[(column,row)].state == "S": #green
                        tup = (0.0,1.0, 0.0)
                    elif self.cells[(column,row)].state == "R": #gray
                        tup = (0.5,0.5, 0.5)
                    elif self.cells[(column,row)].state == "I": #red
                        tup = (1.0,0.0, 0.0)
                else:
                    tup = (0.0,0.0, 0.0)
                line.append(tup)
            image.append(line)
        
        plt.imshow(image)
        
    
    def adjacent_cells(self, x,y):
        adj_list = []
        # return cells  adjacent not infected
        # check up down left right
        # check if in map
        # check if in  cells dictionary

        if x-1 >=0:
            if (x-1,y) in self.cells:
                adj_list.append(self.cells[(x-1,y)])
        if x+1 <=self.width:
            if (x+1,y) in self.cells:
                adj_list.append(self.cells[(x+1,y)])
        if y-1 >=0:
            if (x,y-1) in self.cells:
                adj_list.append(self.cells[(x,y-1)])
        if y+1 <=self.height:
            if (x,y+1) in self.cells:
                adj_list.append(self.cells[(x,y+1)])
            
        return adj_list
    
    def time_step(self):
        for column in range(self.height+1):
            for row in range(self.width+1):
                if (column,row) in self.cells:
                    adj = self.adjacent_cells(column,row)
                    self.cells[column,row].process(adj)
                    
        self.display()
          
def read_map(filename):
    m = Map()
    f = open(filename, "r")
    for line in f:
        cord_list = line.strip().split(",")
        cell = Cell(int(cord_list[0]), int(cord_list[1]))
        m.add_cell(cell)
    # ... Write this function
    return m
