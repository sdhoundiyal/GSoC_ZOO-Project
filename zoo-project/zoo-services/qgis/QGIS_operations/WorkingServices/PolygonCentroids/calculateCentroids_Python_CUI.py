#set the algorithm to be applied
algorithmToApply="native:centroids"
processing.algorithmHelp(algorithmToApply)



#define function to apply affine transform
def qgisCentroids(sourceFile,parts,destinationFile):
    #set the algorithm to be applied
    algorithmToApply="native:centroids"
    #check if no centroids are to be calculated
    if parts==0:
        print("No centroids calcualted")
    else:
        #set parameters for the transform
        transformParameters={
            'INPUT':sourceFile,
            'ALL_PARTS':parts,
            'OUTPUT':destinationFile
        }
        #apply the transform
        processing.run(algorithmToApply,transformParameters)
        
        #processed message
        print("Data processed")



#read a geojson file containing the geometry whose centroids are to be calculated
sourceFileAddress='F:/GSOC22/Files/Affine transform/uttarPradesh.geojson'
#set centroids are to be calcualted for which parts
allParts=True
#set the destination for the transformed geometry
destinationFileAddress='F:/GSOC22/Files/Affine transform/centroids_UttarPradesh.geojson'




qgisCentroids(sourceFileAddress,
                allParts,
                destinationFileAddress)
