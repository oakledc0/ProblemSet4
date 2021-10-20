##############################################################################
# Task 3
# Name: Task3.py
# Description: Splitting multiple benthic monitoring site feature classes by county
# Author: Cal Oakley
# Date: Fall 2021
##############################################################################

#import arcpy
import arcpy, sys

#set environment and enable file overwrites
arcpy.env.workspace = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True

#load splitting features (TriCounties.shp)
counties = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Data/TriCounties.shp"

#check for appropriate product license
if arcpy.CheckProduct('ArcInfo') == "Available":
  
    #create list of all 5 BMR feature classes    
    BMRlist = arcpy.ListFeatureClasses("BMR_*")
    
    #create empty list to hold folder locations
    BMRfolders = []
    
    #create folders for each BMR ranking
    for rank in BMRlist:
            arcpy.management.CreateFolder("E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Scratch", rank[:-4])
            #populate list of folders for each BMR ranking
            BMRfolders.append("E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Scratch/"+rank[:-4])
    
    for shp in BMRlist:
        arcpy.analysis.Split(shp,counties,"CO_NAME","E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Scratch/"+shp[:-4])
else:
    msg = 'ArcGIS for Desktop Advanced License not available'
    print(msg)
    sys.exit(msg)