import numpy


class Solution:
    def __init__(self):
        self.decrement_count = 0

    # O(n)
    def build_dictionary(self, s):
        store = {}

        for char in s:
            store[char] = store.get(char, 0) + 1

        return store

    def set_correctly(self, key, value):
        has_been_set = False

        while has_been_set is False:
            # If freq in frequencies array is not taken, then store the key there
            if self.frequencies[value] == 0:
                self.frequencies[value] = key
                has_been_set = True
            elif value != 0:
                value -= 1
                self.decrement_count += 1
            else:
                has_been_set = True

    # O(n)
    def compute_deletion(self, store):

        for key, value in dict.items(store):
            self.set_correctly(key, value)

        return self.frequencies

    def minDeletions(self, s: str) -> int:
        freq_dict = self.build_dictionary(s)

        # Based on the frequency dictionary, build the frequencies array
        max_freq = max(dict.values(freq_dict))
        self.frequencies = list(numpy.zeros(max_freq + 1, dtype=int))

        self.compute_deletion(freq_dict)
        return self.decrement_count


# print(Solution().minDeletions("aab"))
# print(Solution().minDeletions("accdcdadddbaadbc"))
# print(Solution().minDeletions("bbcebab"))
print(Solution().minDeletions(
    "abcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwz"
))
