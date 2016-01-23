from osgeo import ogr
def createPointGeometry(point):
	"""
	Create a point geometry from wkt lat lon strings
	
	Args:
		wkt string of lat lon
	Returns:
		ogr point object
	"""
	geometry = ogr.CreateGeometryFromWkt(point)
	return geometry

def applyDriverSettings( driverName ):
	"""
	Applies driver settings

	Args:
		Driver name (str)

	Returns:
		Driver (ogr) object
	"""
	driver = ogr.GetDriverByName(driverName)
	return driver

def CreateLayer(datasource, layerName, SpatialRefObj, eType):
	"""
	Creates a layer from a datasource linked to a shapefile
	
	Args:
		datasource (ogr object): OGRDataSourceShadow
		layerName (str): chosen by user
		spatialRefObj (ogr object): output of osr.SpatialReference()
		eType (int): the geometry type for the layer, Use wkbUnknown if no constraints
			otherwise ogr.wkbPoint in our case
	Returns:
		OGR layer shadow object
		layerDefinition
	"""
	layer = datasource.CreateLayer(layerName, SpatialRefObj, eType)
	return layer

def defineFeature(layerDefinition):
	"""
	Defines a  feature from a layer definition
	
	Args:
		point
		layer Definition (OGRDataObject): that is defined from the return of layer creation
	Returns:
		A feature with the appropriate layer definition (OGRDataObject)
	"""
	feature = ogr.Feature(layerDefinition)
	return feature













		
