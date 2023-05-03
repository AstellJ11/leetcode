class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Use a slice that steps backwards
        palindrome = str(x)[::-1]

        if palindrome == str(x):
            return True
        else:
            return False