#creation of the node

class Node:
    def __init__(self,info):
        self.info=info
        self.link=None

n1=Node(10)
print(n1.info)