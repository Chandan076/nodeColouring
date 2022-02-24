class Graph():
 
    def _init_(self, vertices):

        self.V = vertices
        self.graph = [[0 for column in range(vertices)]\
                              for row in range(vertices)]
 
    def isSafe(self, v, colour, c):

        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def graphColourUtil(self, m, colour, v):

        if v == self.V:
            return True
 
        for c in range(1, m + 1):

            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0
 

    def graphColouring(self, m):

        colour = [0] * self.V

        if self.graphColourUtil(m, colour, 0) == None:
            return False

        print ("Color Pattern:")

        for c in colour:
            print (c,end=' ')
        return True

if __name__ == "__main__":
    g = Graph()
    g.V = 4
    g.graph = [[1, 1, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]

    m = 4
    g.graphColouring(m)

