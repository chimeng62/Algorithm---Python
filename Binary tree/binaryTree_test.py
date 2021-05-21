from binaryTree import *

root = BSTNode(50)
# insert
root.insert(25,root)
root.insert(75,root)
root.insert(10,root)
root.insert(33,root)
root.insert(55,root)
root.insert(90,root)

print("-----------------Before")
root.display()
root.delete(50,root)

print("-----------------After")
root.display()
