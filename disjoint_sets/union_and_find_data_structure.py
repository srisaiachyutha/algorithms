class DSU :
    def __init__(self,number):
        self.rank = [0 for i in range(number)]
        self.parent = [i for i in range(number)]
    def find_parent(self,child):
        if child != self.parent[child]:
            self.parent[child] = self.find_parent(self.parent[child])
        return self.parent[child]
    def union_children(self,child_one , child_two):
        parent_one = self.find_parent(child_one)
        parent_two = self.find_parent(child_two)
        if self.rank[parent_one] > self.rank[parent_two]:
            self.parent[parent_two] = parent_one
        else:
            self.parent[parent_one] = parent_two
            if self.rank[parent_one] == self.rank[parent_two]:
                self.rank[parent_two]+=1