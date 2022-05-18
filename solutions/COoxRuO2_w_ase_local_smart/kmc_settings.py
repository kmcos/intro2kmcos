model_name = 'COoxRuO2_w_ase'
simulation_size = 20
random_seed = 1

def setup_model(model):
    """Write initialization steps here.
       e.g. ::
    model.put([0,0,0,model.lattice.default_a], model.proclist.species_a)
    """
    #from setup_model import setup_model
    #setup_model(model)
    pass

# Default history length in graph
hist_length = 30

parameters = {
    "A":{"value":"20.0616*angstrom**2", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_CO_bridge":{"value":"-1.6", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_CO_cus":{"value":"-1.3", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_COdiff_bridge_bridge":{"value":"0.6", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_COdiff_bridge_cus":{"value":"1.6", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_COdiff_cus_bridge":{"value":"1.3", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_COdiff_cus_cus":{"value":"1.7", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_COgas":{"value":"0.00", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_O2gas":{"value":"0.00", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_O_bridge":{"value":"-2.3", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_O_cus":{"value":"-1.0", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_Odiff_bridge_bridge":{"value":"0.7", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_Odiff_bridge_cus":{"value":"2.3", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_Odiff_cus_bridge":{"value":"1.0", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_Odiff_cus_cus":{"value":"1.6", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_react_Obridge_CObridge":{"value":"1.5", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_react_Obridge_COcus":{"value":"1.2", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_react_Ocus_CObridge":{"value":"0.8", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_react_Ocus_COcus":{"value":"0.9", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "T":{"value":"450", "adjustable":True, "min":"300.0", "max":"1500.0","scale":"linear"},
    "p_COgas":{"value":"1", "adjustable":True, "min":"1e-13", "max":"100.0","scale":"log"},
    "p_O2gas":{"value":"1", "adjustable":True, "min":"1e-15", "max":"100.0","scale":"log"},
    }

rate_constants = {
    "CO_adsorption_bridge":("p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)", True),
    "CO_adsorption_cus":("p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)", True),
    "CO_desorption_bridge":("p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)*exp(beta*(E_CO_bridge-GibbsGas_COgas)*eV)", True),
    "CO_desorption_cus":("p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)*exp(beta*(E_CO_cus-GibbsGas_COgas)*eV)", True),
    "COdiff_bridge_down":("(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_bridge)*eV)", True),
    "COdiff_bridge_left":("(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_bridge)*eV)", True),
    "COdiff_bridge_right":("(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_cus)*eV)", True),
    "COdiff_bridge_up":("(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_bridge)*eV)", True),
    "COdiff_cus_down":("(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_cus)*eV)", True),
    "COdiff_cus_left":("(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_cus)*eV)", True),
    "COdiff_cus_right":("(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_bridge)*eV)", True),
    "COdiff_cus_up":("(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_cus)*eV)", True),
    "O2_adsorption_bridge_right":("p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)", True),
    "O2_adsorption_bridge_up":("p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)", True),
    "O2_adsorption_cus_right":("p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)", True),
    "O2_adsorption_cus_up":("p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)", True),
    "O2_desorption_bridge_right":("p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)*exp(beta*((E_O_bridge+E_O_cus)-GibbsGas_O2gas)*eV)", True),
    "O2_desorption_bridge_up":("p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)*exp(beta*(2*E_O_bridge-GibbsGas_O2gas)*eV)", True),
    "O2_desorption_cus_right":("p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)*exp(beta*((E_O_cus+E_O_bridge)-GibbsGas_O2gas)*eV)", True),
    "O2_desorption_cus_up":("p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)*exp(beta*(2*E_O_cus-GibbsGas_O2gas)*eV)", True),
    "Odiff_bridge_down":("(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_bridge)*eV)", True),
    "Odiff_bridge_left":("(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_bridge)*eV)", True),
    "Odiff_bridge_right":("(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_cus)*eV)", True),
    "Odiff_bridge_up":("(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_bridge)*eV)", True),
    "Odiff_cus_down":("(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_cus)*eV)", True),
    "Odiff_cus_left":("(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_cus)*eV)", True),
    "Odiff_cus_right":("(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_bridge)*eV)", True),
    "Odiff_cus_up":("(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_cus)*eV)", True),
    "React_bridge_down":("(beta*h)**(-1)*exp(-beta*E_react_Obridge_CObridge*eV)", True),
    "React_bridge_left":("(beta*h)**(-1)*exp(-beta*E_react_Ocus_CObridge*eV)", True),
    "React_bridge_right":("(beta*h)**(-1)*exp(-beta*E_react_Obridge_COcus*eV)", True),
    "React_bridge_up":("(beta*h)**(-1)*exp(-beta*E_react_Obridge_CObridge*eV)", True),
    "React_cus_down":("(beta*h)**(-1)*exp(-beta*E_react_Ocus_COcus*eV)", True),
    "React_cus_left":("(beta*h)**(-1)*exp(-beta*E_react_Obridge_COcus*eV)", True),
    "React_cus_right":("(beta*h)**(-1)*exp(-beta*E_react_Ocus_CObridge*eV)", True),
    "React_cus_up":("(beta*h)**(-1)*exp(-beta*E_react_Ocus_COcus*eV)", True),
    }

site_names = ['ruo2_bridge', 'ruo2_cus']
representations = {
    "CO":"""Atoms('CC',[[0,0,0],[0,0,1.2]])""",
    "O":"""Atoms('O')""",
    "empty":"""""",
    }

lattice_representation = """[Atoms(symbols='N2Ru2',
          pbc=np.array([False, False, False]),
          cell=np.array(      ([6.43, 3.12, 20.0])),
          scaled_positions=np.array(      [[0.6898882, 0.0, 0.6390143], [0.3039135, 0.0, 0.6390143], [0.0, 0.0, 0.6390143], [0.4969008, 0.4994377, 0.6390143]]),
),]"""

species_tags = {
    "CO":"""""",
    "O":"""""",
    "empty":"""""",
    }

tof_count = {
    "React_bridge_down":{'CO_oxidation': 1},
    "React_bridge_left":{'CO_oxidation': 1},
    "React_bridge_right":{'CO_oxidation': 1},
    "React_bridge_up":{'CO_oxidation': 1},
    "React_cus_down":{'CO_oxidation': 1},
    "React_cus_left":{'CO_oxidation': 1},
    "React_cus_right":{'CO_oxidation': 1},
    "React_cus_up":{'CO_oxidation': 1},
    }

xml = """<?xml version="1.0" ?>
<kmc version="(0, 3)">
    <meta author="Mie Andersen" email="mie@phys.au.dk" model_name="COoxRuO2_w_ase" model_dimension="2" debug="0"/>
    <species_list default_species="empty">
        <species name="CO" representation="Atoms('CC',[[0,0,0],[0,0,1.2]])" color="#000000" tags=""/>
        <species name="O" representation="Atoms('O')" color="#ff0000" tags=""/>
        <species name="empty" representation="" color="#ffffff" tags=""/>
    </species_list>
    <parameter_list>
        <parameter name="A" value="20.0616*angstrom**2" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_CO_bridge" value="-1.6" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_CO_cus" value="-1.3" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_COdiff_bridge_bridge" value="0.6" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_COdiff_bridge_cus" value="1.6" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_COdiff_cus_bridge" value="1.3" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_COdiff_cus_cus" value="1.7" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_COgas" value="0.00" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_O2gas" value="0.00" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_O_bridge" value="-2.3" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_O_cus" value="-1.0" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_Odiff_bridge_bridge" value="0.7" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_Odiff_bridge_cus" value="2.3" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_Odiff_cus_bridge" value="1.0" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_Odiff_cus_cus" value="1.6" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_react_Obridge_CObridge" value="1.5" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_react_Obridge_COcus" value="1.2" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_react_Ocus_CObridge" value="0.8" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="E_react_Ocus_COcus" value="0.9" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="T" value="450" adjustable="True" min="300.0" max="1500.0" scale="linear"/>
        <parameter name="p_COgas" value="1" adjustable="True" min="1e-13" max="100.0" scale="log"/>
        <parameter name="p_O2gas" value="1" adjustable="True" min="1e-15" max="100.0" scale="log"/>
    </parameter_list>
    <lattice cell_size="6.43 0.0 0.0 0.0 3.12 0.0 0.0 0.0 20.0" default_layer="ruo2" substrate_layer="ruo2" representation="[Atoms(symbols='N2Ru2',
          pbc=np.array([False, False, False]),
          cell=np.array(      ([6.43, 3.12, 20.0])),
          scaled_positions=np.array(      [[0.6898882, 0.0, 0.6390143], [0.3039135, 0.0, 0.6390143], [0.0, 0.0, 0.6390143], [0.4969008, 0.4994377, 0.6390143]]),
),]">
        <layer name="ruo2" color="#ffffff">
            <site pos="0.0 0.5 0.7" type="bridge" tags="" default_species="default_species"/>
            <site pos="0.5 0.5 0.7" type="cus" tags="" default_species="default_species"/>
        </layer>
    </lattice>
    <process_list>
        <process rate_constant="p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)" name="CO_adsorption_bridge" enabled="True">
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)" name="CO_adsorption_cus" enabled="True">
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)*exp(beta*(E_CO_bridge-GibbsGas_COgas)*eV)" name="CO_desorption_bridge" enabled="True">
            <condition species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)*exp(beta*(E_CO_cus-GibbsGas_COgas)*eV)" name="CO_desorption_cus" enabled="True">
            <condition species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_bridge)*eV)" name="COdiff_bridge_down" enabled="True">
            <condition species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
            <action species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_bridge)*eV)" name="COdiff_bridge_left" enabled="True">
            <condition species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_cus)*eV)" name="COdiff_bridge_right" enabled="True">
            <condition species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_bridge)*eV)" name="COdiff_bridge_up" enabled="True">
            <condition species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_cus)*eV)" name="COdiff_cus_down" enabled="True">
            <condition species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
            <action species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_cus)*eV)" name="COdiff_cus_left" enabled="True">
            <condition species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
            <action species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_bridge)*eV)" name="COdiff_cus_right" enabled="True">
            <condition species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_cus)*eV)" name="COdiff_cus_up" enabled="True">
            <condition species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
        </process>
        <process rate_constant="p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)" name="O2_adsorption_bridge_right" enabled="True">
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)" name="O2_adsorption_bridge_up" enabled="True">
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
            <action species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
        </process>
        <process rate_constant="p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)" name="O2_adsorption_cus_right" enabled="True">
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)" name="O2_adsorption_cus_up" enabled="True">
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
            <action species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
        </process>
        <process rate_constant="p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)*exp(beta*((E_O_bridge+E_O_cus)-GibbsGas_O2gas)*eV)" name="O2_desorption_bridge_right" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)*exp(beta*(2*E_O_bridge-GibbsGas_O2gas)*eV)" name="O2_desorption_bridge_up" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
        </process>
        <process rate_constant="p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)*exp(beta*((E_O_cus+E_O_bridge)-GibbsGas_O2gas)*eV)" name="O2_desorption_cus_right" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="p_O2gas*bar*A/4./sqrt(2*pi*umass*m_O2/beta)*exp(beta*(2*E_O_cus-GibbsGas_O2gas)*eV)" name="O2_desorption_cus_up" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_bridge)*eV)" name="Odiff_bridge_down" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
            <action species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_bridge)*eV)" name="Odiff_bridge_left" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_cus)*eV)" name="Odiff_bridge_right" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_bridge)*eV)" name="Odiff_bridge_up" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_cus)*eV)" name="Odiff_cus_down" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
            <action species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_cus)*eV)" name="Odiff_cus_left" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_bridge)*eV)" name="Odiff_cus_right" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_cus)*eV)" name="Odiff_cus_up" enabled="True">
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*E_react_Obridge_CObridge*eV)" name="React_bridge_down" enabled="True" tof_count="{'CO_oxidation': 1}">
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
            <condition species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*E_react_Ocus_CObridge*eV)" name="React_bridge_left" enabled="True" tof_count="{'CO_oxidation': 1}">
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*E_react_Obridge_COcus*eV)" name="React_bridge_right" enabled="True" tof_count="{'CO_oxidation': 1}">
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <condition species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*E_react_Obridge_CObridge*eV)" name="React_bridge_up" enabled="True" tof_count="{'CO_oxidation': 1}">
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <condition species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="0 1 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*E_react_Ocus_COcus*eV)" name="React_cus_down" enabled="True" tof_count="{'CO_oxidation': 1}">
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
            <condition species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*E_react_Obridge_COcus*eV)" name="React_cus_left" enabled="True" tof_count="{'CO_oxidation': 1}">
            <condition species="O" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
            <condition species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*E_react_Ocus_CObridge*eV)" name="React_cus_right" enabled="True" tof_count="{'CO_oxidation': 1}">
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="CO" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="bridge" coord_offset="1 0 0"/>
        </process>
        <process rate_constant="(beta*h)**(-1)*exp(-beta*E_react_Ocus_COcus*eV)" name="React_cus_up" enabled="True" tof_count="{'CO_oxidation': 1}">
            <condition species="O" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <condition species="CO" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="ruo2" coord_name="cus" coord_offset="0 1 0"/>
        </process>
    </process_list>
    <output_list/>
</kmc>
"""
if __name__ == "__main__":
    #benchmark if kmc_settings.py is run without additional arguments, else call cli with additional argument provided.
    import sys
    if len(sys.argv) == 1:
        from kmcos import cli
        cli.main("benchmark")
    if len(sys.argv) == 2:
        from kmcos import cli
        cli.main(sys.argv[1])
