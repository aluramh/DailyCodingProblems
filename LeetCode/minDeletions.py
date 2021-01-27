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
        cutoff_freq = max(map(lambda x: x[1], frequency_list))
        deletions = 0

        for i, (key, value) in frequency_list.val
            if value > cutoff_freq:
                # Calculate the diff and add it to the deletion count
                diff = value - cutoff_freq
                deletions = deletions + diff
                # Reduce 1 from the max freq
                cutoff_freq = max((cutoff_freq - 1), 0)

            elif value == cutoff_freq:
                # Reduce 1 from the max freq
                cutoff_freq = max((cutoff_freq - 1), 0)

            elif value < cutoff_freq:
                # Level the cutoff freq to the largest number right now, minus 1 for the next iter
                cutoff_freq = max((value - 1), 0)

            elif value <= 0:
                pass

        return deletions

    def minDeletions(self, s: str) -> int:
        freq_dict = self.build_freq_dictionary(s)

        # Create a list of frequencies
        list_freqs = list(map(lambda k: (k, freq_dict[k]), freq_dict.keys()))
        list_freqs.sort(key=lambda tup: tup[1], reverse=True)

        return self.compute_deletions(list_freqs)


try:
    tests = [
        ("bbcebab", 2),
        ("accdcdadddbaadbc", 1),
        ("aab", 0),
        ("abcabc", 3),
        ("abcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwz",
         276),
    ]

    for s, expected_val in tests:
        result = Solution().minDeletions(s)
        print(result)
        assert result == expected_val

except AssertionError as e:
    print("Assertion error")
