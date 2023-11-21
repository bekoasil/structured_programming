

def two_sum_exists(numbers, target):
    # Create an empty dictionary to store seen values
    values = {}

    # Iterate through the list
    for number in numbers:
        # Calculate the complement of the current number
        complement = target - number

        # Check if the complement exists in the seen values dictionary
        if complement in values:
            return True

        # Add the current number to the seen values dictionary
        values[number] = True

    # If no two values sum to the target, return False
    return False


numbers = [2, 7, 11, 15]
target = 21

if two_sum_exists(numbers, target):
    print("True")
else:
    print("False")
