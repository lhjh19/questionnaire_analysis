#!/usr/local/bin/python3


#import plotly.plotly as draw
#import plotly.graph_objs as graphObjs
import argparse
import xlrd # read excel .xls
import openpyxl # read excel .xlsx
from datetime import date, datetime
import sys
import os
import re
import pandas as pds
import matplotlib.pyplot as plt

class PresentData:
    "Help info:"

    def __init__( self, excel_path, out_format ):
        "pass parameters to class using this function\
        also set initial values to internal variables"

        self.xl_path = excel_path
        self.out_fmt = out_format
    # enddef __init__

    def read_excel(self):
        "read excel by sheet"

        print ("%s1. Reading data from %s" % (">" * 10, exl_path))
        if re.search(r"^(.*)\.xls$", self.xl_path):
            print ("Detected xls format. Gonna use xrld library.")
            workbook = xlrd.open_workbook(filename=self.xl_path)
            sheetNames = workbook.sheet_names()
        elif re.search(r"^(.*)\.xlsx$", self.xl_path):
            print ("Detected xlsx format. Gonna use openpyxl library.")
            workbook = openpyxl.load_workbook(self.xl_path)
            sheetNames = workbook.sheetnames
        else:
            sys.exit("***** Error: Unknown file format. Requires xls or xlsx.")
        print ("\nAvailable sheets:")
        print (sheetNames)
        for sheet in sheetNames:
            print ("\n%s Working on worksheet: %s" % ("#" * 10, sheet))
            ### get the worksheet
            #worksheet = workbook[sheet]
            ### index_col=0 -> don't use default numeric row index
            ### another way to read in a bunch of excel files is pds.ExcelFile
            datFram = pds.read_excel(self.xl_path, sheet) #, index_col=0)
            ### drop completely empty rows, can add arguments to do smarter drop
            datFram.dropna(inplace=True)
            ### print all rows and all columns
            #with pds.option_context('display.max_rows', None, 'display.max_columns', None):
            #    print(datFram)
            #print( list(datFram.columns) )
            #datFram.rename(columns={'Unnamed: 1' : '%', 'Unnamed: 2' : 'Count'}, inplace=True)
            print ("Rows:")
            print( list(datFram.index) )
            print ("Columns:")
            datFram.rename(columns={'Unnamed: 3' : 'lastCol'}, inplace=True)
            print( list(datFram.columns) )
            print (datFram[["lastCol"]])
            print ( datFram.iloc[4:16, 3] )
            subDatFram = datFram.iloc[4:16, 3];
            print ( "SubDatFram:")
            print ( subDatFram )
            print ( "Axes:" )
            print ( subDatFram.axes )
            for item in datFram[["lastCol"]]:
                print ( item )
            datFram.iloc[4:16, 3].plot(kind = "barh")
            ### print beginning rows
            # print (datFram.head(10))
            ### print dimension
            # print (datFram.shape)
            ### print tailing rows
            # print (datFram.tail(10))
            if sheet == "graduation_year":
                print (">>>")
                datFram.plot(kind="scatter", x="Answer", y="%", color="green")
                #print(datFram.loc["Answer"])
            # sort_by_clm2 = datFram.sort_values(["column2"], ascending=False)
            # print (sort_by_clm2["column2"].head())
            # try:
            #     sort_by_clm2["column2"].head().plot(kind="barh")
            # except TypeError as e:
            #     print ("\n***** Error while trying to plot %s:" % sheet)
            #     sys.exit( e )
            # plt.show()
            # datFram["column1"].plot(kind="hist")
            # plt.show()
    # enddef read_excel

    def draw(self):
        print ("\t>>> 2. Deciding output format")
        if self.out_fmt == "table":
            print ("Going to")
        elif self.out_fmt == "graph":
            print ("Gonna present excel data as bar graph.")
        elif self.out_fmt == "pie":
            print ("Gonna present excel data as pir graph.")
        else:
            sys.exit("***** Error: unknown output format!")
    #enddef draw

    def create_table( self, **kwargs ):
        "**kwargs allows passing of variable number of arguments to function"
        for key, value in kwargs.items():
            if key == "row":
                print ("Rows for table: ", value)
            elif key == "column":
                print ("columns for tbale: ", value)
            else:
                print ("Error: Unkown argument %s passed to create_table function." % key)
        print ("Creating table with plotly version ", plotly.__version__)
    # endded create_table

    def main( self ):
        "execute class functions"
        self.read_excel()
        self.draw()
    # enddef main
### endclass PresentData



#################################################################################
#################################################################################
#################################################################################
if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-rd_excel", nargs=1, help="read one excel file")
    arg_parser.add_argument("-out_fmt", nargs=1, help="give one output data chart format. Support: line, bar, pie")
    # table arguments
    arg_parser.add_argument("-table", action="store_true", help="create a table")
    arg_parser.add_argument("-r", nargs="+", help="rows for table")
    arg_parser.add_argument("-c", nargs="+", help="columns for table")
    # bar chart arguments
    arg_parser.add_argument("-bar", action="store_true", help="create a bar graph")
    # pie chart arguments
    arg_parser.add_argument("-pie", action="store_true", help="create a pie chart")
    args = arg_parser.parse_args()
    if args is not None:
        if args.rd_excel[0] and args.out_fmt[0]:
            exl_path = os.path.abspath( args.rd_excel[0] )
            out_fmt = args.out_fmt[0]
            draw = PresentData(exl_path, out_fmt)
            print ()
            draw.main()
        else:
            sys.exit( "***** Error: No excel file to read OR unknown output format." )
    else:
        print ("***** Error: No command line arguments found")


