def encoder(password):
    result = ''

    for element in password:
        #cast the element to int, add three, mod 10 to get 0-9 inclusive, then cast back to string
        result += str(((int(element) + 3) % 10) )

    return result
if __name__ == "__main__":

    done = False

    while not done:
        print('''Menu
    -----
    1. Encode Password
    2. Decode Password''')
        choice = int(input('Choose an option:'))
        match choice:
            case 1:
                password = input('Enter a password:')
                print('Encoded password:' + encoder(password))
            case 2:
                pass
