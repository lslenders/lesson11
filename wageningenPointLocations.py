from createVectorProperties import *
from spatialRefSyst import applySpatialRefSystem
from osgeo import ogr, osr
import os

#set working directory
os.chdir('/home/jasondavis/Wageningen/geoscripting/lesson11')

##Add spatial reference system
spatialReference = applySpatialRefSystem(4326)


## Import driver
driver = applyDriverSettings("ESRI Shapefile")

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

# Generate kml file
#fpor
#f = open("+coordinate[2]+".kml", "w+")
#f.write("<Placemark>" + point.ExportToKML() + "</Placemark>")
#f.close()









