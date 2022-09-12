def quick_sort(nums):
    if len(nums)==1:
        return [nums[0]]
    if len(nums)==0:
        return []
    pivot = sum(nums)/len(nums)
    first=[]
    second=[]
    for i in range(len(nums)):
        if nums[i]<pivot:
            first.append(nums[i])
        if nums[i]>=pivot:
            second.append(nums[i])
    return quick_sort(first)+quick_sort(second)
a=[11,10,9,8,7,6,5,4,3,2,1]
print(quick_sort(a))
