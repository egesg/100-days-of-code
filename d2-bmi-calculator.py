# Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Write your code below this line
weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2 # Using the exponent operator **
bmi = weight_as_int / (height_as_float * height_as_float) # or using multiplication and PEMDAS
bmi_as_int = int(bmi)

print(bmi_as_int)

# enter your height in m: 1.75
# enter your weight in kg: 55
# 17