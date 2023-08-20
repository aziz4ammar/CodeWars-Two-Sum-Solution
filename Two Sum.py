def two_sum(nums, target):
    num_indices = {}  # A dictionary to store number-to-index mapping
    
    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in num_indices:
            return [num_indices[complement], index]  # Return indices of the two numbers
        
        num_indices[num] = index  # Store current number and its index
    
    return None  # Return None if no solution is found

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output should be [0, 1] since nums[0] + nums[1] = 2 + 7 = 9