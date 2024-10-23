def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Finding the middle point to divide the array
    mid = len(arr) // 2
    
    # Recursively sorting the two halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merging the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    
    # Merging the two arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # Adding remaining elements (if any)
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

# Example usage
if __name__ == "__main__":
    sample_array = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort(sample_array)
    print("Sorted array:", sorted_array)
