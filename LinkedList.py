##simple linked list and node class written in python

#create the "Node" structure
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def getData(self):
        return self.data

#create the structure to hold information about the list
#including methods to append or remove a Node
class LinkedList:

    def __init__(self,data):
        self.head = Node(data, None)

    def getHead(self):
        return self.head

    def append(self, data):
        cur_node = self.head
        while(cur_node.next_node is not None):
            cur_node = cur_node.next_node
        cur_node.next_node = Node(data)

    def remove(self, value):
        if self.head.data == value:
            self.head = self.head.next_node
            return
        prev_node = self.head
        cur_node = self.head.next_node
        while(True):
            if (cur_node.data == value):
                prev_node.next_node = cur_node.next_node
            if (cur_node.next_node == None):
                break
            prev_node = cur_node
            cur_node = cur_node.next_node
        return None

    def printList(self):
        cur_node = self.head
        while(cur_node.next_node):
            print cur_node.data
            cur_node = cur_node.next_node
        print cur_node.data

    def findNode(self, value):
        cur_node = self.head
        while(True):
            if (cur_node.data == value):
                return cur_node
            if (cur_node.next_node == None):
                break
            cur_node = cur_node.next_node
        return None

if __name__ == "__main__":
    print '-> first test with data "information"'
    data = "information"
    #pass in data for "head" Node
    linked_list = LinkedList(data)
    head = linked_list.getHead()
    print head.getData()

    print '-> one more Node added with data "more information"'
    moredata = "more information"
    linked_list.append(moredata)
    linked_list.printList()

    print '-> another test adding value "another piece of information"'
    anotherpiece = "another piece of information"
    linked_list.append(anotherpiece)
    linked_list.printList()

    print '-> return Node with specified value "another piece of information"'
    found_node = linked_list.findNode("another piece of information")
    print found_node.data

    print '-> search for value that doesn\'t exist'
    no_node = linked_list.findNode("not a value")
    if no_node == None:
        print 'Value searched for does not exist'

    print '-> remove "more information" value'
    linked_list.remove("more information")
    linked_list.printList()

    print '-> remove "information" value'
    linked_list.remove("information")
    linked_list.printList()
