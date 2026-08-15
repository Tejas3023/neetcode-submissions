class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maxW = 0

        for i in range(len(heights)):

            while len(stack) > 0 and heights[i] < heights[stack[-1]]:

                eleindex = stack.pop()
                element = heights[eleindex]

                nse = i

                if len(stack) == 0:
                    pse = -1
                else:
                    pse = stack[-1]

                maxW = max(maxW, element * (nse - pse - 1))

            stack.append(i)

        while len(stack) > 0:

            eleindex = stack.pop()
            element = heights[eleindex]

            nse = len(heights)

            if len(stack) == 0:
                pse = -1
            else:
                pse = stack[-1]

            maxW = max(maxW, element * (nse - pse - 1))

        return maxW