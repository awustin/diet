# 
# Manages list of food
#
from os import path


class FoodList(object):
    new_item = None
    file_path = path.join(path.dirname(path.curdir), 'files')

    def __init__(self):
        print(self.file_path)
    
    def create_food_list(self):
        pass
