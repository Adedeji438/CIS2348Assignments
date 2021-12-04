# Adedeji Akingbola
# 173979
# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        largest_value_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[largest_value_index]:
                largest_value_index = j
        numbers[i], numbers[largest_value_index] = numbers[largest_value_index], numbers[i]
        for x in numbers:
            print(x, end=' ')
        print()
    return numbers

if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = []
    inp = input().split()
    for i in inp:
        numbers.append(int(i))
    selection_sort_descend_trace(numbers)
