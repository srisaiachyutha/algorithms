#TODO

class FloydWarshall(object):
    POSITIVE_INFINITY = float('inf')
    NEGATIVE_INFINITY =  float('-inf')
    REACHES_NEGATIVE_INFINITY = -1
    def __init__(self,no_of_nodes):
        # solved is used to check whether the algorithm is runned or not
        self.num = no_of_nodes
        self.solved = False
        self.solvenegative = False
        self.negativecycleexists  = False
        self.matrix = []
        self.dp = []
        self.next = [[0 for i in range(self.num)] for j in range(self.num)]
    def initialize(self,m):
        # m is the adjacency weighted graph matrix
        #ver is for vertical traversal
        #hor is for horizontal traversal
        for ver in range(self.num):
            newlist = []
            for hor in range(self.num):
                newlist.append(m[ver][hor])
                if m[ver][hor] != FloydWarshall.POSITIVE_INFINITY:
                    self.next[ver][hor]=hor 
            self.matrix.append(newlist)
            self.dp.append(newlist[::])
    def solve(self):
        #this is the place where to main algorithm is implemented to solve it
        for k in range(self.num):
            for i in range(self.num):
                for j in range(self.num):
                    if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:
                        self.dp[i][j] = self.dp[i][k]+self.dp[k][j]
                        self.next[i][j] = self.next[i][k]
        self.solved = True
    def findnegativecycles(self):
        # this is to find the negative cycles present or not in the graph
        if not self.solved:
            # this is to conform that solve function to run and then only we
            # can find the negative cycles present or not  
            self.solve()
        for k in range(self.num):
            for i in range(self.num):
                for j in range(self.num):
                    if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:
                        self.dp[i][j] = FloydWarshall.NEGATIVE_INFINITY
                        self.next[i][j] = FloydWarshall.REACHES_NEGATIVE_INFINITY
                        self.negativecycleexists = True
        self.solvenegative = True
    def isnegativecycleexists(self):
        if not self.solvenegative:
            self.findnegativecycles()
        return self.negativecycleexists
    def shortestpath(self,start,end):
        # the shortest path is generated based on the dp graph 
        # we will return empty list when we cannot go to end from the starting node.
        # we will return None when we reach the negative cycle from start to end path some where in it.
        # we will return the path with not empty list when ever we can find the path from source to destination.
        path = []
        if not self.solvenegative:
            self.findnegativecycles()
        if self.dp[start][end] == FloydWarshall.POSITIVE_INFINITY:
            return path
        procede = start
        while procede != end:
            if self.next[procede][end] == FloydWarshall.REACHES_NEGATIVE_INFINITY:
                return None
            path.append(procede)
            procede = self.next[procede][end]
        if self.next[procede][end] == FloydWarshall.REACHES_NEGATIVE_INFINITY:
            return None
        return path



