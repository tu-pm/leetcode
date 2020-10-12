class LinkedList:
    def __init__(self, values):
        self._head = ListNode()
        self._tail = None
        self._length = 0
        self.append_array(*values)

    def __iter__(self):
        node = self._head.next
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        if isinstance(item, int):
            node = self._head
            item = item if item >= 0 else len(self) + item
            for _ in range(item + 1):
                if node is None:
                    return None
                node = node.next
            return node
        raise NotImplementedError("Not implemented")

    def append_array(self, *values):
        if len(values) == 0:
            return
        node = self._tail if self._tail is not None else self._head
        for val in values:
            node.next = ListNode(val)
            node = node.next
            self._length += 1
        self._tail = node

    def append_node(self, node):
        last = self._tail if self._tail is not None else self._head
        last.next = node
        while last is not None:
            self._length += 1
            last = last.next
        self._tail = last


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3])
    print("->".join(map(str, ll)))
    print(ll[-2])
