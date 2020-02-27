def binarySearch (num, lst):
    mid = (len(lst)//2)
    if num == lst[mid]:
        return mid
    elif len(lst) == 1:
        return False
    elif num > lst[mid]:
        return mid + binarySearch(num, lst[mid+1:]) + 1
    else:
        return binarySearch(num, lst[0:mid])

print(binarySearch(1,[2,3,4,5,6,7,8]))

