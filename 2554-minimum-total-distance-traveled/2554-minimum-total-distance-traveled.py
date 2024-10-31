# class Solution:
#     def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
#         factory.sort()
#         robot.sort()

        
#         dp=[[0]*(len(factory)+1) for _ in range(len(robot)+1)]
#         for i in range(len(robot)+ 1):
#             dp[i][len(factory)] = 1e12  # No factories left
#         for i in range(len(robot)-1,-1,-1):
#             for j in range(len(factory)-1,-1,-1):
               
                
#                 curr=dp[i+1][j+1]+abs(factory[j][0]-robot[i])
#                 skip=dp[i][j+1]
#                 dp[i][j]=min(curr,skip)
#         return int(dp[0][0])
class Solution:
    def minimumTotalDistance(self, robot, factory):
        # Sort robots and factories by position
        robot.sort()
        factory.sort(key=lambda x: x[0])

        # Flatten factory positions according to their capacities
        factory_positions = []
        for f in factory:
            for _ in range(f[1]):
                factory_positions.append(f[0])

        robot_count, factory_count = len(robot), len(factory_positions)
        dp = [[0] * (factory_count + 1) for _ in range(robot_count + 1)]

        # Initialize base cases
        for i in range(robot_count):
            dp[i][factory_count] = 1e12  # No factories left

        # Fill DP table bottom-up
        for i in range(robot_count - 1, -1, -1):
            for j in range(factory_count - 1, -1, -1):
                # Option 1: Assign current robot to current factory
                assign = abs(robot[i] - factory_positions[j]) + dp[i + 1][j + 1]

                # Option 2: Skip current factory for the current robot
                skip = dp[i][j + 1]

                dp[i][j] = min(assign, skip)  # Take the minimum option

        # Minimum distance starting from first robot and factory
        return dp[0][0]  
        
