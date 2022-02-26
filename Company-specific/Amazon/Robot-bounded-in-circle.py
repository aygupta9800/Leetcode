# "G": go straight 1 unit.
# "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
# "R": turn 90 degrees to the right (i.e., clockwise direction).
# Return true if and only if there exists a circle in the plane such that the
# robot never leaves the circle.

# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
# "G": move one step. Position: (0, 1). Direction: South.
# "G": move one step. Position: (0, 0). Direction: South.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
# Based on that, we return true.


# time: O(N), space: O(1)
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY = 0, 1 #dir vector
        x, y = 0, 0 #initial pos

        for d in instructions:
            if d == 'G':
                x, y = x+dirX, y+dirY
            elif d == 'L':
                dirX, dirY = -1 * dirY, dirX
            else:
                dirX, dirY = dirY, -1 * dirX

        #Two ways to check if circle
        # 1. repeat instruction 4 times and see if it returns to 0,0
        # 2. (after 1 instruction=> returns to 0rigin or (dir change) )

        return (x,y) == (0,0) or (dirX, dirY) != (0, 1)
        