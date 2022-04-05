import autode as ade
import numpy as np
import os

Cores = 36
ade.Config.n_cores = Cores

orca = ade.methods.ORCA()
xtb = ade.methods.XTB()

MoI1 = ade.Molecule('aBiCyDNH.xyz', solvent_name=None, charge=0)

print(MoI1, flush=True)

MoI1.optimise(method=xtb, n_cores=Cores)

print('molecules have been optimised with XTB', flush=True)

MoI1.optimise(method=orca, keywords=ade.OptKeywords(['Opt', 'BP86', 'def2-SVP', 'def2/J', 'RIJCOSX', 'D4']), n_cores=Cores)

print('molecules have been optimised with ORCA', flush=True)

CoI1 = ade.Calculation(name=MoI1.name, molecule=MoI1, method=orca, keywords=ade.HessianKeywords(['Freq', 'PBE0', 'def2-SVP', 'def2/J', 'RIJCOSX', 'D4']), n_cores=Cores)

print('Calculations have been carried out', flush=True)

CoI1.output.filename = MoI1.name+'_hess_orca.out'

print('calculations have been output to files', flush=True)

MoI1.calc_thermo(calc=CoI1, n_cores=Cores)

print('thermodynamic calculations have been carried out', flush=True)

GibbsE1 = MoI1.free_energy

GibbsE1_kcal = MoI1.free_energy.to('kcal')

print('gibbs free energies acquired', flush=True)

print(f'gibbsE {MoI1.name} = {GibbsE1} Ha', flush=True)

print(f'The absolute Gibbs free energy of  {MoI1.name} = {GibbsE1_kcal} kcal/mol', flush=True)

print('gibbs free energies printed', flush=True)
