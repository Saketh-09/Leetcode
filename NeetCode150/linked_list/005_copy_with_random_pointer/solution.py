class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Create a copy of each node and insert it after the original node.
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Step 2: Assign random pointers for the copied nodes.
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the original and copied nodes.
        original_head = head
        new_head = head.next
        new_current = new_head

        while original_head:
            original_head.next = new_current.next
            original_head = original_head.next

            if original_head:
                new_current.next = original_head.next
                new_current = new_current.next

        return new_head
