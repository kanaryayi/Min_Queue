# min_queue structure with : one queue and one skip list
# enqueue time O(logn)
# dequeue time O(logn)
# find_min O(logn)

from queue import Queue
from pyskiplist import SkipList


class MinQueue(Queue):
    def __init__(self):
        super().__init__()
        self.skip_list = SkipList()

    def get(self, **kwargs) -> int:
        item = super().get(**kwargs)  # O(1)
        self.skip_list.remove(key=item)  # O(logn)
        return item

    def put(self, item: int, **kwargs):
        self.skip_list.insert(item, item)  # insert by the key as the item value # O(logn)
        super().put(item, **kwargs)  # O(1)

    def find_min(self) -> int:
        min_item = self.skip_list.popitem()  # O(logn)
        self.skip_list.insert(*min_item)  # O(logn)
        return min_item[0]

    def __str__(self):
        rep_list = []
        for _ in range(self.qsize()):
            item = super().get()
            rep_list.append(item)
            super().put(item)
        return str(rep_list)


if __name__ == "__main__":
    from numpy.random import choice
    import time
    import math

    min_queue = MinQueue()
    t_number_elems = int(1e5)

    in_arr = choice(t_number_elems, t_number_elems)

    print(f"O(log N) : {(math.log2(t_number_elems))}")

    start_time = time.time()
    [min_queue.put(value) for value in in_arr]
    print(f"enqueue time for {t_number_elems} elements : {time.time() - start_time} ")

    start_time = time.time()
    [min_queue.find_min() for _ in in_arr]
    print(f"find min time for {t_number_elems} tries : {time.time() - start_time} ")

    start_time = time.time()
    [min_queue.get() for _ in in_arr]
    print(f"dequeue time for {t_number_elems} tries : {time.time() - start_time} ")
