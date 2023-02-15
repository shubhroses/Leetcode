from __future__ import print_function

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

def reverse_alternate_k_elements(head, k):
    dummy = Node(0, head)
    groupPrev = dummy

    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next
        prev = kth.next
        curr = groupPrev.next

        while curr != groupNext:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
        groupPrev = getKth(tmp, k)

    return dummy.next

def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


if __name__ == "__main__":
    main()
