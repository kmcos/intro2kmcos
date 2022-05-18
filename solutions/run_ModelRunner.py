"""
Use the ModelRunner to generate an Arrhenius plot
"""

from kmcos.run import ModelRunner, PressureParameter, TemperatureParameter

class ScanKinetics(ModelRunner):
    p_O2gas = PressureParameter(1.e-1)
    T = TemperatureParameter(min=450, max=650, steps=20)
    p_COgas = PressureParameter(2.e-1)

if __name__ == "__main__":
    ScanKinetics().run(init_steps=1e7, sample_steps=1e7, cores=4)
