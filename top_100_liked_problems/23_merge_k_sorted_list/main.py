# Problem: https://leetcode.com/problems/merge-k-sorted-lists/

# Travsersing through all lists requires k*N steps, which is efficient enough
# We will focus more on how to achieve O(1) space complexity, which should
# greatly improve our performance

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def gen_list(items):
    head = None
    for i, item in enumerate(items):
        node = ListNode(item)
        if i == 0:
            head = prev = node
        else:
            prev.next = node
            prev = prev.next
    return head

def pprint(node):
    def _iter(node):
        while node is not None:
            yield str(node.val)
            node = node.next
    print(' -> '.join(_iter(node)))

def merge_two(node1, node2):
    if node1 is None:
        return node2
    if node2 is None:
        return node1
    node1, node2 = (node1, node2) if node1.val < node2.val else (node2, node1)
    curr = merged = node1
    while True:
        while node1.val <= node2.val:
            if node1.next is None:
                curr = node1
                curr.next = node2
                return merged
            curr, node1 = node1, node1.next
        curr.next = node2
        node2, node1 = node1, node2

# Method #1: Merge two lists at a time
def mergeKLists(lists):
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    return merge_two(
        mergeKLists(lists[0:len(lists)//2]),
        mergeKLists(lists[len(lists)//2:])
    )

