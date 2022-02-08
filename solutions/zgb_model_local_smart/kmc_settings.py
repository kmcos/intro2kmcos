model_name = 'zgb_model'
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
    "kfast":{"value":"10000000000.0", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "kslow":{"value":"1e-10", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "yCO":{"value":"0.5", "adjustable":True, "min":"0.0", "max":"1.0","scale":"linear"},
    }

rate_constants = {
    "CO_ads":("yCO", True),
    "CO_des":("kslow", True),
    "CO_oxi_00":("kfast", True),
    "CO_oxi_01":("kfast", True),
    "CO_oxi_02":("kfast", True),
    "CO_oxi_03":("kfast", True),
    "O2_ads_00":("0.5*(1-yCO)", True),
    "O2_ads_01":("0.5*(1-yCO)", True),
    "O2_des_00":("kslow", True),
    "O2_des_01":("kslow", True),
    }

site_names = ['fcc100_hol']
representations = {
    "CO":"""Atoms('N',[[0.,0.,0.]])""",
    "O":"""Atoms('O',[[0.,0.,0.]])""",
    "empty":"""""",
    }

lattice_representation = """"""

species_tags = {
    "CO":"""""",
    "O":"""""",
    "empty":"""""",
    }

tof_count = {
    "CO_oxi_00":{'CO_oxidation': 1},
    "CO_oxi_01":{'CO_oxidation': 1},
    "CO_oxi_02":{'CO_oxidation': 1},
    "CO_oxi_03":{'CO_oxidation': 1},
    }

xml = """<?xml version="1.0" ?>
<kmc version="(0, 3)">
    <meta author="Juan M. Lorenzi" debug="0" email="jmlorenzi@gmail.com" model_dimension="2" model_name="zgb_model"/>
    <species_list default_species="empty">
        <species color="#0000ff" name="CO" representation="Atoms('N',[[0.,0.,0.]])" tags=""/>
        <species color="#ff0000" name="O" representation="Atoms('O',[[0.,0.,0.]])" tags=""/>
        <species color="#dddddd" name="empty" representation="" tags=""/>
    </species_list>
    <parameter_list>
        <parameter adjustable="False" max="0.0" min="0.0" name="kfast" scale="linear" value="10000000000.0"/>
        <parameter adjustable="False" max="0.0" min="0.0" name="kslow" scale="linear" value="1e-10"/>
        <parameter adjustable="True" max="1.0" min="0.0" name="yCO" scale="linear" value="0.5"/>
    </parameter_list>
    <lattice cell_size="1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0" default_layer="fcc100" representation="" substrate_layer="fcc100">
        <layer color="#ffffff" name="fcc100">
            <site default_species="default_species" pos="0.5 0.5 0.5" tags="" type="hol"/>
        </layer>
    </lattice>
    <process_list>
        <process enabled="True" name="CO_ads" rate_constant="yCO">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="CO"/>
        </process>
        <process enabled="True" name="CO_des" rate_constant="kslow">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="CO"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="CO_oxi_00" rate_constant="kfast" tof_count="{'CO_oxidation': 1}">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="CO"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="1 0 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="1 0 0" species="empty"/>
        </process>
        <process enabled="True" name="CO_oxi_01" rate_constant="kfast" tof_count="{'CO_oxidation': 1}">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="CO"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 1 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 1 0" species="empty"/>
        </process>
        <process enabled="True" name="CO_oxi_02" rate_constant="kfast" tof_count="{'CO_oxidation': 1}">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="CO"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="-1 0 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="-1 0 0" species="empty"/>
        </process>
        <process enabled="True" name="CO_oxi_03" rate_constant="kfast" tof_count="{'CO_oxidation': 1}">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="CO"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 -1 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 -1 0" species="empty"/>
        </process>
        <process enabled="True" name="O2_ads_00" rate_constant="0.5*(1-yCO)">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="1 0 0" species="O"/>
        </process>
        <process enabled="True" name="O2_ads_01" rate_constant="0.5*(1-yCO)">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 1 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 1 0" species="O"/>
        </process>
        <process enabled="True" name="O2_des_00" rate_constant="kslow">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="O"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="1 0 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="1 0 0" species="empty"/>
        </process>
        <process enabled="True" name="O2_des_01" rate_constant="kslow">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="O"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 1 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 1 0" species="empty"/>
        </process>
    </process_list>
    <output_list/>
</kmc>
"""
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        from kmcos import cli
        cli.main("benchmark")
    if len(sys.argv) == 2:
        from kmcos import cli
        cli.main(sys.argv[1])
