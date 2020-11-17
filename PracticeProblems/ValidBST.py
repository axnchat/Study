class Node(object):
    def __init__(self,value,left=None,right=None):
            self.value= value
            self.left = left
            self.right = right

class Solution(object):
    def IsValidBST(self,this,low,high):
        if not this: 
            return True
        if not this.left :
            leftValue = float('-inf')
        else:
            leftValue = this.left.value

        if not this.right :
            rightValue = float('inf')
        else:
            rightValue = this.right.value

        val = this.value
        if val < high and val > low :
            return self.IsValidBST(this.right,val,) and self.IsValidBST(this.left)
        
        return False

n = Node(5)
n.left = Node(3)
n.right = Node(7)
n.right.left = Node(2)

print (Solution().IsValidBST(n,n.left.value,n.right.value))

        
