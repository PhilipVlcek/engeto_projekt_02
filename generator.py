import random

def num_generator():
    
    """
    This function will generate a random four digit number. It must not start with a 0 and each digit must be unique.
    """

    first_number = random.sample("123456789", 1)
    rest_of_numbers = random.sample("0123456789", 3)
    random_number = "".join(first_number + rest_of_numbers)

    return random_number

