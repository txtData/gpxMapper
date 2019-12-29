# -*- coding: utf-8 -*-
import gpxpy
import gpxpy.gpx
from folium import Map, PolyLine
from os.path import join
from os import walk


GPX_INPUT_DIR = './GPX/'
HTML_OUT_FILE = './gpx_berlin.html' 
MAP_CENTER = [52.5200, 13.4050]
MAP_ZOOM = 11


def read_gpx(file):
    gpx_file = open(file, 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    return points


my_map = Map(location=MAP_CENTER, MAP_ZOOM=11)
for (dirpath, dirnames, filenames) in walk(GPX_INPUT_DIR):
    for file in filenames:   
        file = join(dirpath, file)
        points = read_gpx(file)
        PolyLine(points, color="blue", weight=5, opacity=0.5).add_to(my_map)
        print('Reading',file)


print('Writing', HTML_OUT_FILE)
my_map.save(HTML_OUT_FILE)