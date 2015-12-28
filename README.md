# SnakesNLadders

Solving the hackerrank snakes and ladders puzzle

https://www.hackerrank.com/challenges/the-quickest-way-up

This isn't a particularly efficient solution. I solve the problem, and then look at how other people solved it better.

It finding the shortest distance between a start and end point. It is a 1D problem, there is a direct distance, and then nodes
can instantly transporting from one point to another. There are discrete distances, and a maximum range of movement possible
each turn. The goal is to reach the end point in the fewest possible turns.

It is a graph theory problem, my approach was something of a bounds-limited, depth first approach - I found the first 
solution, the direct distance between the start and end, used that as a limit. I then proceeded with a depth-first approach,
from furthest to nearest from the start node.

There were cycles that needed to be detected, and cases where there were no solutions.


## Execution

python takingIntoAccountOtherSquares.py < input4.txt


## Better approachs

Breadth-first would have used less code at least, and been more straight forwards. First calculate the distances between all
nodes, and then sequentially explore the shortest routes, stopping when the end is reached. Cycle-detection would have to
have been incorporated - some problems do not have solutions, but can have infinite loops.

This isn't the most efficient approach of all, in terms of fewest lines of code. That was for each discrete point, calculate
all possible distances from the next reachable points. In around 30 lines of quite clear code, the answer could be found.
I was looking at this to get my head round graph theory, though, and that was a separate approach.
