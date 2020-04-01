class TreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def search(self,data):
        if not self.root:
            print('tree is empty to perform search operation')
            return self.root
        y=None
        x=self.root
        while x and x.val != data:
            y=x
            if x.val <data:
                x = x.right
            else:
                x = x.left
        if not x:
            
            print('searching element is not present')
            return None
        return (x,y)
    
    def delete(self,data):
        def deleteNode( root, key) :
		    if not root:
		        return root
		    y=None
		    x=root
		    while x and x.val != key:
		        y=x
		        if x.val > key:
		            x = x.left
		        else:
		            x = x.right
		    if x==None:
		        return root
		    if not x.left and not x.right:
		        if not y:
		            root=None
		            return root
		        else:
		            if x.val < y.val:
		                y.left = None
		            else:
		                y.right = None
		            return root
		    elif not x.right:
		        if not y:
		            root = x.left
		            return root
		        else:
		            if x.val < y.val:
		                y.left = x.left
		            else:
		                y.right = x.left
		            return root
		    elif not x.left:
		        if not y :
		            root = x.right
		            return root
		        else:
		            if x.val < y.val:
		                y.left = x.right
		            else:
		                y.right = x.right
		            return root
		    else:
		        k=x.right
		        p=None
		        while k.left:
		            p=k
		            k=k.left
		        x.val=k.val
		        x.right = self.deleteNode(x.right,k.val)
		        return root
		    
        self.root = deleteNode(self.root,data)   
            
            
    def insert_iterative(self,data):
        if self.root==None:
            self.root=TreeNode(data)
        else:
            z=TreeNode(data)
            y=None
            x=self.root
            while x:
                y=x
                if z.val < x.val:
                    x = x.left
                else:
                    x = x.right
            if y==None:
                self.root=z
            elif z.val < y.val:
                y.left = z
            else:
                y.right = z
    def preorder_recursive(self):
        def pre(root):
            if root:
                print(root.val,end = ' ')
                pre(root.left)
                pre(root.right)
        pre(self.root)

    def inorder_recursive(self):
        def i(root):
            if root:
                i(root.left)
                print(root.val,end =' ')
                i(root.right)
        i(self.root)
    def postorder_recursive(self):
        def post(root):
            if root:
                post(root.left)
                post(root.right)
                print(root.val,end = ' ')
        post(self.root)

    def maximum_element(self):
        if not self.root:
            return self.root
        else:
            y=None
            x=self.root
            while x:
                y=x
                x=x.right
            print(y.val)
            return y
    def minimum_element(self):
        if not self.root:
            return self.root
        else:
            y=None
            x=self.root
            while x:
                y=x
                x=x.left
            print(y.val)
            return y
    
print('enter the list of elements to form a tree')
l=list(map(int,input().split()))
b=BinaryTree()
for i in l:
    b.insert_iterative(i)
b.inorder_recursive()
print()
b.preorder_recursive()
print()
b.postorder_recursive()
print()
b.minimum_element()
b.maximum_element()

