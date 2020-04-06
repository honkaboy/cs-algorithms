# Collection of sorting algorithms
from typing import List, Tuple


def qsort(array: List) -> List:
  def partition(array: List[int], lo: int, hi: int) -> Tuple[List[int], int]:
    # Select pivot value.
    pivot_value = array[hi // 2]
    i = lo
    j = hi
      for _ in range(hi - low):  # Can't do it more than N times?
        # Find the next element of the array (from the front) greater than the pivot.
        # TODO what pivot is the greatest?
        while array[i] <= pivot_value and i < j:
          i = i + 1
        # Find the next element of the array (from the back) lesser than the pivot.
        # TODO similar
        while array[j] >= pivot_value and j > i:
          j = j - 1
        if i >= j:
          # Partitioned. Pivot at... j?
          return array, j
        else:
          # Swap the inverted values.
          array[i], array[j] = array[j], array[i]

  def quicksort(array: List, lo: int, hi: int) -> List:
    partitioned, p = partition(array, lo, hi)
    sort_bottom = quicksort(partitioned, lo, p-1)
    sorted = quicksort(sort_bottom, p+1, hi)
    return sorted

l = [3,6,2,7,1]
ls = quicksort(l)
print(ls)
