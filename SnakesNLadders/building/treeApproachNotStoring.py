'''
I built this with a set ordering, which was a mistake. I need to think
about this as a tree, treat it as infinite. So lets have another go.

Created on 24 Dec 2015

@author: chris
'''
import copy
# Enter your code here. Read input from STDIN. Print output to STDOUT
    
class OutOfNodesError(Exception):
    pass

class EndNodeError(Exception):
    pass

class snakeOrLadderNode:
    def __init__(self, iInOutPair):
        self.iIn, self.iOut = map(int,iInOutPair.split())
        self.inOutRange = self.iOut - self.iIn 
        self.laterNodes = []
        self.bigNo = 100/6 + 2
        self.jthLaterNode = 0
        self.firstCall = True
    
    
    def __str__(self):
        return str(self.iIn) + " " + str(self.iOut)
    
    
    def __repr__(self):
        return str(self.iIn) + " " + str(self.iOut)
    
    
    
    def firstCallReset(self):
        self.jthLaterNode = 0
        self.firstCall = True
            
    
    def populateLaterNodes(self, nodes):
        
        # populate nodes

        for node in nodes:
            if node.iIn > self.iOut and node != self:
                self.laterNodes.append(node)
            if self.iOut == 100 and node.iIn == 100:
                self.laterNodes.append(node)
                
        # sort nodes
        
        def getKey(item):
            return item.iIn
        
        self.laterNodes = sorted(self.laterNodes, key=getKey)[::-1]
        
        
    def getNextDist(self, route, maxDist): 
        if self in route:
            return -self.bigNo, -1
        if maxDist < 0:
            return -maxDist, -1
        
        routeNew = copy.copy(route)
        routeNew.append(self)
        
        if self.firstCall:
            self.laterNodes[self.jthLaterNode].firstCallReset()
            self.firstCall = False
            
        err = -1
        while err == -1 and self.jthLaterNode < len(self.laterNodes):
            thisDist = iToMoves(self.laterNodes[self.jthLaterNode].iIn - self.iOut)
            dist, err = self.laterNodes[self.jthLaterNode].getNextDist(routeNew, maxDist - thisDist)
            dist += thisDist
#             if self.iIn == 79:
#                 print self.jthLaterNode, err
            
            if err == -1:
                self.jthLaterNode += 1
                while self.jthLaterNode < len(self.laterNodes) and self.laterNodes[self.jthLaterNode] in route:
                    self.jthLaterNode += 1
                if self.jthLaterNode < len(self.laterNodes):
                    self.laterNodes[self.jthLaterNode].firstCallReset()
                
        return dist, err
            
        
        
class endNode(snakeOrLadderNode):
    def __init__(self):
        self.iIn  = 100
        self.iOut = float('NaN')
        self.bigNo = 100/6 + 2
        self.jthLaterNode = 0
        self.firstCall = True
        
    def populateLaterNodes(self, nodes):
        pass
    
    def getNextDist(self, route, maxDist):
        if self.firstCall:
            self.firstCall = False
            return 0, 0
        else:
            return -self.bigNo, -1

    
        
class startNode(snakeOrLadderNode):
    def __init__(self):
        self.iIn  = float('NaN')
        self.iOut = 1
        self.laterNodes = []
        self.jthLaterNode = 0
        self.maxDist = 100/6 + 1
        self.firstCall = True
        
    def __iter__(self):
        return self
    
    def next(self):
        
        route = []
        dist, err = self.getNextDist(route, self.maxDist)
        if err == -1:
            raise StopIteration
        
        if dist < self.maxDist:
            self.maxDist = dist
        
        return dist
        
#             
#     
#     def getNextNode(self, prevNode):
#         
#         iMax = -1
#         nodeImax = None
#         for node in self.laterNodes:
#             if node.iIn 
        
      

def iToMoves(i):
    if i%6 == 0:
        return i/6
    else:
        return i/6 + 1
          
        
for _ in range(input()):
    
    start = startNode()
    end = endNode()
    
    nodes = []
    
    
    # Ladders
    
    for _ in range(input()):
        nodes.append(snakeOrLadderNode(raw_input()))
    
    
    # Snakes
    
    for _ in range(input()):
        nodes.append(snakeOrLadderNode(raw_input()))
    
    nodes.append(end)
    
    start.populateLaterNodes(nodes)

    for node in nodes:
        node.populateLaterNodes(nodes)
    
    dist = min([dist for dist in start])
    
    print dist
#         if i == 32:
#             break
# [nan 0, 93 37, 49 47, 67 17, 97 25, 32 62, 79 27, 42 68, 75 19, 95 13]
# [nan 0, 93 37, 49 47, 67 17, 97 25, 32 62, 75 19, 79 27, 42 68, 95 13]
