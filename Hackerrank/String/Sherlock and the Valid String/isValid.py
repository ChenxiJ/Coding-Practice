# two cases, one is everything appears n times, one char n+1 times
# the other is everything appears n times, only one char appears 1 time
def isValid(s):
    mapp = {}
    for i in s:
        if i in mapp:
            mapp[i] += 1
        else:
            mapp[i] = 1
    count = mapp[s[0]]
    diff = 0
    for key, value in mapp.items():
        if value == count:
            continue
        else:
            if abs(count - value) > 1 and min(count, value) != 1:
                return 'NO'
            else:
                # very important which case comes first, if write "if abs(count - value) == 1"...
                # will be wrong. needs to see which case dominant!
                if min(count, value) == 1:
                    count = max(count, value)
                    diff += 1
                else:
                    count = min(count, value)
                    diff += 1
    if diff > 1:
        return 'NO'
    return 'YES'