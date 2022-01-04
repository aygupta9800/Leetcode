class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        word = "apple"
        abbr ="a2e"
        We maintain two pointers, i pointing at word and j pointing at abbr.
        There are only two scenarios:

        j points to a letter. We compare the value i and j points to. If equal, we increment them. Otherwise, return False.
        j points to a digit. We need to find out the complete number that j is pointing to, e.g. 123. Then we would increment i by 123. We know that next we will:
        either break out of the while loop if i or j is too large
        or we will return to scenario 1.
        """
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == "0":
                    return False
                digit = ""
                while j< len(abbr) and abbr[j].isdigit():
                    digit += abbr[j]
                    j += 1
                i = i + int(digit)
        return i == len(word) and j == len(abbr)

                