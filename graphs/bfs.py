def breadth_first_search(matrix,start):
    vis = [False]*len(matrix)
    queue = [start-1]
    while queue:
        node = queue.pop(0)
        print(node)
        vis[node]=True
        for i in range(len(matrix)):
            if matrix[node][i]==1 and vis[i]==False:
                queue.append(i)
    

def main():
    print('enter the no of vertices of the graph')
    n = int(input())
    print('enter the adjacency matrix data')
    matrix=[]
    for i in range(len(n)):
        print('enter the data into the row',i+1)
        matrix.append(list(map(int,input().split())))
    start = int(input('enter the starting node to explore'))
    breadth_first_search(matrix,start)



if __name__ == "__main__":
    main()