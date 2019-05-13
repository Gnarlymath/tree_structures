
preorder_array = []

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val
    
    def __str__(self):
        return str(self.left) + " " + str(self.right) + " " + str(self.data)

#recursive binary tree
#check if value is greater or less than current root node value,
#then internally call the function to continue comparing until no more roots 
#are available for comparison
def binary_insert(root, node):
    if root is None:
        root = node

    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                # output_array_left.append(root.left)
                binary_insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right, node)

#typical in order, pre order and post order binary tree traversal.
#This checks the binary insert fucntion, if working, these functions should be predictable for all array values. These are all recursive functions that rely on being called over and over to traverse the tree till exhausted of values
def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.data)
    in_order(root.right)

def pre_order(root):
    if not root:
        return        
    print(root.data)
    preorder_array.append(root.data)
    pre_order(root.left)
    pre_order(root.right)    

def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data)

if __name__ == "__main__":
    #list used for holding all values going into the binary tree
    input_array = [5,8,1,4,11,6]
    # input_array = [1,2,3,4,5]

    #initial root value object created
    rn = TreeNode(input_array[0])

    #iterate remaining list values, starting from index 1:onwards,
    #as index 0 is the initial root value
    for value in input_array[1:]:
        binary_insert(rn, TreeNode(value))

    pre_order(rn)
