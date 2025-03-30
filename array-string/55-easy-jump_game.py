# Leetcode 55: Jump Game
# Link: https://leetcode.com/problems/jump-game/

def canJump(nums: list[int]) -> bool:
    # Keep track of the furthest index we can reach
    max_reach = 0
    
    # Iterate through array up to the furthest reachable position
    for i in range(len(nums)):
        # If current position is beyond our max reach, we can't get here
        if i > max_reach:
            return False
            
        # Update max_reach if current position + jump length is further
        max_reach = max(max_reach, i + nums[i])
        
        # If we can reach the last index, return True
        if max_reach >= len(nums) - 1:
            return True
            
    return True


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
