# ask for yes or no input
def askYesNo(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question + '\n').lower()
    return response

# ask for a string input
def ask_str(question):
    response = None
    while response != '':
        response = input(question + '\n').lower()
        return response

# ask for an integer input
def ask_int(question):
    response = None
    while response != 0:
        try:
            response = int(input(question + '\n').strip('$'))
            return response
        except:
            print('Please enter a number.\n')