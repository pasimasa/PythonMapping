///
Script to import all GPX tracks from a folder into a line feature class
in a file geodatabase.

Paths hardcoded in script so needs changed first before running it
///

import sys, arcpy, os

gpxFolder = r"c:\stuff\python\gpx"

target = r"c:\stuff\python\GPS.gdb\Tracks_1"

arcpy.env.overwriteOutput = True

for f in os.listdir(gpxFolder):
    print f
    arcpy.GPXtoFeatures_conversion(gpxFolder + "\\" + f, "in_memory\\track")
    
		print "convert to in_mem"
    arcpy.PointsToLine_management("in_memory\\track", "in_memory\\track_line")
    
		print "converted to line"
    arcpy.Append_management("in_memory\\track_line", target, "NO_TEST")
