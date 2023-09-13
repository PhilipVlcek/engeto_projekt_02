def compare_numbers(ran_num, guess):

    """
    This function calculates the number of bulls and cows by comparing a secret number with a guessed number.
    """

    ran_num = str(ran_num)
    guess = str(guess)

    bulls = 0
    cows = 0

    for i in range(0, 4):

        for j in range(0,4):

            if i == j and ran_num[i] == guess[j]:

                bulls += 1

            elif i != j and ran_num[i] == guess[j]:

                cows += 1

    return [bulls, cows]


