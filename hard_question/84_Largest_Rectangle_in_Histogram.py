class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Return the area of the largest rectangle in the histogram
        
        1. 
        Consider every pair of bars and find the area of the rectangle between them using the height of the shortest bar lying between them 
        """
        
        #Brute Force 1
        """
        maxArea = 0
        for l in range(len(heights)):
            for r in range(l, len(heights)):
                minBar = min(heights[l:r+1])
                area = (r-l+1)*minBar
                maxArea = max(maxArea, area)
        return maxArea
        """
        
        #Brute Force 2
        """
        Instead of taking every possible pair and then finding the bar of minimum height lying between them, we can find the bar of minimum height for current pair by using the minimum heigh bar of the pevious pair 
        """ 
        """
        maxArea = 0
        for l in range(len(heights)):
            minBar = inf
            for r in range(l, len(heights)):
                minBar = min(minBar, heights[r])
                area = (r-l+1)*minBar
                maxArea = max(maxArea, area)
        return maxArea
    
        #Brute Force 3
        """
        """
        This approach relies on the observation that the rectangle with the maximum area will be the maximum of
        1. The widest possible rectange with height ewual to the height of the shortest bar
        2. The largest rectangle confined to the left of the shortest bar
        3. The largest rectangle confined to teh right of the shoftest bar
        
        [6, 4, 5, 2, 4, 3, 9]
        
        Shortest bar is of height 2. 
        The are of the widest rectange using this bar as height is 2x7=14. Now, we need to looks for cases 2 and 3 mentioned above. Thus we repat the same process to the left and right of 2. In the left of 2, 4 is the minimum, forming an area of rectangel 4x3 = 12. Fither, rectanges of area 6x1=1 and 5x1 = 5 exist to the left and right respectively. Similar we find the area of 3x3= 9, 4x1=4 and 9x1 = 9 to the left of 2. Thus, we get 14 as the correct maximum area. 
        
        1. Find shortest bar and its index
        2. Find area with shortest
        3. Call function recursively
        """
        #Divide and conquer
        """
        def helper(l, r): # return rectangle with max area
            if r <= l:
                return 0
            if r-l == 1:
                return heights[l]
            
            minBar = min(heights[l:r])
            indMinBar = heights[l:r].index(minBar) + l
            
            includeMin = (r-l)*minBar
            leftOfMin = helper(l, indMinBar)
            rightOfMin = helper(indMinBar+1, r)
            return max(includeMin, leftOfMin, rightOfMin)
        
        return helper(0, len(heights))
        """
        
        """
        You can obeserve in the divide and conquer, we gain the advantage, Wont gain much advantage if the array is sorted. We can use a segment tree to fin dthe minimum time in O(logn)
        
        """
        """
        Using a stack. Initially we push a -1 onto the stack to mark the end. We start withthe left most bar and keep pushing the ucrrent bar's index onto the stack until we get two successive numbers in descending order, we want heights[i] < heights[i-1]. Now we start popping the numbers from the stack until we hit a number stack[j] on the stack such as heights[stack[j]] <= heights[i]. Everytime we pop, we find the area of the rectangel formed using the current element as the height of the rectanve and the dfference ebetween the current element's index pointet to in the original array and the elemtn stack[top-1] -1 as the widht. if we pop an element stack[top] and i is the current index to which we are pointint ins the original array 
        """
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)
            

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea