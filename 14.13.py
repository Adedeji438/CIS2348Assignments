# Adedeji Akingbola
# 1793979
# Global variable
num_calls = 0

# TODO: Write the partitioning algorithm - pick the middle element as the 
#       pivot, compare the values using two index variables l and h (low and high), 
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, i, k):
    # lower = i - 1
    # print("DEBUG: lower: {} i: {} k:{}".format(lower, i, k))
    # pivot = user_ids[k]
    # for j in range(i, k):
    #     if user_ids[j] < pivot:
    #         lower += 1
    #         user_ids[lower], user_ids[j] = user_ids[j], user_ids[lower]
    # user_ids[lower + 1], user_ids[k] = user_ids[k], user_ids[lower + 1]
    # return (lower + 1)

    #pivot_index = i
    pivot_index = i + (k - i) // 2
    pivot = user_ids[pivot_index]
    finished = False
    left = i
    right = k
    while finished == False:
        while user_ids[left] < pivot:
            left += 1
        while user_ids[right] > pivot:
            right -= 1
        if left >= right:
            finished = True
        else:
            user_ids[left], user_ids[right] = user_ids[right], user_ids[left]
            left += 1
            right -= 1
    return right


# TODO: Write the quicksort algorithm that recursively sorts the low and 
#       high partitions. Add 1 to num_calls each time quisksort() is called
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    if(i >= k):
        return
    if i < k:
        mid = partition(user_ids, i, k)
        quicksort(user_ids, i, mid)
        quicksort(user_ids, mid + 1, k)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
        
    # Initial call to quicksort 
    quicksort(user_ids, 0, len(user_ids) - 1)
    
    # Print number of calls to quicksort
    print(num_calls)
    
    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
