##############################################################################
# Task 5
# Name: Script5.py
# Description: Determine what feature a point lies within
# Author: Cal Oakley
# Date: Fall 2021
##############################################################################

#import arcpy
import arcpy, sys

#set environment and enable file overwrites
arcpy.env.workspace = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True

#set input feature class
inputFC = arcpy.GetParameterAsText(0)

#describe inputFC to access fields
#descFC = arcpy.da.Describe(inputFC)

#create point object at (587000,265000)
point = arcpy.Point(587000,265000)
#turn point into geometry object
ptgeom = arcpy.PointGeometry(point)

#create search cursor with user selected field as input
rows = arcpy.da.SearchCursor(inputFC,[arcpy.GetParameterAsText(1),'Shape@'])

#iterate through rows and extract 
for row in rows:
    recShape = row[1]
    if recShape.contains(ptgeom):
    #if ptgeom in recShape:
    #if r"in_memory\tempOutput"      
        print(arcpy.AddMessage('The point is located in {} County'.format(row[0])))
    