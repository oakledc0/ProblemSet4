##############################################################################
# Task 2
# Name: Task2.py
# Description: iterates through road type codes and extracts road types 0, 201, and 203
# Author: Cal Oakley
# Date: Fall 2021
##############################################################################

#import arcpy
import arcpy

#set environment and enable file overwrites
arcpy.env.workspace = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True

#specify Roads.shp
roads = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Data/Roads.shp"

#create string of values for selecting road types 0, 201, & 203
road_clss_str = "0;201;203"

#split road_clss_str into list
road_clss_lst = road_clss_str.split(";")

#iterate through road_clss_lst to produce seperate feature classes for each road type in Roads.shp
for t in road_clss_lst:
    #create SQL expression
    road_clss_SQL = "ROAD_TYPE = "+t
    #create output file pathname
    output_roads = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Scratch/road_"+t+".shp"
    #select and output new feature classes
    road_select = arcpy.Select_analysis(roads,output_roads,road_clss_SQL)
