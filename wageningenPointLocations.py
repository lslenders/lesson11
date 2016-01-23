from createVectorProperties import *
from spatialRefSyst import applySpatialRefSystem
from osgeo import ogr, osr
import os



#set working directory]
os.chdir('/home/jasondavis/Wageningen/geoscripting/lesson11')

##Add spatial reference system
spatialReference = applySpatialRefSystem(4326)


## Import driver
driver = applyDriverSettings("ESRI Shapefile")


# Create a datasource
shapefileObject = "WageningenPoints.shp"
datasource = driver.CreateDataSource(shapefileObject)

#create a point geometry from wkt (well known text)
pointA = "POINT (51.986328 5.663271)"
pointB = "POINT (51.968977 5.664226)"

points = [pointA, pointB]

## Create a layer
layername = "wageningenlayer"
layer = CreateLayer(datasource, layername, spatialReference, ogr.wkbPoint)



##Main loop
for point in points:
	## give geometry to points
	geometry = createPointGeometry(point); print "returned"
	## create a feature
	feature = defineFeature(layer.GetLayerDefn()) ; print "returned"
	print point
	## add points to the feature
	feature = feature.SetGeometry(geometry); print feature
	## store the feature in a layer
	layer.CreateFeature(feature)
	print point


## Close the layer




## Modify a shapefile

##Visualize the object

#Create KML file
out_KMLfile = '/home/jasondavis/Wageningen/lesson11/outKMLfile.kml'
## Put into list of lists

## Export to a KML file
