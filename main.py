import DataStructures as DS

# myArr = DS.Array([1, 2, 3, 4])
# myArr.print()

# using reversePrint()
# second = DS.LLNode(2)
# first = DS.LLNode(1, second)
# first.print()
# first.reversePrint()

# using LLinsert
# third = DS.LLNode(3)
# first = DS.LLNode(1, third)
# first.print()
# DS.LLinsert(first, 1, 2)
# first.print()

# using LLdelete
# third = DS.LLNode(3)
# second = DS.LLNode(2, third)
# first = DS.LLNode(1, second)
# first.print()
# DS.LLdelete(first, 1)
# first.print()

# using new LLNode constructor
# zoheb = DS.LLNode(2, [4, 6, 8, 10])
# zoheb.print()

# doubly linked list
zoheb = DS.createDLL([7, 3, 1, 9, 10, 16])
DS.printDLL(zoheb) # 7 3 1 9 10 16
zoheb = DS.insertDLL(zoheb, 0, 6)
DS.printDLL(zoheb) # 6 7 3 1 9 10 16
DS.insertDLL(zoheb, 7, 5)
DS.printDLL(zoheb) # 6 7 3 1 9 10 16 5
DS.deleteDLL(zoheb, 3)
DS.printDLL(zoheb) # 6 7 3 9 10 16 5
zoheb = DS.deleteDLL(zoheb, 0)
DS.printDLL(zoheb) # 7 3 9 10 16 5
