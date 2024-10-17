def highest_picker(number_1, number_2, highest_number_placeholder):
    if number_1 > number_2:
        highest_number_placeholder.append(number_1)
    elif number_2 > number_1:
        highest_number_placeholder.append(number_2)
    else:  # If both numbers are equal
        highest_number_placeholder.extend([number_1, number_2])

# Define a list to store the highest numbers
highest_number = []

# Example usage
highest_picker(5, 15, highest_number)

print("Highest numbers:", highest_number)
