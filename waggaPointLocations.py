from functions import *
from osgeo import ogr, osr
import os, os.path

#set working directory
os.getcwd()
os.chdir(str(os.getcwd()+'/data'))

##Add spatial reference system
spatialReference = applySpatialRefSystem(4326)


## Import driver
driver = applyDriverSettings("ESRI Shapefile")
if os.path.exists('WageningenPoints.shp'):
	os.remove('WageningenPoints.shp')
	os.remove('WageningenPoints.prj')
	os.remove('WageningenPoints.shx')
	os.remove('WageningenPoints.dbf')


# Create a datasource
shapefileObject = "WageningenPoints.shp"
datasource = driver.CreateDataSource(shapefileObject)

#create a point geometry from wkt (well known text)
pointA = [51.986328, 5.663271]
pointB = [51.968977, 5.664226]

points = [pointA, pointB] # make a list from points


## Create a layer to store points in, define spatialReference, and feature geometry type
layername = "wageningenlayer"
layer = CreateLayer(datasource, layername, spatialReference, ogr.wkbPoint)

##Main loop
for point in points:
	print point
	## Create a point
	geometry = ogr.Geometry(ogr.wkbPoint)
	## AddPoint
	geometry.AddPoint(point[0], point[1]) ; print geometry
	## Give feature definition from layer; Feature is defined from properties of the layer
	layerDefinition = layer.GetLayerDefn()
	feature = ogr.Feature(layerDefinition)
	## add the points to the feature
	feature.SetGeometry(geometry)
	## store the feature in a layer
	layer.CreateFeature(feature)


print "The new extent"
print layer.GetExtent()

## save and write to shapefile
datasource.Destroy()

## Create map-------------------------------------------------------------------------------------------

import mapnik

#First we create a map
map = mapnik.Map(600, 300) #This is the image final image size

#Lets put some sort of background color in the map
map.background = mapnik.Color("steelblue") # steelblue == #4682B4 

#To style the map we need to define a set or rules
#        Map
#  Style      Style
# Rule   Rule   Rule  Rule

# we normally start from the bottom creating an empty rule
rule = mapnik.Rule()

#1) rule that the polygon should be dark red
symbolizer = mapnik.PolygonSymbolizer(mapnik.Color("darkred"))
rule.symbols.append(symbolizer)

#2) The rule is added to the style
style = mapnik.Style()
style.rules.append(rule)

# File with symbol for point
file_symbol=os.path.join("figs","fig_start.png")

#3) Adding style to map, "mapStyle" is a simple name for our style
#Later we will define that our layer uses this style that is stored on the maps object
map.append_style("mapStyle", style)

#4) Adding the data first step is creating a layer, a map has mutiple layers
layerPoly = mapnik.Layer("mapLayer")
layerPoly.datasource = mapnik.Shapefile(file=os.path.join("ne_110m_land.shp"))

layerPoly.styles.append("mapStyle")

# Set boundaries for the Netherlands
boundsLL = (8 , 45, 7, 54.5) #(minx, miny, maxx,maxy)
map.zoom_to_box(mapnik.Box2d(*boundsLL)) # zoom to bbox

#5) The current layer is not yet associated to the map 
map.layers.append(layerPoly)

mapnik.render_to_file(map, "map.png", "png")

print "All done - check content"





