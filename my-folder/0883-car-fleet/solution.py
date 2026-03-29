class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
         
        cars = [] # array of tuple(position, speed)
        for index in range(len(position)):
            cars.append((position[index], speed[index]))
        
        cars.sort(key=lambda x: x[0])

        stack = []

        for index in range(len(cars) - 1, -1, -1):
            position1, speed1 = cars[index] # new car
            if stack:
                position2, speed2 = stack[-1] # car on stack

                if (target - position1) / speed1 > (target - position2) / speed2:
                    stack.append((position1, speed1))
            else:
                stack.append((position1, speed1))

        return len(stack)

