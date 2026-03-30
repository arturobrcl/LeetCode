class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for operation in operations:
            if operation == "X++" or operation == "++X":
                result += 1
            elif operation == "X--" or operation == "--X":
                result -= 1
        return result
