#import the zoo project and system libraries
import zoo
import sys

#import the packages required to interface with QGIS
import os
import sys
import json
import pandas as pd

#set the paths needed for the QGIS interface
qspath='home/GSoC_ZOO-Project/zoo-project/zoo-services/qgis/setting_up_operations/qgis_sys_paths.csv' 
qepath='home/GSoC_ZOO-Project/zoo-project/zoo-services/qgis/setting_up_operations/qgis_env.json'
	

#create the funtion to apply the affine transform
def ApplyAffineTransform(conf,inputs,outputs):
	
	#interface with QGIS
	global qspath
	global qepath
	paths=pd.read_csv(qspath).paths.tolist()
	sys.path+=paths
	js=json.loads(open(qepath,'r').read())
	for k, v in js.items():
	    os.environ[k] = v
	os.environ['PROJ_LIB']='/Applications/Qgis.app/Contents/Resources/proj'
	import PyQt5.QtCore
	from osgeo import gdal
	import qgis.PyQt.QtCore
	from qgis.core import (QgsApplication,
	                       QgsProcessingFeedback,
	                       QgsProcessingRegistry)
	from qgis.analysis import QgsNativeAlgorithms
	feedback=QgsProcessingFeedback()
	QgsApplication.setPrefixPath(js['HOME'],True)
	qgs=QgsApplication([],False)
	qgs.initQgis()
	from processing.core.Processing import Processing
	Processing.initialize()
	import processing
	algs = dict()
	for alg in QgsApplication.processingRegistry().algorithms():
	    algs[alg.displayName()] = alg.id()
	
	#select affine transform is to be applied
	algorithmToApply="native:affinetransform"

	#get the inputs, and output destination
	#read a geojson file containing the geometry on which the transform is to be applied
	inputGeometry=inputs['inputGeometry']
	#set translation parameters for the affine transforms
	deltaXValue=inputs['deltaX']
	deltaYValue=inputs['deltaY']
	deltaZValue=inputs['deltaZ']
	deltaMValue=inputs['deltaM']
	#set scale parameters for the affine transforms
	scaleXValue=inputs['scaleX']
	scaleYValue=inputs['scaleY']
	scaleZValue=inputs['scaleZ']
	scaleMValue=inputs['scaleM']
	#set rotation around the Z-axis
	rotationZValue=inputs['rotationZ']
	#set the destination for the transformed geometry
	outputGeometrydeltaX=outputs['outputGeometry']

	#check if the scale factor for X direction is 0
    if scaleX==0:
        print("Scale factor for X dimension is 0")
    #check if the scale factor for Y direction is 0
    elif scaleY==0:
        print("Scale factor for Y dimension is 0")
    #check if the scale factor for Z direction is 0
    elif scaleZ==0:
        print("Scale factor for Z dimension is 0")
    #check if the scale factor for M direction is 0
    elif scaleM==0:
        print("Scale factor for M dimension is 0")
    else:
        #set the parameters for the transform
        transformParameters={
            'DELTA_X':deltaX,
            'DELTA_Y':deltaY,
            'DELTA_Z':deltaZ,
            'DELTA_M':deltaM,
            'SCALE_X':scaleX,
            'SCALE_Y':scaleY,
            'SCALE_Z':scaleZ,
            'SCALE_M':scaleM,
            'ROTATION_Z':rotationZ,
            'INPUT':sourceFile,
            'OUTPUT':destinationFile,  
        }
        #apply the transform
        processing.run(algorithmToApply,transformParameters)
        #send success message
        return zoo.SERVICE_SUCCEEDED
    #send failure message
    return zoo.SERVICE_FAILED