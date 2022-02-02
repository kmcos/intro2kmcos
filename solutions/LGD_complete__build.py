"""
Simple lattice gas particle diffusion model
"""
import kmcos
from kmcos.types import *


model_name = __file__[+0:-3] # This is the python file name, the brackets cut off zero characters from the beginning and three character from the end (".py").  To manually name the model just place a string here.
model_name = model_name.replace("_complete__build", "")
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
kmc_model.add_species(name='source', color = '#00ff00',
               representation="Atoms('Au')")
kmc_model.add_species(name='drain', color = '#ff0000',
               representation="Atoms('Ag')")
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
kmc_model.add_parameter(name= 'eps_f', value = 0.0, adjustable=True, min = -0.05, max=0.05)

kmc_model.add_parameter(name= 'thetaS', value=1.0, adjustable=True, min=0.0, max=1.0)
kmc_model.add_parameter(name= 'thetaD', value=0.0, adjustable=True, min=0.0, max=1.0)

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
               rate_constant='1/(beta*h)*exp(-beta*(E0+eps_f)*eV)')

kmc_model.add_process(name='diffusion_right',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=right)],
               actions=[Action(species='ion', coord=right),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*(E0-eps_f)*eV)')

kmc_model.add_process(name='source_entry',
               conditions=[Condition(species='empty', coord=center),
                           Condition(species='source', coord=left)],
               actions=[Action(species='ion', coord=center),
                        Action(species='source', coord=left)],
               rate_constant='thetaS*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)')

kmc_model.add_process(name='source_exit',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='source', coord=left)],
               actions=[Action(species='empty', coord=center),
                        Action(species='source', coord=left)],
               rate_constant='(1-thetaS)*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)')

kmc_model.add_process(name='drain_exit',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='drain', coord=right)],
               actions=[Action(species='empty', coord=center),
                        Action(species='drain', coord=right)],
               rate_constant='(1-thetaD)*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)',
               tof_count = {
                   # 'exit' : 1,
                   'current' : 1
                   },
               )

kmc_model.add_process(name='drain_entry',
               conditions=[Condition(species='empty', coord=center),
                           Condition(species='drain', coord=right)],
               actions=[Action(species='ion', coord=center),
                        Action(species='drain', coord=right)],
               rate_constant='thetaD*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)',
               tof_count = {
                   # 'back_entry' : 1,
                   'current' : -1
                   }
                            )

# Save the model to an xml file
###It's good to simply copy and paste the below lines between model creation files.
kmc_model.print_statistics()
kmc_model.clear_model(model_name, backend=kmc_model.backend) #This line is optional: if you are updating a model, this line will remove the old model before exporting the new one. It is convenent to always include this line because then you don't need to 'confirm' removing the old model.
kmc_model.save_model()
kmcos.compile(kmc_model)