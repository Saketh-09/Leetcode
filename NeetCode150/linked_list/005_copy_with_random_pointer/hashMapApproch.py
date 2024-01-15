class Solution(object):
    def copyRandomList(self, head):
        hashMap = {None:None}
        curr = head
        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            hashMap[curr].next = hashMap[curr.next]
            hashMap[curr].random = hashMap[curr.random]
            curr = curr.next
        return hashMap[head]