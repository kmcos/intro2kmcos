"""
Generate the ZGB CO oxidation model

Juan M. Lorenzi
TU Munich
June 2016
"""

import kmcos
# First kmcos.types
from kmcos.types import *

model_name = str( os.path.basename(__file__)[+0:-3]) # This is the python file name, the brackets cut off zero characters from the beginning and three character from the end (".py").  To manually name the model just place a string here.
model_name = model_name.replace("__build", "")

# Initialize the project
kmc_model = kmcos.create_kmc_model(model_name)

# Set projects metadata
kmc_model.set_meta( author = 'Juan M. Lorenzi',
             email = 'jmlorenzi@gmail.com',
             model_name = 'zgb_model',
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

kmc_model.add_species(name = 'CO', color = '#0000ff',
               representation = "Atoms('N',[[0.,0.,0.]])",
               )

# Model parameters
kmc_model.add_parameter(name = 'yCO', value = 0.5,
                 adjustable = True, min = 0.0, max = 1.0)

kmc_model.add_parameter(name = 'kfast', value = 1e10, # "Infinite" reaction rate
                 adjustable = False)

kmc_model.add_parameter(name = 'kslow', value = 1e-10, # "Zero" desorption rate
                 adjustable = False)


# Define Processes
#   Generate auxiliary coordinates
center = kmc_model.lattice.generate_coord('hol')
right = kmc_model.lattice.generate_coord('hol.(1,0,0)')
up = kmc_model.lattice.generate_coord('hol.(0,1,0)')
left = kmc_model.lattice.generate_coord('hol.(-1,0,0)')
down = kmc_model.lattice.generate_coord('hol.(0,-1,0)')


# Define single site processes
kmc_model.add_process(name = 'CO_ads',
               conditions = [Condition(coord=center,species='empty'),],
               actions = [Action(coord=center,species='CO')],
               rate_constant = 'yCO')

kmc_model.add_process(name = 'CO_des',
               conditions = [Condition(coord=center,species='CO'),],
               actions = [Action(coord=center,species='empty')],
               rate_constant = 'kslow')


# Define two-site processes programatically
#    O2 ads/des
for i, coord in enumerate([right, up]):
    ads_conds = [Condition(coord=center, species='empty'),
                 Condition(coord=coord, species='empty')]
    ads_acts  = [Action(coord=center, species='O'),
                 Action(coord=coord, species='O')]
    # O2 adsorption
    kmc_model.add_process(name = 'O2_ads_{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = '0.5*(1-yCO)')
    # O2 desorption
    kmc_model.add_process(name = 'O2_des_{:02d}'.format(i),
                   conditions = ads_acts,
                   actions = ads_conds,
                   rate_constant = 'kslow')

#    CO oxidation
for i, coord in enumerate([right, up, left, down]):
    ads_conds = [Condition(coord=center, species='CO'),
                 Condition(coord=coord, species='O')]
    ads_acts  = [Action(coord=center, species='empty'),
                 Action(coord=coord, species='empty')]

    # O2 adsorption
    kmc_model.add_process(name = 'CO_oxi_{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'kfast',
                   tof_count = {'CO_oxidation' : 1})

# Save the model to an xml file
###It's good to simply copy and paste the below lines between model creation files.
kmc_model.print_statistics()
kmc_model.backend = 'local_smart'
kmc_model.clear_model() #This line is optional: if you are updating a model, this line will remove the old model before exporting the new one. It is convenent to always include this line because then you don't need to 'confirm' removing the old model.
kmc_model.save_model()
kmcos.compile(kmc_model)