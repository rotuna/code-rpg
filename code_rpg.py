from util.story_controller import story_controller

print('Welcome to Code RPG')
print("To play the game enter 'c', to exit the game type 'exit'. ")

position_in_story = None
story = story_controller()
while True:
    print(story.get_story())
    user_input = input()
    if user_input != 'exit':
        if not story.perform_action(user_input):
            print("That action cannot be performed")
    else:
        raise SystemExit