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

## Create a layer
layername = "wageningenlayer"
layer = CreateLayer(datasource, layername, spatialReference, ogr.wkbPoint)

##Create a point
point1 = ogr.Geometry(ogr.wkbPoint)
point2 = ogr.Geometry(ogr.wkbPoint)

point1.AddPoint(51.986328, 5.663271)
point2.AddPoint(51.968977, 5.664226)

#Define properties of the layer
layerDefinition = layer.GetLayerDefn()
feature1 = ogr.Feature(layerDefinition)
feature2 = ogr.Feature(layerDefinition)

## add points to feature
feature1.SetGeometry(point1)
feature2.SetGeometry(point2)

## store feature in layer
layer.CreateFeature(feature1)
layer.CreateFeature(feature2) 

print "The new extent"
print layer.GetExtent()

## save and write to shapefile
datasource.Destroy()
