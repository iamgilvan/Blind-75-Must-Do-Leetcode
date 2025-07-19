from collections import defaultdict
from typing import OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.key_to_val_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        val, freq = self.key_to_val_freq[key]
        # Remove da freq atual
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        # Adiciona na nova freq
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_val_freq[key] = (val, freq + 1)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self.get(key)  # incrementa freq
            return

        if self.size == self.capacity:
            # Remove o LFU + LRU
            k, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[k]
            self.size -= 1

        # Adiciona novo
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
        self.size += 1

lfu = LFUCache(2)
lfu.put(1, 1)       # cache = {1=1}
lfu.put(2, 2)       # cache = {1=1, 2=2}
lfu.get(1)          # retorna 1, freq: 1=2, 2=1
lfu.put(3, 3)       # remove 2 (menos frequente), cache = {1=1, 3=3}
lfu.get(2)          # retorna -1 (2 foi removido)
lfu.get(3)          # retorna 3, freq: 3=2
lfu.get(1)          # retorna 1, freq: 1=3
lfu.put(4, 4)       # remove 3 (freq 2), cache = {1=1, 4=4}