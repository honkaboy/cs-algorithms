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
    self.array = array.copy()

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


class MergeSort(object):
  def __init__(self, array: List[int]):
    self.array = array.copy()

  def sorted(self):
    self.mergesort(0, len(self.array) - 1)
    return self.array

  def mergesort(self, lo, hi):
    # Split a list into two lists.
    split = lo + (hi - lo) // 2

    # For the base case (list of length 1), do nothing (list is already sorted).
    if (hi - lo) < 1:
      return

    # Sort the first.
    self.mergesort(lo, split)
    # Sort the second.
    self.mergesort(split + 1, hi)
    # Merge them.
    self.merge(lo, split, hi)

  def merge(self, lo1, hi1, hi2):
    lo2 = hi1 + 1  # Assume lists are contiguous in memory.
    # Indices we're currently examining.
    idx1 = lo1
    idx2 = lo2
    # Place to write the output before copying back to the original array.
    size_write_array = hi2 - lo1 + 1
    write_array = []
    for i in range(size_write_array):
      if idx1 <= hi1 and idx2 <= hi2:
        if self.array[idx1] < self.array[idx2]:
          write_array.append(self.array[idx1])
          idx1 += 1
        else:
          write_array.append(self.array[idx2])
          idx2 += 1
      else:
        if idx1 <= hi1:
          write_array.append(self.array[idx1])
          idx1 += 1
        else:
          write_array.append(self.array[idx2])
          idx2 += 1

    # Copy back to original array.
    assert(len(write_array) == (hi1 - lo1 + 1 + hi2 - lo2 + 1))
    assert(len(write_array) == hi2 - lo1 + 1)
    self.array[lo1:hi2 + 1] = write_array

    return


for i in range(100):
  l = [random.randint(0, 10) for i in range(10)]
  a = QuickSortPivotFirst(l).sorted()
  b = MergeSort(l).sorted()
  assert(a == b)
