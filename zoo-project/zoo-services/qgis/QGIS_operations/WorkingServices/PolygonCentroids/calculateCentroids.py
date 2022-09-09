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
def CalculateCentroids(conf,inputs,outputs):
	
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
	
	#set the algorithm to be applied
    algorithmToApply="native:centroids"

    #get the inputs, and output destination
    inputGeometry=inputs['inputGeometry']
    parts=inputs['parts']
    outputGeometry=outputs['outputGeometry']

    #check if no centroids are to be calculated
    if parts==0:
        print("No centroids calcualted")
    else:
        #set parameters for the transform
        transformParameters={
            'INPUT':inputGeometry,
            'ALL_PARTS':parts,
            'OUTPUT':outputGeometry
        }
        #apply the transform
        processing.run(algorithmToApply,transformParameters)
       
        #send success message
        return zoo.SERVICE_SUCCEEDED
        
    #send failure message
    return zoo.SERVICE_FAILED