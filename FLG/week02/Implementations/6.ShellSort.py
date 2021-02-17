"""
Idea. Move entries more than one position at a time by h-sorting the array

an h-sorted array is h interleaved sorted ubsequences

1. The worst case number of compares used by shellsort with the 3x + 1 increments id O (N ^ 3/2)

Time complexity: O (N ^ 3/2), close to O (N * LogN)

"""
def shell_sort(arr):
    """ Insertion Sort implementation"""
    n = len(arr)
    gap = n//3


    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

                # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2


def test_shell_sort():
    a = [6,2,9,2,5]
    a_sorted = [2,2,5,6,9]
    shell_sort(a)
    print("1.", "OK" if a == a_sorted else "Failed")

    b = [1,0,0,0,0]
    b_sorted = [0,0,0,0,1]
    shell_sort(b)
    print("2.", "OK" if b == b_sorted else "Failed")


if __name__ == '__main__':
    test_shell_sort()
