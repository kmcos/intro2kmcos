"""
Generate a kmos model for simple crystal growth using
an adsorption-desorption Solid-on-Solid (SOS) model.

Adsorption rate is constant, and desorption rate follow
an Arrhenius like rate, that considers atractive nearest
neighbor interactions

Juan M. Lorenzi
TU Munich
16.05.2016
"""

import kmcos
from kmcos.types import *
import itertools

def main():
    model_name = __file__[+0:-3] # This is the python file name, the brackets cut off zero characters from the beginning and three character from the end (".py").  To manually name the model just place a string here.
    model_name = model_name.replace("__build", "")
    kmc_model = kmcos.create_kmc_model(model_name)

    # Define project meta
    kmc_model.meta.author = 'Juan M. Lorenzi'
    kmc_model.meta.email = 'jmlorenzi@gmail.com'
    kmc_model.meta.model_name = 'SOS_adsdes'
    kmc_model.meta.model_dimension = 3
    kmc_model.meta.debug = 0

    # Add species
    kmc_model.add_species(name='empty', color='#ffffff')
    kmc_model.add_species(name='Pt', color = '#0000ff', representation = "Atoms('Pt')")

    kmc_model.add_species(name='sub', color='#00ff00', representation = "Atoms('Pd')")

    # Add sites and layer
    layer = Layer(name='default')
    layer.sites.append(Site(name='sc'))
    kmc_model.add_layer(layer)

    # Define the unit cell size for better visualization
    kmc_model.layer_list.cell = 2.7*np.eye(3)

    kmc_model.species_list.default_species = 'empty'

    # Parameters
    kmc_model.add_parameter(name='T', value=200, adjustable=True, min=200., max=500.)
    kmc_model.add_parameter(name='kads', value=3e-3, adjustable=True, min = 1e-5, max=1e0, scale='log')

    kmc_model.add_parameter(name='E_des', value=1.0)
    kmc_model.add_parameter(name='E_int', value=0.5)

    # Auxiliary coordinates
    central = kmc_model.lattice.generate_coord('sc')
    up = kmc_model.lattice.generate_coord('sc.(0,0,1)')
    down = kmc_model.lattice.generate_coord('sc.(0,0,-1)')
    xp = kmc_model.lattice.generate_coord('sc.(1,0,0)')
    xm = kmc_model.lattice.generate_coord('sc.(-1,0,0)')
    yp = kmc_model.lattice.generate_coord('sc.(0,1,0)')
    ym = kmc_model.lattice.generate_coord('sc.(0,-1,0)')

    xpd = kmc_model.lattice.generate_coord('sc.(1,0,-1)')
    xmd = kmc_model.lattice.generate_coord('sc.(-1,0,-1)')
    ypd = kmc_model.lattice.generate_coord('sc.(0,1,-1)')
    ymd = kmc_model.lattice.generate_coord('sc.(0,-1,-1)')


    # Processes

    # Adsorption
    condition_list = [ Condition(coord=central, species='empty'),
                       Condition(coord=down, species='Pt')]
    action_list = [Action(coord=central, species='Pt')]

    kmc_model.add_process(name = 'Ads',
                   rate_constant = 'kads',
                   condition_list = condition_list,
                   action_list = action_list,
                   tof_count = {'Adsorption' : 1,
                                'Growth' : 1}
                   )

    # Auxiliary adsorption into substrate
    condition_list = [ Condition(coord=central, species='empty'),
                       Condition(coord=down, species='sub')]
    action_list = [Action(coord=central, species='Pt')]

    kmc_model.add_process(name = 'Ads_sub',
                   rate_constant = 'kads',
                   condition_list = condition_list,
                   action_list = action_list,
                   )


    # Desorption

    conds_base = [ Condition(coord=central, species='Pt'),
                   Condition(coord=up, species='empty'),]

    action_list = [ Condition(coord=central, species='empty') ]

    # We need to consider all possible configurations of
    # the NNs of the central site
    nns = [xp, yp, xm, ym]

    proc_counter = 0
    for conf in itertools.product(['empty', 'Pt'], repeat=len(nns)):
        nr_nns = conf.count('Pt')
        conds_extra = []
        for i, spec in enumerate(conf):
            conds_extra.append(Condition(coord=nns[i], species=spec))

        rate = '1/(beta*h)*exp(-beta*(E_des+{}*E_int)*eV)'.format(nr_nns)
        proc = Process(name = 'Des_{:03d}'.format(proc_counter),
                       condition_list = conds_base + conds_extra,
                       action_list = action_list,
                       rate_constant = rate,
                       tof_count = {'Desorption' : 1,
                                    'Growth' : -1})
        kmc_model.add_process(proc)
        proc_counter += 1

    # Save the model to an xml file
    ###It's good to simply copy and paste the below lines between model creation files.
    kmc_model.print_statistics()
    kmc_model.clear_model(model_name, backend=kmc_model.backend) #This line is optional: if you are updating a model, this line will remove the old model before exporting the new one. It is convenent to always include this line because then you don't need to 'confirm' removing the old model.
    kmc_model.save_model()
    kmcos.compile(kmc_model)

if __name__ == '__main__':
    main()
