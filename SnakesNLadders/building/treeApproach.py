'''
I built this with a set ordering, which was a mistake. I need to think
about this as a tree, treat it as infinite. So lets have another go.

Created on 24 Dec 2015

@author: chris
'''

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
        self.jCalls = 0
#         self.minDist = 100/6 + 2 # largest is 100/6 + 1 (99/6 + 1?)
        
    
    def __str__(self):
        return str(self.iIn) + " " + str(self.iOut)
#     
    def populateLaterNodes(self, nodes):
        
        if len(self.laterNodes) == 0:
            
            iMax = -1
            nodeIMax = None
            for node in nodes:
                if node.iIn > self.iOut:
                    self.laterNodes.append(node)
                if node.iIn > iMax:
                    iMax = node.iIn
                    nodeIMax = node
                if self.iOut == 100 and node.iIn == 100:
                    iMax = node.iIn
                    nodeIMax
                    
            for node in self.laterNodes:
                node.populateLaterNodes(nodes)
                
            self.prevFurthestNode = nodeIMax
            self.distToPrev = iToMoves(self.prevFurthestNode.iIn - self.iOut)
            
    
    def getNextFurthestNode(self, maxDist):
        
        iMax = -1
        nodeIMax = None
        for node in self.laterNodes:
            if node.iIn > iMax \
                    and iToMoves(node.iIn - self.iOut) < maxDist \
                    and iToMoves(node.iIn - self.iOut) < self.distToPrev:
                iMax = node.iIn
                nodeIMax = node
        if nodeIMax != None:
            self.prevFurthestNode = nodeIMax
            self.distToPrev = iToMoves(self.prevFurthestNode.iIn - self.iOut)
            return False
        else:
            return True
    
    def getNextDist(self, maxDist):
        if maxDist < 1:
            return 100/6 + 3, True
        
        shiftExt = False
        if self.jCalls == 0:            
            dist = iToMoves(self.prevFurthestNode.iIn - self.iOut)
            self.jCalls += 1

        else:
            
            dist, shiftInt = self.prevFurthestNode.getNextDist(maxDist 
                                                            - self.distToPrev)
            while shiftInt and not shiftExt:
                shiftExt = self.getNextFurthestNode(maxDist)
                newDist, shiftInt = self.prevFurthestNode.getNextDist(maxDist
                                                                   - self.distToPrev)
                print self.iIn, self.prevFurthestNode.iIn
                dist = newDist + self.distToPrev
        
        if dist > maxDist:
            shiftExt = True
          
        return dist, shiftExt
        
        
class endNode(snakeOrLadderNode):
    def __init__(self):
        self.iIn  = 100
        self.iOut = float('NaN')
        
    def populateLaterNodes(self, nodes):
        pass
    
    def getNextDist(self, maxDistIn):
        return -100/6 - 3, True
    
#     def getJthDist(self, j):
#         raise OutOfNodesError
    
        
class startNode(snakeOrLadderNode):
    def __init__(self):
        self.iIn  = float('NaN')
        self.iOut = 0
        self.laterNodes = []
        self.jCalls = 0
        self.maxDist = 100/6 + 2
        
    def __iter__(self):
        return self
    
    def next(self):
        
        finish = False
        if self.jCalls == 0:            
            self.maxDist = iToMoves(self.prevFurthestNode.iIn - self.iOut)
            self.jCalls += 1
            dist = self.maxDist
        else:
            dist, shift = self.prevFurthestNode.getNextDist(self.maxDist 
                                                            - self.distToPrev)
            while shift and not finish:
                finish = self.getNextFurthestNode(self.maxDist)
                newDist, shift = self.prevFurthestNode.getNextDist(self.maxDist
                                                                   - self.distToPrev)
                print 0, self.prevFurthestNode.iIn
                dist = newDist + self.distToPrev
                
            if dist < self.maxDist:
                self.maxDist = dist
        
        if finish:
            raise StopIteration
        
        return dist
        
#         try:
#             dist = self.getJthDist(self.jCurrent)
#             self.jCurrent += 1
#             return dist
#         except(OutOfNodesError):
#             raise StopIteration
                
                

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
    
    for dist in start:
        print dist
        pass
    print dist
    print