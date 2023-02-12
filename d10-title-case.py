# Functions with outputs
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        # Return as an early exit
        return "You didn't provide valid inputs."
        
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

# Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
# Your first name: ege
# Your last name: kacmaz
# Result: Ege Kacmaz


# OR


# printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))
# What is your first name? ege
# What is your last name? kacmaz
# Result: Ege Kacmaz