# Task 1a
# Name: Task1a.py
# Description: create initial buffer script
   
# Import system modules
import arcpy
  
# Set local variables
in_features_streams = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Data/streams.shp"
out_features_StrmBuff = "E:/Fall2021/GIS/ProblemSets/PS4/ENV859_PS4/Scratch/StrmBuff1km.shp"

#set buffer distance
buffDist = "500 meters"
#run Buffer_analysis
arcpy.Buffer_analysis(in_features_streams,out_features_StrmBuff,buffDist,'','','ALL')

#display any messages
print(arcpy.GetMessages())