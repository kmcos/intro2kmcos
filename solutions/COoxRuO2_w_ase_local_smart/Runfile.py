from kmcos.run import KMC_Model
from kmc_settings import *
model = KMC_Model()
atoms = model.get_atoms(geometry=False)

#We will not need to do any steps to check the rate constants. Not that the rate constants do not depend on coverage etc.
#So we will simply check two of the rate constants for a series of temperatures.

#The temperatures for checking will be (in Kelvin):
TemperaturesToCheck = [100, 300, 500, 800]

#Now we will  check the rate constant for CO desorption. As seen in the build file, there is a thermochemistry term in the below CO desorption reaction 
print(model.rate_constants.by_name('CO_desorption_bridge'))
rate_constants_CO_desorption_bridge = []
for T_value in TemperaturesToCheck:
    #we will use the quick way of changing a parameter (which is slow if we want to change many parameters, but fine for changing one).
    model.parameters.T = T_value
    #now append the new value:
    rate_constants_CO_desorption_bridge.append(model.rate_constants.by_name('CO_desorption_bridge'))
     



#Now we will  check the rate constant for O2 desorption. As seen in the build file, there is a thermochemistry term in the below O2 desorption reaction 
print(model.rate_constants.by_name('O2_desorption_cus_up'))
rate_constants_O2_desorption_cus_up = []
for T_value in TemperaturesToCheck:
    #we will use the quick way of changing a parameter (which is slow if we want to change many parameters, but fine for changing one).
    model.parameters.T = T_value
    #now append the new value:
    rate_constants_O2_desorption_cus_up.append(model.rate_constants.by_name('O2_desorption_cus_up'))
    

#now hstack and export to file.
import numpy as np
stackedArray = np.vstack((TemperaturesToCheck, rate_constants_CO_desorption_bridge, rate_constants_O2_desorption_cus_up))

np.savetxt("StackedArray.csv", stackedArray.transpose(), delimiter=",")