# Min Deletions to Make Frequency of Each Letter Unique
# Given a string s consisting of n lowercase letters, you have to delete the minimum number of characters from s so that every letter in s appears a unique number of times. We only care about the occurrences of letters that appear at least once in result.

# Example 1:

# Input: "eeeeffff"
# Output: 1
# Explanation: We can delete one occurence of 'e' or one occurence of 'f'. Then one letter will occur four times and the other three times.

# Example 2:

# Input: "aabbffddeaee"
# Output: 6
# Explanation: For example, we can delete all occurences of 'e' and 'f' and one occurence of 'd' to obtain the word "aabbda". Note that both 'e' and 'f' will occur zero times in the new word, but that's fine, since we only care about the letter that appear at least once.

# Example 3:

# Input: "llll"
# Output: 0
# Explanation: There is no need to delete any character.

# Example 4:

# Input: "example"
# Output: 4

import numpy


class SolutionNotOptimal:
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


class Solution:
    def __init__(self):
        self.decrement_count = 0

    # O(n)
    def build_freq_dictionary(self, s):
        store = {}

        for char in s:
            store[char] = store.get(char, 0) + 1

        return store

    # O(n)
    def compute_deletions(self, frequency_list: list):
        # max_freq = max(map(lambda x: x[1], frequency_list))
        deletions = 0

        for i, (key, value) in enumerate(frequency_list):
            next_item = None
            if (i + 1) < len(frequency_list):
                next_item = frequency_list[i + 1]

            # Since this is sorted, we can compare with the next item of the list
            if next_item is not None:
                if value == next_item[1]:
                    # Decrease 1 from the next value
                    deletions += 1
                    # Leave it 1 less than the current one
                    frequency_list[i + 1] = (next_item[0], next_item[1] - 1)
                elif value < next_item[1]:
                    diff = (next_item[1] - value)
                    next_val = max((value - 1), 0)
                    deletions += next_item[1] - next_val
                    frequency_list[i + 1] = (next_item[0], next_val)
                else:
                    # values is 0?
                    # do nothin?
                    pass

        return deletions

    def minDeletions(self, s: str) -> int:
        freq_dict = self.build_freq_dictionary(s)

        # Create a list of frequencies
        list_freqs = list(map(lambda k: (k, freq_dict[k]), freq_dict.keys()))
        list_freqs.sort(key=lambda tup: tup[1], reverse=True)

        return self.compute_deletions(list_freqs)


try:
    print(Solution().minDeletions("aab"))
    assert Solution().minDeletions("aab") == 0

    # print(Solution().minDeletions("bbcebab"))
    # print(Solution().minDeletions("accdcdadddbaadbc"))

    print(Solution().minDeletions("abcabc"))
    assert Solution().minDeletions("abcabc") == 3

    print(Solution().minDeletions(
        "abcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwz"
    ))

    assert Solution().minDeletions(
        "abcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwz"
    ) == 276
except AssertionError as e:
    print("Assertion error")
