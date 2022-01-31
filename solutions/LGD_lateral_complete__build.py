from itertools import product

import kmcos
from kmcos.cli import main as cli_main
from kmcos.types import Action, Condition, Layer, Site, Species, create_kmc_model


model_name = __file__[+0:-3] # This is the python file name, the brackets cut off zero characters from the beginning and three character from the end (".py").  To manually name the model just place a string here.
model_name = model_name.replace("_complete__build", "")
# Project
kmc_model = create_kmc_model()
kmc_model.set_meta(
    author='Michael Seibt',
    email='michael.seibt@tum.de',
    model_name='LGD_lateral',
    model_dimension=2
)

# Species
kmc_model.add_species(
    Species(name='empty', color='#d3d3d3'),
    Species(name='ion', color='#0000ff', representation="Atoms('Si')"),
    Species(name='source', color='#00ff00', representation="Atoms('Au')"),
    Species(name='drain', color='#ff0000', representation="Atoms('Ag')")
)
kmc_model.species_list.default_species = 'empty'

# Layer and Coordinates
layer = Layer(name='simple_cubic')
layer.add_site(Site(name='hollow', pos='0.5 0.5 0.5'))
kmc_model.add_layer(layer)

center = kmc_model.lattice.generate_coord('hollow')
bottom = kmc_model.lattice.generate_coord('hollow.(0,-1,0)')
top = kmc_model.lattice.generate_coord('hollow.(0,+1,0)')
left = kmc_model.lattice.generate_coord('hollow.(-1,0,0)')
right = kmc_model.lattice.generate_coord('hollow.(+1,0,0)')

# Parameters
kmc_model.add_parameter(name='E0', value=0.5)
kmc_model.add_parameter(name='T', value=300)
kmc_model.add_parameter(name='eps_f', value=0.0, adjustable=True, min=-0.05, max=0.05)
kmc_model.add_parameter(name='e_int', value=0.002, adjustable=True, min=0.00, max=0.01)
kmc_model.add_parameter(name='thetaS', value=1.0, adjustable=True, min=0.0, max=1.0)
kmc_model.add_parameter(name='thetaD', value=0.0, adjustable=True, min=0.0, max=1.0)

# Processes
names = ['top', 'left', 'bottom', 'right']
delta_Es = ['E0', 'E0+eps_f', 'E0', 'E0-eps_f']
coordinates = [top, left, bottom, right]
for coordinate_name, delta_E, coordinate in zip(names, delta_Es, coordinates):
    for i, conf in enumerate(product(['empty', 'ion'], repeat=3)):
        diffusion_condition = [
            Condition(species='ion', coord=center),
            Condition(species='empty', coord=coordinate)
        ]
        diffusion_action = [
            Condition(species='ion', coord=coordinate),
            Condition(species='empty', coord=center)
        ]
        temp_coords = coordinates[:]
        temp_coords.remove(coordinate)
        for conf_species, temp_coord in zip(conf, temp_coords):
            diffusion_condition.append(Condition(species=conf_species, coord=temp_coord))

        nns = conf.count('ion')
        kmc_model.add_process(
            name='diffusion_%s_%s' % (coordinate_name, i),
            conditions=diffusion_condition,
            actions=diffusion_action,
            rate_constant='1/(beta*h)*exp(-beta*((%s)-%s*e_int)*eV)' % (delta_E, nns)
        )

        # if left == empty, make another process where condition is left == source
        # important for first step after emission -> otherwise deadlock
        if left in temp_coords:
            left_index = temp_coords.index(left)
            if conf[left_index] == 'empty':
                diffusion_condition = [
                    Condition(species='ion', coord=center),
                    Condition(species='empty', coord=coordinate)
                ]
                for conf_species, temp_coord in zip(conf, temp_coords):
                    if temp_coord == left:
                        conf_species = 'source'
                    diffusion_condition.append(Condition(species=conf_species, coord=temp_coord))

                kmc_model.add_process(
                    name='diffusion_%s_%s_source' % (coordinate_name, i),
                    conditions=diffusion_condition,
                    actions=diffusion_action,
                    rate_constant='1/(beta*h)*exp(-beta*((%s)-%s*e_int)*eV)' % (delta_E, nns)
                )

source_entry_conditions = [
    Condition(species='empty', coord=center),
    Condition(species='source', coord=left)
]
source_exit_conditions = [
    Condition(species='ion', coord=center),
    Condition(species='source', coord=left)
]
kmc_model.add_process(
    name='source_entry',
    conditions=source_entry_conditions,
    actions=source_exit_conditions,
    rate_constant='thetaS*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)'
)
kmc_model.add_process(
    name='source_exit',
    conditions=source_exit_conditions,
    actions=source_entry_conditions,
    rate_constant='(1-thetaS)*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)'
)

drain_entry_conditions = [
    Condition(species='ion', coord=center),
    Condition(species='drain', coord=right)
]
drain_exit_conditions = [
    Action(species='empty', coord=center),
    Action(species='drain', coord=right)
]
kmc_model.add_process(
    name='drain_exit',
    conditions=drain_entry_conditions,
    actions=drain_exit_conditions,
    rate_constant='(1-thetaD)*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)',
    tof_count={'current': 1}
)

kmc_model.add_process(
    name='drain_entry',
    conditions=drain_exit_conditions,
    actions=drain_entry_conditions,
    rate_constant='thetaD*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)',
    tof_count={'current': -1}
)

# Build model
file_name = kmc_model.meta.model_name + '.xml'
kmc_model.save(file_name)
if False:  # build the exported .xml directly
    cli_main('export %s' % file_name)
kmc_model.print_statistics()
kmc_model.backend = 'local_smart'
kmcos.export(file_name + ' b' + kmc_model.backend)
