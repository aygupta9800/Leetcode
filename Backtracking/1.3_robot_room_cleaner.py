# PS: You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

# The robot starts at an unknown location in the root that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.

# You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.


# Time complexity : O(N−M), where NN is a number of cells in the room and MM is a number of obstacles.
# We visit each non-obstacle cell once and only once.
# At each visit, we will check 4 directions around the cell. Therefore, the total number of operations would be 4.(N−M).

# Space complexity : O(N−M), where NN is a number of cells in the room and MM is a number of obstacles
# We employed a hashtable to keep track of whether a non-obstacle cell is visited or not.


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def backtrack(cell=(0,0), d =0):
            visited.add(cell)
            robot.clean()
            
            #going clockwise 0:up, 1: right, 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d+i) % 4
                new_cell = (cell[0] +directions[new_d][0], \
                            cell[1] +directions[new_d][1])
                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                
                #turn the robot following the chosen direction: cloclwise
                robot.turnRight()
                
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()
        
