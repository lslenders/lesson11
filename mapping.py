import mapnik
import os

#set working directory
os.chdir('/home/jasondavis/Wageningen/geoscripting/lesson11')
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
symbolizer = mapnik.PolygonSymbolizer(mapnik.Color("red"))
rule.symbols.append(symbolizer)

#2) The rule is added to the style
style = mapnik.Style()
style.rules.append(rule)

#3) Adding style to map, "mapStyle" is a simple name for our style
#Later we will define that our layer uses this style that is stored on the maps object
map.append_style("mapStyle", style)

#4) Adding the data first step is creating a layer, a map has mutiple layers
layer = mapnik.Layer("mapLayer")
layer.datasource = mapnik.Shapefile(file=os.path.join("data",
                                        "world_borders.shp"))
layer.styles.append("mapStyle")

#map.append_style("mapStyle", style)

#5) The current layer is not yet associated to the map 
map.layers.append(layer)

#6) Zoom to full extend of layers and dump content
map.zoom_all()
mapnik.render_to_file(map, os.path.join("figs",
                                        "map.png"), "png")
print "All done - check content"
