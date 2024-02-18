import itertools

# Function to calculate the numerical value of a word based on a substitution dictionary
def get_value(word, substitution):
    s = 0
    factor = 1
    # Iterate over the letters in reverse order
    for letter in reversed(word):
        # Calculate the numerical value of the letter and add it to the total
        s += factor * substitution[letter]
        # Increment the factor for the next digit place
        factor *= 10
    return s

# Function to solve the cryptic arithmetic equation
def solve2(equation):
    # Split the equation into the left-hand side (LHS) and right-hand side (RHS)
    left, right = equation.lower().replace(' ', '').split('=')
    left = left.split('+')  # Split the LHS into individual words

    # Extract all unique letters appearing in the equation
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)  # Convert the set of letters to a list

    digits = range(10)  # Define the range of digits from 0 to 9
    # Generate all possible permutations of digits for the unique letters
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))  # Create a substitution dictionary for the current permutation

        # Check if the sum of the numerical values of words on the LHS equals the value on the RHS
        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            # If a solution is found, print the equation and the mapping of letters to digits
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol))

# Example usage:
equation = "SEND + MORE = MONEY"
solve2(equation)
