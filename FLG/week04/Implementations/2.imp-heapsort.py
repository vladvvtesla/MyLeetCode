"""
Sedgewich w4 - HeapSort

Basic Plan for heapsort
1) start with array of keys in arbitrary order
2) build a max-heap with all N keys (in place)
3) repeatedly remove the maximum key


Heap sort
1. heap construction
First pass: Build heap using bottom-up method
for k in range(1, k//2, -1)
    sink(a, k, N)

Second pass:
 - remove the maximum, one at a time
 - leave in array, instead of nulling out
while n > 1:
    a[1],a[-1] = a[-1],a[1]
    sink(a, k, N)

class heap():
    def sort(pq)
        n = len(pq)
        for k in range(1, k//2, -1)
            sink(a, k, N)
        while n > 1:
            a[1],a[-1] = a[-1],a[1]
            sink(a, k, N)


mathematical analysis
Proposition: Heap construction uses <= 2N compares and exchanges
Proposition: Heapsort uses <= 2 N lg N compares and exchanges

Significance: In-place sorting algorithm with N log N worth case
Mergesort: no, linear extra space
Quicksort: no, quadratic time in worth case
Heapsort: yes!

Bottom line: Heap sort is optimal for both time and space, but
 - inner loop longer than quicksort's
 - makes poor use of cache memory
 - not stable

"""