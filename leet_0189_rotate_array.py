'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

'''
def rotate_array(nums, k):
    for _ in range(k):
        nums.insert(0, nums.pop())


def rotate_array2(nums, k):
    temp_nums = nums.copy()
    for i in range(len(nums)):
        nums[(i+k) % (len(nums))] = temp_nums[i]


def rotate_array3(nums, k):
    for key, value in enumerate(nums.copy()):
        nums[(key + k) % len(nums)] = value

# this function fail if len(nums) < k
def rotate_array4(nums, k):
    stack = []
    for _ in range(k):
        stack.append(nums.pop())
    stack = stack[::-1]
    nums = stack + nums



nums1 = [1,2,3,4,5,6,7]
k = 3

# nums1 = [-1,-100,3,99]
# k = 2

print(rotate_array4(nums1, k))