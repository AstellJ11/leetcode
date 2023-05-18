Determine whether there are two numbers in the array that are the same value and their positions are less than or equal to k distance apart.
​
Method too slow:
​
for i in range(len(nums)):
for j in range(i+1, len(nums)):
if (nums[i] == nums[j]) & (abs(i-j) <= k) & (i != j):
return True