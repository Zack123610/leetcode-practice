# Leetcode 45: Jump Game II
# Link: https://leetcode.com/problems/jump-game-ii/ 

def jump(nums: list[int]) -> int:
    # Keep track of the furthest index we can reach
    max_reach = 0
    
    # Keep track of the number of jumps
    jumps = 0
    
    # Keep track of the current position
    current = 0
    
    # We don't need to check the last position
    for i in range(len(nums) - 1):
        # Update the furthest we can reach
        max_reach = max(max_reach, i + nums[i])
        
        # If we've reached the current position, we need to jump
        if i == current:
            jumps += 1
            current = max_reach
            
            # If we can reach or exceed the last index, we're done
            if max_reach >= len(nums) - 1:
                break
    
    return jumps

# Example usage:
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [2,3,1,1,4],  # Output: 2
        [2,3,0,1,4],  # Output: 2
        [1,2,3],      # Output: 2
    ]
    
    for nums in test_cases:
        print(f"Input: {nums}")
        print(f"Output: {jump(nums)}\n")
    