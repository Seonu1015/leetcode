# 234. Palindrome Linked List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        values = [] # 빈 리스트 생성
        current = head

        while current:
            values.append(current.val)
            current = current.next # 현재 노드의 다음 노드로 업데이트            

        return values == values[::-1] # 파이썬에서는 [::-1]을 사용해서 리스트를 뒤집을 수 있음
    
def createLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
    return head
    
solution = Solution()
lst = createLinkedList([1,2,3,3,2,1])
print(solution.isPalindrome(lst))