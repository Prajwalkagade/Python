# Function to calculate the absolute value of a number
def absolute_value(number):
  # Use the built-in abs function to calculate the absolute value
  return abs(number)

# Get a number from the user
number = float(input("Enter a number: "))

# Print out the absolute value of the number
print("The absolute value of", number, "is", absolute_value(number))
