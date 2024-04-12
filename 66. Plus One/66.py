class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        digits = digits[::-1]
        if digits[0] != 9:
            digits[0] += 1
        else:
            t = 0
            for i in range(1, l):
                if digits[i] != 9:
                    break
                t += 1
            if t == l-1:
                digits.append(0)
            for i in range(0, t + 1):
                digits[i] = 0
            digits[t + 1] += 1
        return digits[::-1]