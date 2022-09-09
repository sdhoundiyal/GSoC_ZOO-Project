#set the algorithm to be applied
algorithmToApply="native:affinetransform"
processing.algorithmHelp(algorithmToApply)


#define function to apply affine transform
def qgisAffineTransform(sourceFile,deltaX,deltaY,deltaZ,deltaM,scaleX,scaleY,scaleZ,scaleM,rotationZ,destinationFile):
    #set the algorithm to apply
    algorithmToApply="native:affinetransform"
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
        #processed message
        print("Data processed")


#read a geojson file containing the geometry on which the transform is to be applied
sourceFileAddress='F:/GSOC22/Files/Affine transform/uttarPradesh.geojson'
#set translation parameters for the affine transforms
deltaXValue=1.2
deltaYValue=1.5
deltaZValue=0
deltaMValue=0
#set scale parameters for the affine transforms
scaleXValue=1
scaleYValue=1
scaleZValue=1
scaleMValue=1
#set rotation around the Z-axis
rotationZValue=0
#set the destination for the transformed geometry
destinationFileAddress='F:/GSOC22/Files/Affine transform/transformed_UttarPradesh.geojson'


qgisAffineTransform(sourceFileAddress,
                    deltaXValue,
                    deltaYValue,
                    deltaZValue,
                    deltaMValue,
                    scaleXValue,
                    scaleYValue,
                    scaleZValue,
                    scaleMValue,
                    rotationZValue,
                    destinationFileAddress)

