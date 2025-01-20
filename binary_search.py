def binary_search_with_bounds(arr, x):
    l, r = 0, len(arr) - 1
    steps = 0
    ub = None

    while l <= r:
        steps += 1
        m = (l + r) // 2

        if arr[m] == x:
            return steps, arr[m]

        if arr[m] < x:
            l = m + 1
        else:
            ub = arr[m]
            r = m - 1

    return steps, ub
