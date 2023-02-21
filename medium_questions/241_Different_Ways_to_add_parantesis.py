class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        result = []
        if '+' not in input and '-' not in input and '*' not in input:
            result.append(int(input))
        else:
            for i in range(0, len(input)):
                char = input[i]
                if not char.isdigit():
                    leftParts = self.diffWaysToCompute(input[0:i])
                    rightParts = self.diffWaysToCompute(input[i+1:])
                    for part1 in leftParts:
                        for part2 in rightParts:
                            if char == '+':
                                result.append(part1 + part2)
                            elif char == '-':
                                result.append(part1-part2)
                            elif char == '*':
                                result.append(part1 * part2)
        return result