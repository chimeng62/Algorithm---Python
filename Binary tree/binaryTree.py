# node class
class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left_node = None
        self.right_node = None

    def insert(self, data,node):
        #to the left of root node
        if data<node.data:
            if node.left_node is None:
                node.left_node = BSTNode(data)
            else:
                self.insert(data,node.left_node)
        #to the right of root node
        else:
            if node.right_node is None:
                node.right_node = BSTNode(data)
            else:
                self.insert(data,node.right_node)

    def getSmallest(self,node):
        currentNode = node
        while currentNode.left_node:
            currentNode= currentNode.left_node
        return currentNode.data

    def getBiggest(self,node):
        currentNode = node
        while currentNode.right_node:
            currentNode= currentNode.right_node
        return currentNode.data

    def search(self,searchValue,node):
        #base case
        #when calling search on a non-existent child node
        if node is None or node.data == searchValue:
            #this return node or None
            return node

        #search on the left 
        elif searchValue < node.data:
            return self.search(searchValue,node.left_node)
        #search on the right :searchValue > node.value
        else:
            return self.search(searchValue,node.right_node)

    def delete(self,deleteValue, node):    
        ###Step 1: Find the node to be deleted
        #base case
        if node is None:
            return None
        #check if the value to be deleted on the left of right of root node
        elif deleteValue<node.data:
            #call recursively on the left node
            node.left_node = self.delete(deleteValue,node.left_node)
            return node
        
        elif deleteValue>node.data:
            node.right_node = self.delete(deleteValue,node.right_node)
            return node
        
        #check if we have found to node to be deleted
        elif deleteValue == node.data:
        ###Step 2: check if the node has any child
            #handle 3 cases
            #1: No child: just delete the node
            #2: has one child
                ##delete the node and move the child to the deleted node's place        
            #3: has 2 children
                ##delete the node and find the next successor node 
                ##(the next number after the deleted node) 
            if node.left_node is None:
                return node.right_node
            elif node.right_node is None:
                return node.left_node

            else:
                node.right_node = self.lift(node.right_node,node)
                return node
    
    def lift(self,node, nodeToDelete):
        if node.left_node:
            node.left_node = self.lift(node.left_node,nodeToDelete)
            return node
        else:
            nodeToDelete.data = node.data
            return node.right_node

############################################################
#######Function to print binary tree graphically
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right_node is None and self.left_node is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_node is None:
            lines, n, p, x = self.left_node._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_node is None:
            lines, n, p, x = self.right_node._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left_node._display_aux()
        right, m, q, y = self.right_node._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
