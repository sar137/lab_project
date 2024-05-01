def get_user_input():
    prompt_message = "Enter an arithmetic expression: "
    user_input = input(prompt_message)
    return user_input

def extract_primitives(expression):
    # Logic to identify numbers and variables
    pass

# Main program
user_expression = get_user_input()
primitives = extract_primitives(user_expression)
print("Primitives extracted:", primitives)
