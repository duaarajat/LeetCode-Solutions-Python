"""Given an integer array nums, return the third distinct maximum number in this array. If the
third maximum does not exist, return the maximum number."""

# Take input from the user
ip = input("Enter the array elements separated by spaces: ")
array = list(map(int, ip.strip().split()))

# Remove duplicates
nums = list(set(array))

# Sort in descending order
nums.sort(reverse=True)

# Return third max if it exists, else return the maximum
if len(nums) >= 3:
    print("Output:", nums[2])
else:
    print("Output:", nums[0])
