# 
# Manages list of food
#
import os
from os import path



class FoodListFile(object):
    __new_item = None
    __files_folder = path.join(path.dirname(path.abspath(path.curdir)), 'files')
    __foodlist_file = path.join(__files_folder, 'food_list.csv')

    def __init__(self):
        self.create_food_list()
    
    def create_food_list(self):
        '''Creates the file where the food list is going to be stored'''
        if(not path.exists(self.__files_folder)):
            os.mkdir(self.__files_folder)
        if(not path.exists(self.__foodlist_file)):
            f = open(self.__foodlist_file, "w+")            
            f.close()
            print(f'Food list file created :)')
