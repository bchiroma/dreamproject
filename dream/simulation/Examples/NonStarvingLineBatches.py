from dream.simulation.imports import BatchScrapMachine, NonStarvingEntry, Exit, Part  
from dream.simulation.Globals import runSimulation

#define the objects of the model 
NS=NonStarvingEntry('NS1','Entry',entityData={'_class':'Dream.Batch','numberOfUnits':100})
M=BatchScrapMachine('M1','Machine', processingTime={'distributionType':'Fixed','mean':0.02})
E=Exit('E1','Exit')  

#define predecessors and successors for the objects    
NS.defineRouting(successorList=[M])
M.defineRouting(predecessorList=[NS],successorList=[E])
E.defineRouting(predecessorList=[M])

def main():
    # add all the objects in a list
    objectList=[NS,M,E]  
    # set the length of the experiment  
    maxSimTime=10
    # call the runSimulation giving the objects and the length of the experiment
    runSimulation(objectList, maxSimTime)
    
    #print the results
    print "the system produced", E.numOfExits, "batches"
    working_ratio = (M.totalWorkingTime/maxSimTime)*100
    print "the total working ratio of the Machine is", working_ratio, "%"
    return {"batches": E.numOfExits,
          "working_ratio": working_ratio}

if __name__ == '__main__':
    main()