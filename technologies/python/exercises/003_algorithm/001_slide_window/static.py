def max_sum_subarray(arr, k):
    if len(arr) < k:
        return -1
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    print(f"arr: {arr} max_sum: {max_sum} window_sum: {window_sum}")

    # Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        print(f"i: {i} k: {k} len: {len(arr)} window_sum: {window_sum} window: {arr[i] - arr[i - k]}")
        max_sum = max(max_sum, window_sum)
    
    return max_sum

arr = [2, 1, 5, 1, 3, 2, 8]
k = 3
print(max_sum_subarray(arr, k))
