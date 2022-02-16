"""
Demonstration of a kmos render scrikmc_model.
Generates a simple model for simulating
dissociative adsorption / associative desorption
of O2 on a FCC(100) (square) lattice

Juan M. Lorenzi
TU Munich
June 2016
"""

import kmcos
# First kmcos.types
from kmcos.types import *

model_name = __file__[+0:-3] # This is the python file name, the brackets cut off zero characters from the beginning and three character from the end (".py").  To manually name the model just place a string here.
model_name = model_name.replace("__build", "")

# Initialize the project
kmc_model = kmcos.create_kmc_model(model_name)

# Set projects metadata
kmc_model.set_meta( author = 'Juan M. Lorenzi',
             email = 'jmlorenzi@gmail.com',
             model_name = 'O2_adsdes',
             model_dimension = 2)

# Define the lattice
layer = Layer(name = 'fcc100')                 # define a layer
site = Site(name = 'hol', pos = '0.5 0.5 0.5') # define a site
layer.sites.append(site)                       # add site to layer
# Add layer to Project
kmc_model.add_layer(layer)

# Define the surface species
kmc_model.add_species(name = 'empty', color='#dddddd')

kmc_model.add_species(name = 'O', color = '#ff0000',
               representation = "Atoms('O',[[0.,0.,0.]])",
               )

# Define model parameters.. pO2 and E_over_kT
kmc_model.add_parameter(name='kads', value = 1.0)
kmc_model.add_parameter(name='kdes', value=1.0,
                 adjustable=True, min=1e-2, max=1e2, scale='log')

# Define Processes
#   Generate auxiliary coordinates
center = kmc_model.lattice.generate_coord('hol')
right = kmc_model.lattice.generate_coord('hol.(1,0,0)')
up = kmc_model.lattice.generate_coord('hol.(0,1,0)')

#   Define both adsorption processes
kmc_model.add_process(name = 'O2_ads_right',
               conditions = [Condition(coord=center, species='empty'),
                             Condition(coord=right, species='empty'),],
               actions = [Action(coord=center, species='O'),
                          Action(coord=right, species='O'),],
               rate_constant = '0.5*kads',
               )

kmc_model.add_process(name = 'O2_ads_up',
               conditions = [Condition(coord=center, species='empty'),
                             Condition(coord=up, species='empty'),],
               actions = [Action(coord=center, species='O'),
                          Action(coord=up, species='O'),],
               rate_constant = '0.5*kads',
               )

#   Define both desorption processes
kmc_model.add_process(name = 'O2_des_right',
               conditions = [Condition(coord=center, species='O'),
                             Condition(coord=right, species='O'),],
               actions = [Action(coord=center, species='empty'),
                          Action(coord=right, species='empty'),],
               rate_constant = '0.5*kdes',
               )

kmc_model.add_process(name = 'O2_des_up',
               conditions = [Condition(coord=center, species='O'),
                             Condition(coord=up, species='O'),],
               actions = [Action(coord=center, species='empty'),
                          Action(coord=up, species='empty'),],
               rate_constant = '0.5*kdes',
               )

# Alternatively, define processes programatically
# for i, coord in enumerate([right, up]):
#     ads_conds = [Condition(coord=center, species='empty'),
#                  Condition(coord=coord, species='empty')]
#     ads_acts  = [Action(coord=center, species='O'),
#                  Action(coord=coord, species='O')]
#     # Adsorption
#     kmc_model.add_process(name = 'O2_ads_{:02d}'.format(i),
#                    conditions = ads_conds,
#                    actions = ads_acts,
#                    rate_constant = '0.5*kads')
#     # Desorption
#     kmc_model.add_process(name = 'O2_des_{:02d}'.format(i),
#                    conditions = ads_acts,
#                    actions = ads_conds,
#                    rate_constant = '0.5*kdes')


# Save the model to an xml file
###It's good to simply copy and paste the below lines between model creation files.
kmc_model.print_statistics()
kmc_model.backend = 'local_smart'
kmc_model.clear_model() #This line is optional: if you are updating a model, this line will remove the old model before exporting the new one. It is convenent to always include this line because then you don't need to 'confirm' removing the old model.
kmc_model.save_model()
kmcos.compile(kmc_model)