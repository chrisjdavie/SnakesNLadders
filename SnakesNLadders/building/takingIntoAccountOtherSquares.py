'''
Solving: https://www.hackerrank.com/challenges/the-quickest-way-up

Previous attempts don't include that you have to take a ladder or snake
if you land on it. 

Created on 27 Dec 2015

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
        
        dist = -1
        err = -1
        while err == -1 and self.jthLaterNode < len(self.laterNodes):
            thisDist, err = iToMoves(self.laterNodes[self.jthLaterNode].iIn, self.iOut, self.laterNodes[self.jthLaterNode+1:],self)
            
            if err == 0:
                dist, err = self.laterNodes[self.jthLaterNode].getNextDist(routeNew, maxDist - thisDist)
                dist += thisDist
                
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
        self.iIn  = float('Nan')
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
        
      

def iToMoves(iDest, iStart, nodesBetweenIn, callingNode):
    
    if (iDest == iStart and iStart == 100):
        return 0, 0
    
    err = 0
    
    if ( callingNode.iIn < iDest and callingNode.iIn > iStart):
        
        nodesBetween = copy.copy(nodesBetweenIn)[::-1]
        nodesBetween.append(callingNode)
        
        def getKey(item):
            return item.iIn
        nodesBetween = sorted(nodesBetween, key = getKey)        
        
    else:
        nodesBetween = copy.copy(nodesBetweenIn)[::-1]
        
    iDiff = 0
    iCheckLast = iStart
    
    for j, node in enumerate(nodesBetween):
        
        if (node.iIn - iCheckLast)%6:
            pass
        elif ( j == 0 ):
            iDiff += node.iIn - iCheckLast
            iDiff += 1
            iCheckLast = node.iIn - 1
        else:
            nodesBack = nodesBetween[:j][::-1]
            jBack = 0
            for jBack, nodeBack in enumerate(nodesBack[:5]):
                if (node.iIn - nodeBack.iIn) != 1 + jBack  \
                        or (nodeBack.iIn - iCheckLast)%6 != 5-jBack:
                    break
            else:
                err = -1
             
            iDiff += node.iIn - iCheckLast
            if iDiff < 1:
                err = -1
               
            iCheckLast = node.iIn - ( 1 + jBack)
    
    i = iDiff + (iDest - iCheckLast) 
    
    if i%6 == 0:
        return i/6, err
    else:
        return i/6 + 1, err
          
        
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
    
    dists = [dist for dist in start]
    if len(dists) > 0:
        dist = min(dists)
        print dist
    else:
        print -1