#include <cassert>
#include <iostream>
#include <vector>

class MaxHeap {
 public:
  MaxHeap(const std::vector<int>& nums) {
    for (const int elem : nums) {
      Insert(elem);
    }
  }

  void Insert(const int elem) {
    // Add to back of heap.
    storage_.push_back(elem);

    size_t idx = storage_.size() - 1;
    while (idx != 0) {
      size_t parent_idx = Parent(idx);
      if (storage_[parent_idx] < storage_[idx]) {
        std::swap(storage_[parent_idx], storage_[idx]);
      }
      idx = parent_idx;
    }
  }

  int DeleteMax() {
    int max = storage_[0];
    std::swap(storage_.back(), storage_[0]);
    storage_.resize(storage_.size() - 1);

    size_t bubble_idx = 0;
    while (LeftChild(bubble_idx) < storage_.size()) {
      const size_t left_child = LeftChild(bubble_idx);
      const size_t right_child = RightChild(bubble_idx);
      // Does the left child exist?
      if (left_child < storage_.size()) {
        size_t greater_child = left_child;
        // Does the right child exist?
        if (right_child < storage_.size()) {
          greater_child =
              storage_[right_child] > storage_[left_child] ? right_child : left_child;
        }
        // Swap with the greater child.
        if (storage_[greater_child] > storage_[bubble_idx]) {
          std::swap(storage_[greater_child], storage_[bubble_idx]);
          bubble_idx = greater_child;
        } else {
          break;
        }
      }
    }

    return max;
  }

  size_t Parent(const size_t idx) { return (idx - 1) / 2; }
  size_t LeftChild(const size_t idx) { return idx * 2 + 1; }
  size_t RightChild(const size_t idx) { return idx * 2 + 2; }

 private:
  std::vector<int> storage_;
};

int main() {
  std::vector<int> unsorted = {1, 6, 8, 3, 2, 5, 5, 5, 100, -5};
  MaxHeap s(unsorted);
  for (size_t i = 0; i < unsorted.size(); ++i) {
    std::cout << s.DeleteMax() << ", ";
  }
  std::cout << std::endl;
  return 0;
}
