# Task 1c
# Name: Task1c.py
# Description: create initial buffer script
#PARAMETERS FORMATTED IN ARCGIS PRO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#See E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/PS4.tbx for details

# Import system modules
import arcpy
   
# Set workspace
arcpy.env.workspace = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True

#allow user specified buffer distance
buffDist = arcpy.GetParameterAsText(0)
buff = "{} meters".format(buffDist)

# Set local variables
in_features_streams = "streams.shp"
out_features_StrmBuff = arcpy.GetParameterAsText(1)

#run Buffer_analysis
arcpy.Buffer_analysis(in_features_streams,out_features_StrmBuff,buff,'','','ALL')

#display any messages
print(arcpy.GetMessages())