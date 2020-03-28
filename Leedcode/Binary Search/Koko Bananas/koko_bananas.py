def min_eating_speed(piles, H):
    def is_possible(speed, H):
        # k//k = 1, want it in one go
        return sum((p - 1) // speed + 1 for p in piles) <= H

    # binary search to find the speed in O(NlgN)
    low = 1
    high = max(piles)

    while low <= high:
        mid = low + (high - low) // 2

        if not is_possible(mid, H):
            low = mid + 1
        else:
            high = mid - 1
    return low