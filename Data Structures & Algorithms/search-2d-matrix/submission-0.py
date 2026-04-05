class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for array in matrix:
            if self.binarySearchArray(array, target):
                return True
        return False

    def binarySearchArray(self, array: List[int], target:int) -> bool:

        lower = 0
        upper = len(array) - 1

        while lower <= upper:
            guess = lower + (upper - lower ) // 2

            number = array[guess]

            if number == target:
                return True
            elif number < target:
                lower = guess + 1
            else:
                upper = guess - 1
        return False
        