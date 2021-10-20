##############################################################################
# Task 4
# Name: Task4.py
# Description: 
# Author: Cal Oakley
# Date: Fall 2021
##############################################################################

#import arcpy
import arcpy, sys

#set environment and enable file overwrites
arcpy.env.workspace = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True

#define input dataset
inputDS = arcpy.GetParameterAsText(0)

#describe input dataset
inputDS_desc = arcpy.da.Describe(inputDS)

#print the dataset's catalogPath
print(arcpy.AddMessage(inputDS_desc['catalogPath']))

#create extent object
extents = inputDS_desc['extent']

#print extent boundaries
print(arcpy.AddMessage('XMin: {}'.format(f'''{extents.XMin:.1f}''')))
print(arcpy.AddMessage('YMin: {}'.format(f'''{extents.YMin:.1f}''')))
print(arcpy.AddMessage('XMax: {}'.format(f'''{extents.XMax:.1f}''')))
print(arcpy.AddMessage('YMax: {}'.format(f'''{extents.YMax:.1f}''')))

#set different warnings for different dataset types
if inputDS_desc['datasetType'] == "FeatureClass":
    arcpy.AddWarning("Shapetype: {}".format(inputDS_desc['shapeType']))
elif inputDS_desc['datasetType'] == "RasterDataset":
    arcpy.AddWarning("Format: {}".format(inputDS_desc['format']))
    arcpy.AddWarning(" # of rows: {}".format(str(inputDS_desc['height'])))
    arcpy.AddWarning(" # of columns: {}".format(str(inputDS_desc['width'])))