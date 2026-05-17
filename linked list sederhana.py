class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#membuat node
n1 = Node(10)
n2 = Node(20)

n1.next = n2

#akses data
print(n1.data)
print(n1.next.data)

#penjelasan
# Node adlah struktur dasar linked list
# Next adalah ponter ke node berikutnya

#Linked List :
#terdiri dari node
#tiap node punya :
#data
#pointer ke node berikutnya (next)