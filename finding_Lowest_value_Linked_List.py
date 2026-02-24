# Creating a linked List and Finding lowest Value in the List 

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def find_lowest_value(head):
    minValue = head.data
    currentNode=head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue=currentNode.data
        currentNode=currentNode.next
    return minValue
    
node1=Node(44)
node2=Node(22)
node3=Node(66)
node4=Node(11)
node5=Node(88)
node6=Node(33)
node7=Node(77)
node8=Node(55)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7
node7.next=node8

print("The Minimum Value in the Linked List:",find_lowest_value(node1))