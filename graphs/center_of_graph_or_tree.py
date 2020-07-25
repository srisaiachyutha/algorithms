#this program is used to find the center of the undirected graph or tree

def center_of_graph_or_tree(m):
    degree = [sum(m[i]) for  i in range(len(m))]
    visted = [False]*len(m)
    #q = sum(j for i,j in enumerate(degree) if j==1])
    q = [i for i ,j in enumerate(degree) if j==1]
    #s = sum(degree)
    n = len(m)
    while q:
        l=[]
        for i in q:
            visted[i]=True
            degree[i]=0
            n-=1#this will maintain still how many nodes must be visited
            for j in range(len(m)):
                #checking whether there is a conection between the present node and the other nodes
                #if it is not visited then we make degree of that element to be decreased by one and we make 
                if m[i][j]==1 and not visted[j]:
                    degree[j]-=1
                    if degree[j] == 1:
                        l.append(j)
        if len(l)==n:
            break #if length is equal to the not visited numbers at that we need to break it 

        q = l
    # the not visited nodes are the centers of the undirected acyclic graph
    return [i for i,j in enumerate(visted) if not j]

    
            
     

def main():
    n = int(input('enter the no of vertices in the graph or undirected-tree'))
    print('enter the adjacency matirx data of undirected graph or tree')
    matrix = []
    for i in range(n):
        print('enter the data of the row ',i)
        matrix.append(list(map(int,input().split())))
    centers = center_of_graph_or_tree(matrix)
if __name__ == "__main__":
    main()