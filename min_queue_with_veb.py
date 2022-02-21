# min_queue structure with : one queue and one Van Emde Boas Tree
# enqueue time O(log log M)
# dequeue time O(log log M)
# find_min O(1)

from queue import Queue
from veb import vEBTree

# M = 2^m is the maximum number of elements that can be stored in the tree. The M is not to be confused with the actual
# number of elements stored in the tree, by which the performance of other tree data-structures is often measured
# m = bit count

# VEB_UNIVERSE_SIZE should be greater than the number of element size in the queue
VEB_UNIVERSE_SIZE = 2**15


class MinQueue(Queue):
    def __init__(self):
        super().__init__()
        self._veb_tree = vEBTree.of_size(VEB_UNIVERSE_SIZE)
        self._count_numbers = {}

    def get(self, **kwargs) -> int:
        value = super().get(**kwargs)  # O(1)
        self._veb_tree.discard(value)  # O(log log M)
        self._count_numbers[value] -= 1
        if self._count_numbers[value] != 0:
            self._veb_tree.add(value)  # O(log log M)
        return value

    def put(self, value: int, **kwargs):
        self._veb_tree.add(value)  # O(log log M)
        if value in self._count_numbers:
            self._count_numbers[value] += 1
        else:
            self._count_numbers[value] = 1
        super().put(value, **kwargs)  # O(1)

    def find_min(self) -> int:
        min_item = self._veb_tree.min  # O(1)
        return min_item

    def __str__(self):
        rep_list = []
        for _ in range(self.qsize()):
            value = super().get()
            rep_list.append(value)
            super().put(value)
        return str(rep_list)


if __name__ == "__main__":
    from numpy.random import choice
    import time
    import math

    min_queue = MinQueue()
    t_number_elems = int(1e5)

    in_arr = choice(t_number_elems, t_number_elems)

    print(f"O(log log M) : {math.log2(math.log2(VEB_UNIVERSE_SIZE))}")

    start_time = time.time()
    [min_queue.put(value) for value in in_arr]
    print(f"enqueue time for {t_number_elems} elements : {time.time() - start_time} ")

    start_time = time.time()
    [min_queue.find_min() for _ in in_arr]
    print(f"find min time for {t_number_elems} tries : {time.time() - start_time} ")

    start_time = time.time()
    [min_queue.get() for _ in in_arr]
    print(f"dequeue time for {t_number_elems} tries : {time.time() - start_time} ")
