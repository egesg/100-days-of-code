# Don't change the code below
two_digit_number = input("Type a two digit number: ")

# Write your code below this line
# print(type(two_digit_number)) # Check the data type of two_digit_number

# Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two digits together
two_digit_number = first_digit + second_digit

print(two_digit_number)

# Type a two digit number: 26
# 8