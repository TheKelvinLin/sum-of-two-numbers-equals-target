def twoSum(nums, target):
    first = 0
    second = 0
    index = 0

    for item in nums:

        if item == target:
            second = index
            break
        elif item < target:
            target = target - item
            first = index
            
        index = index + 1

    return ("[" + str(first) + "," + str(second) + "]")
    
result=twoSum([11, 15, 1, 8], 12)
print(result)