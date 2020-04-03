# can have 2n - 1 center, check very element and the 'gap' after. last element is not checked since max_len is 1 as center
def longest_palindrome_substring(s):
    if len(s) == 0:
        return ''

    def with_center(c):
        interval_a = [c, c]
        interval_b = [c, c]
        i_a = 0
        j = 0
        while c - i_a >= 0 and c + j < len(s):
            if not s[c - i_a] == s[c + j]:
                break
            interval_a = [c - i_a, c + j]
            i_a += 1
            j += 1

        i_b = -1
        j = 0
        while c - i_b >= 0 and c + j < len(s):
            if not s[c - i_b] == s[c + j]:
                break
            interval_b = [c - i_b, c + j] if c - i_b <= c + j else [c + j, c - i_b]
            i_b += 1
            j += 1
        return interval_a if interval_a[1] - interval_a[0] > interval_b[1] - interval_b[0] else interval_b

    temp_max = 0
    ans = [0, 0]
    for i in range(len(s) - 1):
        interval = with_center(i)
        if (interval[1] - interval[0]) > temp_max:
            ans = interval
            temp_max = interval[1] - interval[0]

    return s[ans[0]: ans[1] + 1]