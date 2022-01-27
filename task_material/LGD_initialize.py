"""
Simple lattice gas particle diffusion model
"""
from kmcos.types import *
import kmcos

model_name = __file__[+0:-14] # This is the python file name, the brackets cut off zero characters from the beginning and three character from the end ("initialize.py").  To manually name the model just place a string here.

pt = Project()
# Meta information
pt.set_meta(author='Juan M. Lorenzi',
            email='jmlorenzi@gmail.com',
            model_name='ion_diffusion_model',
            model_dimension=2)

# Species
pt.add_species(name='empty', color='#d3d3d3')
pt.add_species(name='ion', color = '#0000ff',
               representation="Atoms('Si')")
pt.species_list.default_species = 'empty'

# Layers
layer = Layer(name='default')
layer.sites.append(Site(name='a', pos='0.5 0.5 0.5',
                        default_species='empty'))
pt.add_layer(layer)
pt.lattice.cell = np.diag([3, 3, 3])

# Parameters
pt.add_parameter(name= 'E0', value = 0.5)
pt.add_parameter(name='T', value = 300)

# Coords
center = pt.lattice.generate_coord('a.(0,0,0).default')

up = pt.lattice.generate_coord('a.(0,1,0).default')
down = pt.lattice.generate_coord('a.(0,-1,0).default')

left = pt.lattice.generate_coord('a.(-1,0,0).default')
right = pt.lattice.generate_coord('a.(1,0,0).default')

# Processes
pt.add_process(name='diffusion_up',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=up)],
               actions=[Action(species='ion', coord=up),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

pt.add_process(name='diffusion_down',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=down)],
               actions=[Action(species='ion', coord=down),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

pt.add_process(name='diffusion_left',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=left)],
               actions=[Action(species='ion', coord=left),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

pt.add_process(name='diffusion_right',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=right)],
               actions=[Action(species='ion', coord=right),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

###It's good to simply copy and paste the below lines between model creation files.
pt.filename = model_name + ".xml"
pt.backend = 'local_smart' #specifying is optional. local_smart is the dfault. Currently, the other options are 'lat_int' and 'otf'
pt.clear_model(model_name, backend=pt.backend) #This line is optional: if you are updating a model, this line will remove the old model before exporting the new one. It is convenent to always include this line because then you don't need to 'confirm' removing the old model.
pt.save()
kmcos.export(pt.filename + ' -b ' + pt.backend) #alternatively, one can use: kmcos.cli.main('export '+  pt.filename + ' -b' + pt.backend)
