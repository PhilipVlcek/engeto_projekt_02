def player_input():

    """
    This function takes input from the user
    and compares it against all possible errors
    """

    while(True):
        
        input_num = input(" >>> ")

        if input_num.isnumeric() == False:
            
            print("Only numbers are allowed")
            continue

        elif len(input_num) != 4:
                
            print("Enter a 4 digit number!")
            
        else:

            duplicate = 0

            for i in range(0,4):
                duplicate += input_num.count(input_num[i])
    
            if duplicate != 4:
                    
                print("Enter a number with different digits")
                continue
                
            elif int(input_num[0]) == 0:
                
                print("Number must not start with zero")
                continue

            else:

                return input_num
        

            

        

                        