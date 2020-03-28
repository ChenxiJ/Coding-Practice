from heapq import heappop, heappush, heapify


def cookies_sweetness(A, k):
    heapify(A)
    count = 0
    try:
        while A[0] < k:
            cookie1 = heappop(A)
            cookie2 = heappop(A)
            cookie_new = cookie1 + 2 * cookie2
            heappush(A, cookie_new)
            count += 1
        return count
    except:
        return -1
