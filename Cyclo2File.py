import autode as ade
import numpy as np
import os

Cores = 36
ade.Config.n_cores = Cores

orca = ade.methods.ORCA()
xtb = ade.methods.XTB()

MoI2 = ade.Molecule('aBiCyDNH2.xyz', solvent_name=None, charge=1)

print(MoI2, flush=True)

MoI2.optimise(method=xtb, n_cores=Cores)

print('molecules have been optimised with XTB', flush=True)

MoI2.optimise(method=orca, keywords=ade.OptKeywords(['Opt', 'BP86', 'def2-SVP', 'def2/J', 'RIJCOSX', 'D4']), n_cores=Cores)

print('molecules have been optimised with ORCA', flush=True)

CoI2 = ade.Calculation(name=MoI2.name, molecule=MoI2, method=orca, keywords=ade.HessianKeywords(['Freq', 'PBE0', 'def2-SVP', 'def2/J', 'RIJCOSX', 'D4']), n_cores=Cores)

print('Calculations have been carried out', flush=True)

CoI2.output.filename = MoI2.name+'_hess_orca.out'

print('calculations have been output to files', flush=True)

MoI2.calc_thermo(calc=CoI2, n_cores=Cores)

print('thermodynamic calculations have been carried out', flush=True)

GibbsE2 = MoI2.free_energy

GibbsE2_kcal = MoI2.free_energy.to('kcal')

print('gibbs free energies acquired', flush=True)

print(f'gibbsE {MoI2.name} = {GibbsE2} Ha', flush=True)

print(f'The absolute Gibbs free energy of  {MoI2.name} = {GibbsE2_kcal} kcal/mol', flush=True)

print('gibbs free energies printed', flush=True)
