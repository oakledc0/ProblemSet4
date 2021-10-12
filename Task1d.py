# Task 1a
# Name: Task1a.py
# Description: create initial buffer script
   
# Import system modules
import arcpy
   
# Set workspace
arcpy.env.workspace = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True

#allow user specified buffer distance
buffDist = arcpy.GetParameterAsText(0)

# Set local variables
in_features_streams = "streams.shp"
out_features_StrmBuff = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Scratch/buff"+buffDist[:-7]+"m.shp"

#run Buffer_analysis
arcpy.Buffer_analysis(in_features_streams,out_features_StrmBuff,buffDist,'','','ALL')

#display any messages
print(arcpy.GetMessages())