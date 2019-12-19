#
# File where the food list is stored
#
from source.foodlistfile import FoodListFile


class FoodList(object):
    file = None

    def __init__(self):
        file = FoodListFile()