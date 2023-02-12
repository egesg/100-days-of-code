import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Write your code below this line
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

# Give me everybody's names, separated by a comma. rose, jack, mathilda, leon
# leon is going to buy the meal today!