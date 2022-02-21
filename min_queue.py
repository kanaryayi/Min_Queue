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
    in_array = [3, 6, 7, 1, 12, 4, 5, 5, 5, 4, 2, 10, 2]
    min_queue = MinQueue()
    list(map(min_queue.put, in_array))
    min_queue.get()
    min_queue.get()
    min_queue.get()
    print(min_queue.find_min())
    min_queue.get()
    print(min_queue)
    min_queue.get()
    print(min_queue.find_min())
