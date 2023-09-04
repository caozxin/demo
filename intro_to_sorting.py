from typing import List
import math

def insertion_sort_list(unsorted_list: List[int]) -> List[int]:
    for i, entry in enumerate(unsorted_list):
        current = i
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1
    return unsorted_list

def selection_sort_list(unsorted_list: List[int]) -> List[int]:
    for idx, entry in enumerate(unsorted_list): 
        # min = float('-inf')
        curr = idx
        min = unsorted_list[curr]
        min_idx = curr
        print('curr', curr)
        print('min', min)
        print('min_idx', min_idx)
        for running_idx in range(curr, len(unsorted_list)):
            if unsorted_list[running_idx] < min:
                min = unsorted_list[running_idx]
                min_idx = running_idx
                print('new min', min)
                print('new min_idx', min_idx)
                running_idx +=1
                print("running_idx", running_idx)

        unsorted_list[curr], unsorted_list[min_idx] = unsorted_list[min_idx], unsorted_list[curr]
        print('new unsorted_list', unsorted_list)
    return unsorted_list

def updated_selection_sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for curr_idx in range(n): 
        min_idx = curr_idx
        for running_idx in range(curr_idx, n):
            if unsorted_list[running_idx] < unsorted_list[min_idx]:
                min_idx = running_idx
                running_idx +=1
        unsorted_list[curr_idx], unsorted_list[min_idx] = unsorted_list[min_idx], unsorted_list[curr_idx]

    return unsorted_list

def bubble_sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    pointer_max = n
    for curr_idx in range(n): 
        for pointer_idx in range(pointer_max-1):
            if unsorted_list[pointer_idx] > unsorted_list[pointer_idx +1]:
                unsorted_list[pointer_idx], unsorted_list[pointer_idx +1] = unsorted_list[pointer_idx +1], unsorted_list[pointer_idx]
        pointer_max -= 1
    return unsorted_list


def merge_sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list) 
    
    # split the list into two halfs until each unit is just only element
    if n > 1:
        #check if the number of the elements are odd or even
        if n % 2 == 0:
            half_max = int(n/2)
        else:
            half_max = int((n+1)/2)
        print('half_max', half_max)
        
        first_half, second_half = unsorted_list[: half_max], unsorted_list[half_max:]
        result_list = []
        print('first_half', first_half)
        print('second_half', second_half)
        merge_sort_list(first_half)
        merge_sort_list(second_half)
        pointer = half_max - 1

        print("pointer", pointer)
        # print('first_half[pointer]', first_half[pointer])
        # print('second_half[pointer]', second_half[pointer])
        print(" -------merging-----------")
        if first_half[pointer] > second_half[pointer]:
            result_list.append(second_half[pointer])
            result_list.append(first_half[pointer])
        else:
            result_list.append(first_half[pointer])
            result_list.append(second_half[pointer])

        print('result_list', result_list)
        pointer += 1
        

        
    # return unsorted_list
def default_merged_sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    if n <= 1:
        return unsorted_list
    midpoint = n // 2
    # print('midpoint', midpoint)
    # left_list, right_list = sort_list(unsorted_list[:midpoint]), sort_list(unsorted_list[midpoint:])
        
    left_list, right_list  = unsorted_list[: midpoint], unsorted_list[midpoint:]
    sort_list(left_list)
    sort_list(right_list)
    print('left_list, right_list ')
    print(left_list, right_list )
    result_list = []
    left_pointer, right_pointer = 0, 0
    while left_pointer < midpoint or right_pointer < n - midpoint:
        if left_pointer == midpoint:
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        elif right_pointer == n - midpoint:
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        elif left_list[left_pointer] <= right_list[right_pointer]:
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result_list.append(right_list[right_pointer])
            right_pointer += 1
    return result_list

if __name__ == '__main__':
    example = [5, 3, 1, 2, 4]
    # print("input", example)
    sort_list = default_merged_sort_list
    result = sort_list(example)
    print("result", result)
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))


