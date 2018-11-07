def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def palindromeIndex(s):
    if isPalindrome(s):
        return -1
    else:
        left = 0
        right = len(s) - 1
        while left <= len(s) // 2:
            while s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if s[left + 1] == s[right] and s[left] == s[right - 1]:
                    index = left
                    # this case can remove both, not sure which is correct, save for future consideration
                    backUp = right
                    if isPalindrome(s[:index] + s[index + 1:]):
                        return index
                    elif isPalindrome(s[:backUp] + s[backUp + 1:]):
                        return backUp
                    else:
                        return -1

                elif s[left + 1] == s[right] and s[left] != s[right - 1]:
                    index = left
                    if isPalindrome(s[:index] + s[index + 1:]):
                        return index
                elif s[left + 1] != s[right] and s[left] == s[right - 1]:
                    index = right
                    if isPalindrome(s[:index] + s[index + 1:]):
                        return index
                else:
                    return -1