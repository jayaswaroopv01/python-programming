class node:
    def __init__(self,data):
         self.data=data
         self.left=None
         self.right=None
def count_node(node):
         if node is None:
             return 0
         return 1 + count_node(node.left) + count_node(node.right)
root=node("ceo")
root.left=node("manager a")
root.right=node("manager b")
root.left.left=node("staff 1")
root.left.right=node("staff 2")
print("total people in org:",count_node(root))
