def checkNums(nums, max):
    for n in nums:
        if n < max: return False

    return True

class Solution:
    def minMoves(self, nums: List[int]) -> int:

        maxNum = max(nums)
        moves = 0

        while not checkNums(nums, maxNum):

            for i in range (len(nums)):
                if nums[i] < maxNum:
                    nums[i] = nums[i] + 1
                    moves += 1


        return moves