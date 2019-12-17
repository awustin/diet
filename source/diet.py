import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl
from foodlist import FoodList


class App():
    def __init__(self):
        on = True

    def main(self):  
        columns = ['Date', 'Name', 'H', 'P', 'G', 'E']
        s1 = pd.Series([pd.datetime(2019,12,17), 'a', 12, 3.3, 6, 140], index=columns)
        s2 = pd.Series([pd.datetime(2019,12,17), 'b', 1, 10, 5, 70], index=columns)
        s3 = pd.Series([pd.datetime(2019,12,17), 'c', 74, 25, 22, 400], index=columns)
        d = pd.DataFrame.from_dict([s1, s2, s3])
        print(d)

        foodlist = FoodList()

if __name__=="__main__":
    myApp = App()
    myApp.main()