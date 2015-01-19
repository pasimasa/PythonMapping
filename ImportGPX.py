"""
Script to import all GPX tracks from a folder into a line feature class
in a file geodatabase. New line feature for each GPX file.

Generate linear density map of those lines to show where most tracks go.

Paths hardcoded in script so needs changed first before running it.

Could do with some error handling, create FGDB if it doesn't exist etc
Also doesn't carry any attributes through from GPX, date/time would be good
"""

import sys, arcpy, os
## TODO Jim - PARAM
gpxFolder = r"c:\stuff\python\gpx"
target = r"c:\stuff\python\GPS.gdb\Tracks_1"

def main():

    print "Truncating %s..." % target
    try:
        arcpy.TruncateTable_management(target)
    except:
        print "Target not found or can't truncate"
        sys.exit()

    for f in os.listdir(gpxFolder):
        print "Processing file %s" % f

        print "\tconvert to points in_mem"
        arcpy.GPXtoFeatures_conversion(gpxFolder + "\\" + f, "in_memory\\track")

        print "\tconvert in_memory points to lines"
        arcpy.PointsToLine_management("in_memory\\track", "in_memory\\track_line")

        print "\tadd the new in_mem line to target feature class"
        arcpy.Append_management("in_memory\\track_line", target, "NO_TEST")

        # Line density stuff todo - needs Spatial Analyst
        # lineDensity = LineDensity(target, "", 10, 20)

if __name__ == '__main__':
    main()
