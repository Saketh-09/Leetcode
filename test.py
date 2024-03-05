def enh_merge_count_inv(arr, left, right):
    count_inv = 0
    if left < right:
        mid = (left + right) // 2
        count_inv += enh_merge_count_inv(arr, left, mid)
        count_inv += enh_merge_count_inv(arr, mid + 1, right)
        count_inv += merge_array_count_inv(arr, left, mid, right)
    return count_inv

def merge_array_count_inv(arr, ll, mm, rr):
    left = arr[ll:mm + 1]
    right = arr[mm + 1:rr + 1]
    ii = jj = 0
    kk = ll
    swaps = 0
    while ii < len(left) and jj < len(right):
        if left[ii] <= right[jj]:
            arr[kk] = left[ii]
            ii += 1
        else:
            arr[kk] = right[jj]
            jj += 1
            swaps += (mm + 1) - (ll + ii)
        kk += 1
    while ii < len(left):
        arr[kk] = left[ii]
        ii += 1
        kk += 1
    while jj < len(right):
        arr[kk] = right[jj]
        jj += 1
        kk += 1
    return swaps