'''
Solvering hackerrank snakes and ladders graph theory problem with an recursive approach

This leads to infinite loops, which is clear it would, but shouldn't.
I didn't spot that when coming up with the solution

I built this with a set ordering, which was a mistake. I need to think
about this as a tree, treat it as infinite. So lets have another go.

Created on 24 Dec 2015

@author: chris

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
    
class OutOfNodesError(Exception):
    pass

class snakeOrLadderNode:
    def __init__(self, iInOutPair):
        self.iIn, self.iOut = map(int,iInOutPair.split())
        self.inOutRange = self.iOut - self.iIn 
        self.laterNodes = []
        self.dists = []
        self.distsNodes = []
        self.kDists = 0
    
    def __str__(self):
        return str(self.iIn) + " " + str(self.iOut)
#     
    def populateLaterNodes(self, nodes):
        
        if len(self.laterNodes) == 0:
            
            iMax = -1
            nodeIMax = None
            for node in nodes:
                if node.iIn > self.iOut:
                    self.laterNodes.append((node))
                if node.iIn > iMax:
                    iMax = node.iIn
                    nodeIMax = node
                    
            for node in self.laterNodes:
                node.populateLaterNodes(self.laterNodes)
                
            self.dists.append(iToMoves(iMax - self.iOut))
            self.prevFurthestNode = nodeIMax
            self.kDists += 1
            
    
    def getNextFurthestNode(self):
        
        iMax = -1
        nodeIMax = None
        for node in self.laterNodes:
            if node.iIn > iMax and node.iIn < self.prevFurthestNode.iIn:
                iMax = node.iIn
                nodeIMax = node
        if nodeIMax != None:
            return nodeIMax
        else:
            raise OutOfNodesError

    
    def getJthDist(self, j):
        try:
            return self.dists[j]#, self.distsNodes[j]
        except IndexError:
            try:
                squares = self.prevFurthestNode.getJthDist(self.kDists)
                
            except(OutOfNodesError):
                node = self.getNextFurthestNode()
                
                self.prevFurthestNode = node
                self.kDists = 0
                squares = self.prevFurthestNode.getJthDist(self.kDists)
                
                
            self.dists.append(squares + iToMoves(self.prevFurthestNode.iIn - self.iOut))
            self.kDists += 1
            
            return self.dists[j]

        
class endNode(snakeOrLadderNode):
    def __init__(self):
        self.iIn  = 100
        self.iOut = float('NaN')
        
    def populateLaterNodes(self, nodes):
        pass
    
    def getJthDist(self, j):
        raise OutOfNodesError
#     def next(self): # This is the end
#         return 0, True
    
        
class startNode(snakeOrLadderNode):
    def __init__(self):
        self.iIn  = float('NaN')
        self.iOut = 0
        self.laterNodes = []
        self.dists = []
        self.kDists = 0
        
        self.jCurrent = 0

        
    def __iter__(self):
        return self
    
    def next(self):
        try:
            dist = self.getJthDist(self.jCurrent)
            self.jCurrent += 1
            return dist
        except(OutOfNodesError):
            raise StopIteration
                
                

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
    
    distMin = 20
    for dist in start:
        if dist < distMin:
            distMin = dist
        print dist
    
