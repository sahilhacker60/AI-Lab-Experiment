def objective_function(x):
    return -x**2

def hill_climbing(start, step_size, max_iteration):
    current = start
    current_value = objective_function(current)

    for i in range(max_iteration):
        left = current - step_size
        right = current + step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        if left_value > current_value and left_value >= right_value:
            current = left
            current_value = left_value
        elif right_value > current_value:
            current = right
            current_value = right_value
        else:
            break

    return current, current_value


# Main program
start = float(input("Enter starting point: "))
step_size = float(input("Enter step size: "))
max_iteration = int(input("Enter max no. of iterations: "))

best_position, best_value = hill_climbing(
    start, step_size, max_iteration
)

print("Best position:", best_position)
print("Best value:", best_value)
# HILL CLIMBING 
def objective_function(x):
    return -x**2

def hill_climbing(start, step_size, max_iteration):
    current = start
    current_value = objective_function(current)

    for i in range(max_iteration):
        left = current - step_size
        right = current + step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        if left_value > current_value and left_value >= right_value:
            current = left
            current_value = left_value
        elif right_value > current_value:
            current = right
            current_value = right_value
        else:
            break

    return current, current_value


# Main program
start = float(input("Enter starting point: "))
step_size = float(input("Enter step size: "))
max_iteration = int(input("Enter max no. of iterations: "))

best_position, best_value = hill_climbing(
    start, step_size, max_iteration
)

print("Best position:", best_position)
print("Best value:", best_value)

#output
# Enter starting point: 5
# Enter step size: 0.5
# Enter max no. of iterations: 20
# Best position: 0.0
# Best value: -0.0