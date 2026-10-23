from collections import deque
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(n):
    if n:inorder(n.left);print(n.data,end="");inorder(n.right)
def preorder(n):
    if n:print(n.data,end="");preorder(n.left);preorder(n.right)
def postorder(n):
    if n:postorder(n.left);postorder(n.right);print(n.data,end="")
def levelorder(root):
    q=deque([root])
    while q:
        n=q.popleft()
        print(n.data,end="")
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
root=node(1)
root.left=node(2);root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
print("inorder:",end="");inorder(root);print()
print("preorder:",end="");preorder(root);print()
print("postorder:",end="");postorder(root);print()
print("level-order:",end="");levelorder(root);print()
