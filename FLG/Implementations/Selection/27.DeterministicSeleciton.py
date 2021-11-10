"""
Deterministic Selecttion

Search for the kth-smallest item

The worst-case performance of a randomized selection algorithm is O(n^2 )
"""


def median_of_medians(elems):
    sublists = [elems[j:j + 5] for j in range(0, len(elems), 5)]
    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist) / 2])
    if len(medians) <= 5:
        return sorted(medians)[len(medians) / 2]
    else:
        return median_of_medians(medians)

def get_index_of_nearest_median(array_list, first, second, median):
    if first == second:
        return first
    else:
        return first + array_list[first:second].index(median)

def swap(array_list, first, second):
    array_list[first], array_list[second] = array_list[second], array_list[first]

def partition(unsorted_array, first_index, last_index):
    if first_index == last_index:
        return first_index
    else:
        nearest_median = median_of_medians(unsorted_array[first_index:last_index])
        index_of_nearest_median = get_index_of_nearest_median(unsorted_array, first_index, last_index, nearest_median)
    swap(unsorted_array, first_index, index_of_nearest_median)

    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1


def deterministic_select(array_list, left, right, k):
    """
    Search for the kth-smallest item
    :return:
    """
    split = partition(array_list, left, right)
    if split == k:
        return array_list[split]
    elif split < k:
        return deterministic_select(array_list, split + 1, right, k)
    else:
        return deterministic_select(array_list, left, split - 1, k)

def test_deterministic_select():
    inp = [([2,3,1,6,4,5,7],0,6,6),
           ([200,300,100], 0, 2, 2),
           ]
    out = [7,300]

    for i in range(len(inp)):
        test_res = deterministic_select(inp[i][0],inp[i][1],inp[i][2],inp[i][3])
        print('test_res:', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_deterministic_select()


