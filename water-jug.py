from collections import deque
import queue
#further to solve water jog problem using
def water_jug(capacity1,capacity2,target):
    visited=set()
    queue=deque()

#initial state: both jugs are empty
queue.append((0,0,[]))

while queue:
    jug1, jug2,path=queue.popleft()

    #skip if the state has already been
    if (jug1,jug2) in visited:
        continue

    visited.add((jug1,jug2))

    #Add current state to the path
    path=path + [(jug1,jug2)]

    #Check if target is reached
    if jug1 == target or jug2 == target:
        returnpath

    #Generate all possible next states
    next_states= [
        #fill jug 1
        (capacity1,jug2),

        #fill jug 2
        (jug1,capacity2),

        #Empty jug 1
        (0,jug2),

        #Empty jug 2
        (jug1, 0),

        #pour jug1 -> jug2
        (
            jug1 - min(jug1, capacity2- jug2),
            jug2 + min(jug1, capacity2 - jug2)
        ),

        #pour jug2 -> jug1
        (
            jug1 + min(jug2, capacity1-jug1),
            jug2 + min(jug2, capacity1-jug1)
        )
    ]

    # Add unvisited states to the queue
    for state in next_states:
        if state not in visited:
            queue.append((state[0],state[1],path))

#No solution found
# return None

#Main program
jug1= int(input("Enter capacity of jug1: "))
jug2= int(input("Enter capacity of jug2: "))
target= int(input("Enter target amount: "))

solution = water_jug(jug1, jug2, target)

if solution:
    print("\nSteps to reach the target: ")

    for step in solution:
        print(step)

else:
    print("No solution exists.")
from collections import deque
#further to solve water jog problem using
def water_jug(capacity1,capacity2,target):
    visited=set()
    queue=deque()

    #initial state: both jugs are empty
    queue.append((0,0,[]))

    while queue:
        jug1, jug2,path=queue.popleft()

        #skip if the state has already been
        if (jug1,jug2) in visited:
            continue

        visited.add((jug1,jug2))

        #Add current state to the path
        path=path + [(jug1,jug2)]

        #Check if target is reached
        if jug1 == target or jug2 == target:
            return path

        #Generate all possible next states
        next_states= [
            #fill jug 1
            (capacity1,jug2),

            #fill jug 2
            (jug1,capacity2),

            #Empty jug 1
            (0,jug2),

            #Empty jug 2
            (jug1, 0),

            #pour jug1 -> jug2
            (
                jug1 - min(jug1, capacity2- jug2),
                jug2 + min(jug1, capacity2 - jug2)
            ),

            #pour jug2 -> jug1
            (
                jug1 + min(jug2, capacity1-jug1),
                jug2 - min(jug2, capacity1-jug1)
            )
        ]

        # Add unvisited states to the queue
        for state in next_states:
            if state not in visited:
                queue.append((state[0],state[1],path))

    #No solution found
    return None

#Main program
jug1= int(input("Enter capacity of jug1: "))
jug2= int(input("Enter capacity of jug2: "))
target= int(input("Enter target amount: "))

solution = water_jug(jug1, jug2, target)

if solution:
    print("\nSteps to reach the target: ")

    for step in solution:
        print(step)

else:
    print("No solution exists.")

#output
# Enter capacity of jug1: 4
# Enter capacity of jug2: 3
# Enter target amount: 2
# 
# Steps to reach the target: 
# (0, 0)
# (0, 3)
# (3, 0)
# (3, 3)
# (4, 2)