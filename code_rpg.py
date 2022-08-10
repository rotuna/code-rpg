from util.input_control import is_valid

print('Welcome to Code RPG')
print("To play the game enter 'c', to exit the game type 'exit'. ")
while True:
    user_input = input()
    if is_valid(user_input, set(['c', 'exit'])):
        if user_input == 'exit':
            raise SystemExit
        else:
            print('You gave me an input')