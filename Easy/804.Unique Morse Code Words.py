# class Solution:
#     def uniqueMorseRepresentations(self, words):
#         morse_dict = {"a": ".-", "b": "-...", "c": "-.-.",
#                       "d": "-..", "e": ".", "f": "..-.",
#                       "g": "--.", "h": "....", "i": "..",
#                       "j": ".---", "k": "-.-", "l": ".-..",
#                       "m": "--", "n": "-.", "o": "---", "p": ".--.",
#                       "q": "--.-", "r": ".-.", "s": "...", "t": "-",
#                       "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
#                       "y": "-.--", "z": "--.."}
#         s = set()
#         for word in words:
#             new_word = ""
#             for w in word:
#                 new_word += morse_dict[w]
#             s.add(new_word)
#         return len(s)


import string


class Solution:
    def uniqueMorseRepresentations(self, words):
        morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.",
                      "--.", "....", "..", ".---", "-.-", ".-..",
                      "--", "-.", "---", ".--.", "--.-", ".-.",
                      "...", "-", "..-", "...-", ".--", "-..-",
                      "-.--", "--.."]

        alphabet = string.ascii_lowercase
        s = set()
        for word in words:
            temp = ""
            for w in word:
                temp += morse_list[alphabet.index(w)]
            s.add(temp)
        return len(s)


words_list = ["gin", "zen", "gig", "msg"]
print(Solution().uniqueMorseRepresentations(words_list))
