#include <cassert>
#include <iostream>
#include <vector>

class Solution {
 public:
  std::vector<int> sortArray(std::vector<int>& nums) {
    std::vector<int> sorted = nums;
    mergeSort(sorted);
    return sorted;
  }

  void mergeSort(std::vector<int>& nums) {
    // Standard mergesort.
    // Base case. Arrays of length <=1 are already sorted.
    if (nums.size() < 2) {
      return;
    }

    // Nominal case. Divide into two sorted arrays.
    const int midpoint = nums.size() / 2;
    std::vector<int> L;
    std::vector<int> R;
    L.insert(L.begin(), nums.begin(), nums.begin() + midpoint);
    R.insert(R.begin(), nums.begin() + midpoint, nums.end());
    mergeSort(L);
    mergeSort(R);

    // Re-merge them in sorted order.
    auto L_it = L.begin();
    auto R_it = R.begin();
    auto nums_it = nums.begin();
    // Merge them until we reach the end of one.
    while (L_it != L.end() && R_it != R.end()) {
      if (*L_it < *R_it) {
        *nums_it = *L_it;
        nums_it++;
        L_it++;
      } else {
        *nums_it = *R_it;
        nums_it++;
        R_it++;
      }
    }

    // Merge the remaining tail (of one).
    while (L_it != L.end()) {
      *nums_it = *L_it;
      nums_it++;
      L_it++;
    }
    while (R_it != R.end()) {
      *nums_it = *R_it;
      nums_it++;
      R_it++;
    }

    // We should have gone through the entire array nums. Let's double-check.
    assert(static_cast<size_t>(std::distance(nums.begin(), nums_it)) == nums.size());
  }
};

int main() {
  std::vector<int> unsorted = {1, 6, 8, 3, 2, 5, 5, 5, 100, -5};
  Solution s;
  const auto sorted = s.sortArray(unsorted);
  for (const auto& elem : sorted) {
    std::cout << elem << ", ";
  }
  std::cout << std::endl;
  return 0;
}
