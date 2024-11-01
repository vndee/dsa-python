# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def _mergeKLists(self, lists):
        """
        Time: O(NK)
        Space: O(1)
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        ans = ListNode()
        cur = ans

        while True:
            min_x = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue

                if min_x == -1 or (lists[min_x] and lists[i].val < lists[min_x].val):
                    min_x = i

            if min_x != -1:
                ans.next = ListNode(val=lists[min_x].val, next=None)
                ans = ans.next

                lists[min_x] = lists[min_x].next
            else:
                break

        return cur.next

    def mergeKLists(self, lists):
        """
        Time: O(N log K)
        Space: O(k)
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        from heapq import heappop, heappush

        dummy = ListNode()
        curr = dummy

        heap = []

        for i, head in enumerate(lists):
            if head:
                heappush(heap, (head.val, i, head))

        while heap:
            val, i, node = heappop(heap)

            curr.next = ListNode(val=val)
            curr = curr.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))

    sol = Solution()
    ans = sol.mergeKLists([l1, l2, l3])
    while ans:
        print(ans.val, end=" ")
        ans = ans.next
