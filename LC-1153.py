class Solution(object):
    def canConvert(self, str1, str2):

        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2:
            return True
        letter = [''] * 26
        n = len(str1)
        for i in range(n):
            letter_i = ord(str1[i]) - ord('a')
            # if matched, but the matched char != current str2[i]: False
            if letter[letter_i] != '' and letter[letter_i] != str2[i]:
                return False
            letter[letter_i] = str2[i]
        return len(set(str2)) < 26
