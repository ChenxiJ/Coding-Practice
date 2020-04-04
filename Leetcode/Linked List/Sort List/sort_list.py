class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# this is to merge two sorted lists
def merge_two_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2


def sort_list(head):
    # important to check head and head.next for both odd and even length cases
    if head is None or head.next is None:
        return head
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    else:
        head2 = slow.next
        # break list into two
        slow.next = None

    # this is such important concept, in function A's return calls another function which calls A
    return merge_two_lists(sort_list(head), sort_list(head2))


# the rest two functions are to help to examine the lists by creating a list from an array
def build_list(arr):
    head = ListNode(arr[0])
    i = 1
    tail = head
    while i < len(arr):
        node = ListNode(arr[i])
        tail.next = node
        tail = node
        i += 1
    return head


def get_sort_list_from_array(arr):
    return sort_list(build_list(arr))
