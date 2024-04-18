class Node:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.data = key
        
def inordertraversal(root):
    st = []
    curr = root
    
    while True:
        if curr is not None:
            st.append(curr)
            curr = curr.left
        elif(st):
            curr  = st.pop()
            print(curr.data, end = " ")
            curr = curr.right
        else:
            break
    print()
    
    
#using recurrsion

def recurrsion(root):
    
    if root is None: return
    
    recurrsion(root.left)
    
    print(root.data, end = " ")
    
    recurrsion(root.right)
    
    
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
     
    inordertraversal(root)
    print("recurssion Output")
    recurrsion(root)