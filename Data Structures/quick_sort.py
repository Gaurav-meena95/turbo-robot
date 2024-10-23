def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and combine

# Example usage
if __name__ == "__main__":
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quick_sort(sample_array)
    print("Sorted array:", sorted_array)
