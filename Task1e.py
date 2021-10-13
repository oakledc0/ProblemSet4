# Task 1e
# Name: Task1e.py
# Description: create initial buffer script
   
# Import system modules
import arcpy
   
# Set workspace
arcpy.env.workspace = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True

#loop through different buffer distances
for buffDist in range(100, 600, 100):
    
#set "buffDist" as string
    buff = str(buffDist)
    
# Set local variables
    in_features_streams = "streams.shp"
    out_features_StrmBuff = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Scratch/buff"+buff+"m.shp"

#run Buffer_analysis
    arcpy.Buffer_analysis(in_features_streams,out_features_StrmBuff,buff,'','','ALL')

#display any messages
print(arcpy.GetMessages())