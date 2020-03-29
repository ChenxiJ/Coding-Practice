def is_possible_divided(nums, k):
    if len(nums) % k != 0:
        return False

    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = dic.get(nums[i], 0) + 1
    sorted_keys = sorted(dic)
    for key in sorted_keys:
        while dic[key] > 0:
            for i in range(key + 1, key + k):
                if i in dic and dic[i] > 0:

                    dic[i] -= 1
                else:
                    return False
            dic[key] -= 1
    return True
