"""
Script to import all GPX tracks from a folder into a line feature class
in a file geodatabase. New line feature for each GPX file.

Paths hardcoded in script so needs changed first before running it.

Could do with some error handling, create FGDB if it doesn't exist etc
"""

import sys, arcpy, os

gpxFolder = r"c:\stuff\python\gpx"

target = r"c:\stuff\python\GPS.gdb\Tracks_1"

arcpy.env.overwriteOutput = True

for f in os.listdir(gpxFolder):
	
	print f
	arcpy.GPXtoFeatures_conversion(gpxFolder + "\\" + f, "in_memory\\track")
    
	print "convert points to lines in memory"
	arcpy.PointsToLine_management("in_memory\\track", "in_memory\\track_line")
    	
    print "add the new in_mem line to target"
	arcpy.Append_management("in_memory\\track_line", target, "NO_TEST")
