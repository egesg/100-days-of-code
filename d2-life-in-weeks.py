# Don't change the code below 👇
age = input("What is your current age? ")

# Write your code below this line
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# What is your current age? 26
# You have 23360 days, 3328 weeks, and 768 months left.