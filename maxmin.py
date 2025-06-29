nums = [2, 4, 1, 0, 2, -1]


def maxmin():
    max = nums[0]
    min = nums[0]
    newnums = []
    for i in nums:
        if i > max:
            max = i
        if i < min:
            min = i
    newnums.append(min)
    newnums.append(max)
    return newnums


print(maxmin())
nums = [2, 4, 1, 0, 2, -1]
