# This is the program introduction message which will be accompanied by
# instructions on whether to continue using the platform or exit.

def intro():
    
    # input selection options.
    proceed = {1:'Yes'}
    exit = {2:'No'}

    
    # Creating a continuos loop that runs if the two provided input selections aren't met.
    while True:
        message = input('''
                    Spice your food, spice your heart
                    Would you like to shop?
                    1. Yes
                    2. No
                    ''')
        # condition checks the input values to determine what to output.
        if message == '1' or '2':
            if message == '2':
                print('Thank you, we hope to see you soon')
                break
            elif message == '1':
                print('We \'re glad to have you on board, please proceed to shopping.')
                break      
            else:
                print('Kinldy make sure your input is the correct character/digit')
        
            
intro()
             
   

  