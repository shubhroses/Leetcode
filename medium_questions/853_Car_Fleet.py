class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        target = 12
        position =  [10, 8, 0, 5, 3]
        speed =     [2,  4, 1, 1, 3]

        Want to determine is two cars will intersect before reaching the target 

        timeToReach=[1, 1, 12, 7, 3]
        time to reach = (target - position)/speed

        there is going to be a collision if a car behind another car takes less time to reach 

        position =  [10, 8, 5, 3, 0]
        speed =     [ 2, 4, 1, 3, 1]
        timeToReach=[ 1, 1, 7, 3, 12]
                               i

        stack=[1, 7, 12]

        sort position and speed by position decreasing
        if nothing in stack push, 
        while time to reach of current car is <= time to reach of top of stack 
        pop from stack 
        else push onto the stack 
        return len of stack 

        target = 100
                           i
        position =  [4, 2, 0] 
        speed =     [1, 2, 4]
        timetoReach=[96, 48, 25]

        stack = [(0, 25)]

        target = 10
        position =      [3]
        speed =         [3]
        timetoreach =   [2.3333]

        stack = [(3, 2.333)]


        target: 100
                            i
        position =  [50, 2, 0]
        speed =     [1, 1, 4]
        timeToReach=[50,98,25]

        stack = [50, 98]

        dont push onto the stack if the top of the stack is larger than the current time to reach 
        """

        # Sort the position and speed by the position in decreasing order
        posSpeed = [(position[i], speed[i]) for i in range(len(position))]
        posSpeed.sort(reverse = True)

        def timeToReach(pos, spd):
            return (target - pos)/spd
        
        stack = []
        for p, s in posSpeed:
            tToR = timeToReach(p, s)
            if not stack:
                stack.append(tToR)
            else:
                top = stack[-1]
                if top < tToR:
                    stack.append(tToR)
        return len(stack)