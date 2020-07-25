
def depth_first_search(m,s):
    vis = [False]*len(m)
    stack = [s-1]
    while stack:
        node = stack.pop()
        print(node)
        vis[node]=True
        for i in range(len(m)):
            if m[node][i]==1 and not vis[i]:
                stack.append(i)
def main():
    print('enter the no of vertices of the graph')
    n = int(input())
    print('enter the adjacency matrix data')
    matrix=[]
    for i in range(len(n)):
        print('enter the data into the row',i+1)
        matrix.append([])
        for j in range(len(n)):
            matrix[-1].append(int(input()))
    start = int(input('enter the starting node to explore'))
    depth_first_search(matrix,start)



if __name__ == "__main__":
    main()