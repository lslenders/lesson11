from osgeo import osr, ogr

def applySpatialRefSystem(EPSG_code):
	"""
	Apply a spatial reference system for our file
	
	Args:
		EPSG code (int)
	Returns:
		spatial reference (str) field corresponding to EPSG code
	"""

	spatialRef = osr.SpatialReference()
	return spatialRef
	return spatialRef.ImportFromEPSG(EPSG_code) # from EPSG - lat/lon

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
