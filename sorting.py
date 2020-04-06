# Collection of sorting algorithms
from typing import List, Tuple
import random


# Hoare partition scheme - doesn't work
# def partition(array: List[int], lo: int, hi: int) -> Tuple[List[int], int]:
#   # Select pivot value.
#   pivot_value = array[hi // 2]
#   i = lo
#   j = hi
#   while True:
#     # Find the next element of the array (from the front) greater than the pivot.
#     # TODO what pivot is the greatest?
#     while array[i] <= pivot_value:
#       i = i + 1
#     # Find the next element of the array (from the back) lesser than the pivot.
#     # TODO similar
#     while array[j] > pivot_value:
#       j = j - 1
#     if i >= j:
#       # Partitioned. Pivot at... j?
#       return array, j
#     # Swap the inverted values.
#     array[i], array[j] = array[j], array[i]
#
#
# def quicksort(array: List, lo: int, hi: int) -> List:
#   # If the partition to be sorted is of length 1, it's already sorted.
#   if hi <= lo:
#     return array
#
#   partitioned, p = partition(array, lo, hi)
#   sort_bottom = quicksort(partitioned, lo, p - 1)
#   sorted = quicksort(sort_bottom, p + 1, hi)
#   return sorted
#
#

# Quick sort with first element in array as pivot. Works.
class QuickSortPivotFirst(object):
  def __init__(self, array: List[int]):
    self.array = array

  def partition(self, lo: int, hi: int) -> int:
    # Select a pivot and a location to store the next value from the "lesser" set.
    pivot = lo
    swap_idx = lo + 1

    # Iterate through the list section specified
    for i in range(lo + 0, hi + 1):
      # ...arranging low values in a section right after pivot, and the high values right after that.
      if self.array[i] < self.array[pivot]:
        # Swap the first value of the high set (swap_idx) and the found value from the lesser set.
        self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        swap_idx += 1

    # Finally, swap the pivot and the last value from the low section
    sorted_pivot = swap_idx - 1
    self.array[pivot], self.array[sorted_pivot] = self.array[sorted_pivot], self.array[pivot]
    return sorted_pivot

  def quicksort(self, lo: int, hi: int) -> List:
    if (hi <= lo):
      return

    p = self.partition(lo, hi)
    self.quicksort(lo, p - 1)
    self.quicksort(p + 1, hi)

  def sorted(self):
    self.quicksort(0, len(self.array) - 1)
    return self.array


l = [random.randint(0, 10) for i in range(10)]
print(QuickSortPivotFirst(l).sorted())
