import pandas as pan
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl
import numpy as num


class App():
    def __init__(self):
        on = True

    def main(self):
        data = pan.DataFrame({'column1': [1,2,3,4],
                              'column2': [1,2,3,4]})
        writer = ExcelWriter('Diet_Test.xlsx')
        data.to_excel(writer, 'Sheet1', index=False)
        writer.save()

if __name__=="__main__":
    myApp = App()
    myApp.main()