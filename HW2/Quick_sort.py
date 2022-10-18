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
a=[1,2,3,4,5,6,7,8,9,10,11]
print(quick_sort(a))
