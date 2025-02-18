# Old function
def calculate_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

# Refactored function
def calculate_sum(numbers):
    return sum(numbers)  # Simplified using built-in sum()
