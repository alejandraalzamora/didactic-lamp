"""Alejandra Alzamora"""


def encode(password):
    encoded = ''

    for i in password:
        value = int(i)
        new_value = value + 3
        string_value = str(new_value)
        encoded += string_value

    return encoded


if __name__ == '__main__':

    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        option = input('Please enter an option:')

        if option == '1':
            password = input('Please enter your password to encode:')
            encoded = encode(password)
            print('Your password has been encoded and stored!')

        elif option == '2':
            decoded = decode(encoded)
            print(f'The encoded password is {encoded}, and the original password is {decoded}.')

        elif option == '3':
            break

