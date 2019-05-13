
balanced_array = []


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class balanced_tree(object):

    def binary_insert(self, root, new):

    # if root value is empty, new object instantiation is performed,
    # the value 'new'is the value passed from an array
        if root is None:
            root = TreeNode(new)

    # if root isn't none, follow through the conditional statements to
    # check for left and right values, and instantiate objects on conditions being true
    # initially check for left and check for right on left being invalid
        else:
            if root.val > new:
                if root.left is None:
                    root.left = TreeNode(new)
                else:
                    self.binary_insert(root.left, new)
            else:
                if root.right is None:
                    root.right = TreeNode(new)
                else:
                    self.binary_insert(root.right, new)

    # when left or right insertion is successful, set a new height value for the current + 1
    # this means that the current root will represent the current number of children objects + 1
        root.height = 1 + self.return_max_height(root)

    # balance returns a single int that is calculated by taking the current depth of
    # left and right children and subtracting 1 from the other.
        balance = self.getBalance(root)

    # if the return is 1, that means that left child was larger and subtracting
    # the height of the right child mean't that the depths weren't equal and that left is
    # at least 1 object deeper, so perform a left rotate
        if balance > 1:

            if new > root.left.val:
                root.left = self.left_rotate(root.left)
                return self.rightRotate(root)

            elif new < root.left.val:
                return self.rightRotate(root)

    # if the balance calculation creates a -1 value, then the depth of the right children
    # where at least 1 child deeper, so when the depth was subtracted, it went over zero and
    # hit -1. This will require a right rotation to be performed
        elif balance < -1:

            if new > root.right.val:
                return self.left_rotate(root)

            elif new < root.right.val:
                root.right = self.rightRotate(root.right)
                return self.left_rotate(root)

    # return the root current root value for every iteration of this function to process every int
    # in the array
        return root

    # functionzed max height to remove repeated code
    def return_max_height(self, root):
        return max(self.getHeight(root.left),
                   self.getHeight(root.right))


    def auto_balance(self):
    # todo check the balance values within a function and determine if left or right rotate is needed
    # return the necessary rotation when executed
        pass

    # left rotate
    # pass the current root of a node as a param
    # initiate object to store the right value of the node passed
    # store the left value of the parameter object, inside a current_left_Value object
    # reassign the node.left object - which is a node object its self - with the node passed
    # as a paramter
    # reassign the variable current_left_value, as the right child of the paramterised node.
    # repeated with right child values for the rightRotate function
    def left_rotate(self, node):

        root_value = node.right

        current_left_Value = root_value.left

        root_value.left = node

        node.right = current_left_Value

        node.height = 1 + self.return_max_height(node)
        root_value.height = 1 + self.return_max_height(root_value)

        return root_value

    def rightRotate(self, node):

        root_value = node.left
        current_right_value = root_va
        lue.right

        root_value.right = node
        node.left = current_right_value

        node.height = 1 + self.return_max_height(node)
        root_value.height = 1 + self.return_max_height(root_value)
        return root_value

    # return the existing height value of the passed root object
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # by subtracting the height of left or right children, you can get 1 or -1 values. This
    # makes it observable as to which branches are out of balance
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    # pre order, post order and in order are typical methods of traversing binary trees
    def preOrder(self, root):
        if not root:
            return
        print(root.val)
        balanced_array.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def post_order(self, root):
        if not root:
            return

        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val)

    def in_order(self, root):
        if not root:
            return

        self.post_order(root.left)
        print(root.val)
        self.post_order(root.right)


if __name__ == "__main__":

    #example array to iterate
    tree_values = [4, 3, 1, 5, 2]
    
    tb = balanced_tree()

    root_value = None

    for x in tree_values:
        root_value = tb.binary_insert(root_value, x)

    tb.preOrder(root_value)


