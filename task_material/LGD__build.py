"""
Simple lattice gas particle diffusion model
"""
from kmcos.types import *
import kmcos

model_name = __file__[+0:-3] # This is the python file name, the brackets cut off zero characters from the beginning and three character from the end (".py").  To manually name the model just place a string here.
model_name = model_name.replace("__build", "")

kmc_model = kmcos.create_kmc_model(model_name)
# Meta information
kmc_model.set_meta(author='Juan M. Lorenzi',
            email='jmlorenzi@gmail.com',
            model_name='ion_diffusion_model',
            model_dimension=2)

# Species
kmc_model.add_species(name='empty', color='#d3d3d3')
kmc_model.add_species(name='ion', color = '#0000ff',
               representation="Atoms('Si')")
kmc_model.species_list.default_species = 'empty'

# Layers
layer = Layer(name='default')
layer.sites.append(Site(name='a', pos='0.5 0.5 0.5',
                        default_species='empty'))
kmc_model.add_layer(layer)
kmc_model.lattice.cell = np.diag([3, 3, 3])

# Parameters
kmc_model.add_parameter(name= 'E0', value = 0.5)
kmc_model.add_parameter(name='T', value = 300)

# Coords
center = kmc_model.lattice.generate_coord('a.(0,0,0).default')

up = kmc_model.lattice.generate_coord('a.(0,1,0).default')
down = kmc_model.lattice.generate_coord('a.(0,-1,0).default')

left = kmc_model.lattice.generate_coord('a.(-1,0,0).default')
right = kmc_model.lattice.generate_coord('a.(1,0,0).default')

# Processes
kmc_model.add_process(name='diffusion_up',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=up)],
               actions=[Action(species='ion', coord=up),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

kmc_model.add_process(name='diffusion_down',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=down)],
               actions=[Action(species='ion', coord=down),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

kmc_model.add_process(name='diffusion_left',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=left)],
               actions=[Action(species='ion', coord=left),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

kmc_model.add_process(name='diffusion_right',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=right)],
               actions=[Action(species='ion', coord=right),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

# Save the model to an xml file
###It's good to simply copy and paste the below lines between model creation files.
kmc_model.print_statistics()
kmc_model.backend = 'local_smart'
' '
kmc_model.clear_model() #This line is optional: if you are updating a model, this line will remove the old model before exporting the new one. It is convenent to always include this line because then you don't need to 'confirm' removing the old model.
kmc_model.save_model()
kmcos.compile(kmc_model)