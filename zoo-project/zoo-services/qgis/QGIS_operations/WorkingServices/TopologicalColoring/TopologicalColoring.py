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
def TopologicalColoring(conf,inputs,outputs):
	
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
    algorithmToApply="qgis:topologicalcoloring"

    #get the inputs, and output destination
    inputGeometry=inputs['inputGeometry']
    minValue=inputs['minValue']
    minDistance=inputs['minDistance']
    balance=inputs['balance']
	outputGeometry=outputs['coloredGeometry']

    #ensure that the minimum number of colors is postive
    if minimumColors<1:
        print("Minimum number of colors cannot be negetive or 0. It must be 1 or greater")
    #ensure the minimum distance is postive
    elif minimumDistance<=0:
        print("Minimum distance between features cannot be negetive.")
    #ensure the color balancing term is between 0 and 2
    elif balancingParameter>2 or balancingParameter<0:
        print("balancing parameter must be 0,1 or 2.\nKey\n0--Feature Count\n1--Assigned Area\n2--Distance between Colors")
    else:
        #set parameters for the transform
        transformParameters={
            'INPUT':inputGeometry,
            'MIN_COLORS':minValue,
            'MIN_DISTANCE':minDistance,
            'BALANCE':balance,
            'OUTPUT':outputGeometry
        }
        #apply the transform
        processing.run(algorithmToApply,transformParameters)
       
        #send success message
        return zoo.SERVICE_SUCCEEDED
        
    #send failure message
    return zoo.SERVICE_FAILED