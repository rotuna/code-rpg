import json
path = './story/'

class story_controller():
    def __init__(self):
        self.chapter = 'introduction'
        self.position = '0'
        self.curr_story = json.load(open(path + self.chapter + '.json'))
    
    def get_story(self) -> str:
        return self.curr_story[self.position]['story_text']

    def perform_action(self, action: str) -> True:
        if action in self.curr_story[self.position]['available_actions']:
            self.position = self.curr_story[self.position]['available_actions'][action]
            return True
        else:
            return False

