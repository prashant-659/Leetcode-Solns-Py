class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # maxArea = 0
        # stack = []  # pair: (index, height)

        # for i, h in enumerate(heights):
        #     start = i
        #     while stack and stack[-1][1] > h:
        #         index, height = stack.pop()
        #         maxArea = max(maxArea, height * (i - index))
        #         start = index
        #     stack.append((start, h))

        # for i, h in stack:
        #     maxArea = max(maxArea, h * (len(heights) - i))
        # return maxArea

        #NSL
        stack=[]
        left=[]
        n=len(heights)
        for i in range(n):
            if len(stack)==0:
                left.append(-1)
            elif len(stack)>0 and heights[stack[-1]]<heights[i]:
                left.append(stack[-1])
            elif len(stack)>0 and heights[stack[-1]]>=heights[i]:
                while len(stack)>0 and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if len(stack)==0:
                    left.append(-1)
                else:
                    left.append(stack[-1])
            stack.append(i)
        

        #NSR
        right=[]
        stack=[]
        for i in range(n-1,-1,-1):
            if len(stack)==0:
                right.append(len(heights))
            elif len(stack)>0 and heights[stack[-1]]<heights[i]:
                right.append(stack[-1])
            elif len(stack)>0 and heights[stack[-1]]>=heights[i]:
                while len(stack)>0 and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if len(stack)==0:
                    right.append(len(heights))
                else:
                    right.append(stack[-1])
            stack.append(i)
        right=right[::-1]
        width=[]
        for i in range(len(left)):
            width.append(right[i]-left[i]-1)
        
        area = [i[0] * i[1] for i in zip(heights, width)]
        return max(area)


