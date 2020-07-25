#given the nodes and edges of a un-cyclic graph and making it into the 
# rooted tree is the main task of this program
class Treenode:
    def __init__(self,data = None):
        self.val = data
        self.children = []
def construct_rooted_tree_using_adjacency_list(m,root_index):
    #this function will be used for constructing the tree from the graph 
    #for the specified index or node when adjacency list is given
    
    root = Treenode(root_index) #first we create a root node of the tree
    q=[root]
    vis = [False]*len(m)
    while q:
        node = q.pop(0)
        vis[node.val]=True
        # here we mark the node as visited and then we explore the children of it
        for i in m[node.val]:
            if not vis[i]:
                k = Treenode(i) # here we are creating the treenodes for the present 
                #curent running node
                node.children.append(k)#we are attaching the created children nodes to the 
                #present explore node and also to the queue to do the bfs
                q.append(k)
    return root




def main():
    #this program is used when adjacency list is given
    n = int(input('enter the nodes in the acyclic graph'))
    print('enter the adjacency list of the graph')
    matrix = []
    for i in range(n):
        print('enter the adjacency list of the node ',i)
        matrix.append(list(map(int,input().split())))
    root_index = int(input('enter the root index for which it should become the root of the tree'))
    root = construct_rooted_tree_using_adjacency_list(matrix,root_index)
    #this root variable will contained the rooted graph information
if __name__ == "__main__":
    main()