from osgeo import osr

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
