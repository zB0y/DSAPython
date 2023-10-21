class Array:
    def __init__(self, inputArr):
        self.arr = inputArr

    def print(self):
        for i in self.arr:
            print(i)

class LLNode:
    def __init__(self, val, next = None):
        self.val = val
        if isinstance(next, LLNode):
            self.next = next
        elif isinstance(next, list):
            self.next = LLNode(next[0], next[1:]) if len(next) > 1 else LLNode(next[0])
        else:
            self.next = next # or None

    def print(self):
        temp = self
        while temp != None:
            print(temp.val, "->", end=' ')
            temp = temp.next
        print("None")

    def reversePrint(self): # reverse prints from end of linked list till this node
        temp = self
        if temp.next == None:
            print(temp.val, "->", end=' ')
        else:
            temp.next.reversePrint()
            print(temp.val, end=' ')

# friend functions for LLNode
def LLinsert(node : LLNode, index : int, val : int): # cannot insert before beginning node
    if index == 0: return
    else: index-=1
    temp = node
    while index > 0:
        if temp == None: return
        temp = temp.next
        index-=1

    temp.next = LLNode(val, temp.next)

def LLdelete(node: LLNode, index : int): # cannot delete beginning node
    if index == 0: return
    else: index-=1
    temp = node
    while index > 0:
        temp = temp.next
        index-=1

    if temp.next != None:
        temp.next = temp.next.next

class DoublyLLNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

def createDLL(arr):
    head = DoublyLLNode(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = DoublyLLNode(arr[i], None, temp)
        temp = temp.next
    return head

def printDLL(node):
    temp = node
    while (temp != None):
        print(temp.val, end=" ")
        temp = temp.next
    print()

def insertDLL(node, index, val): # return newHead if newHead else None
    if index == 0:
        newHead = DoublyLLNode(val, node)
        node.prev = newHead
        return newHead
    else:
        temp = node
        index-=1
        while index > 0:
            if temp == None: return
            else: temp = temp.next
            index-=1

        newNode = DoublyLLNode(val, temp.next, temp)
        if temp.next != None: temp.next.prev = newNode
        temp.next = newNode
        return None

def deleteDLL(node, index):
    if index == 0:
        newHead = node.next
        newHead.prev = None
        node.next = None # delete memory allocation
        return newHead
    else:
        temp = node
        while index > 0:
            temp = temp.next
            index-=1
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

