import autode as ade
import numpy as np
import os

Cores = 8
ade.Config.n_cores = Cores

orca = ade.methods.ORCA()
xtb = ade.methods.XTB()

R1 = ade.Molecule('p-fluorophenol',smiles='C1=CC(=CC=C1O)F', solvent_name=None, charge=0)
P1 = ade.Molecule('p-fluorophenolate',smiles='C1=CC(=CC=C1[O-])F',solvent_name=None, charge=-1)

print(R1, flush=True)
print(P1, flush=True)

R1.optimise(method=xtb, n_cores=Cores)
P1.optimise(method=xtb, n_cores=Cores)

print('molecules have been optimised with XTB', flush=True)

R1.optimise(method=orca, keywords=ade.OptKeywords(['Opt', 'BP86', 'def2-SVP', 'def2/J', 'RIJCOSX', 'D4']), n_cores=Cores)
P1.optimise(method=orca, keywords=ade.OptKeywords(['Opt', 'BP86', 'def2-SVP', 'def2/J', 'RIJCOSX', 'D4']),n_cores=Cores)

print('molecules have been optimised with ORCA', flush=True)

CoIR1 = ade.Calculation(name=R1.name, molecule=R1, method=orca, keywords=ade.HessianKeywords(['Freq', 'PBE0', 'def2-SVP', 'def2/J', 'RIJCOSX', 'D4']), n_cores=Cores)
CoIP1 = ade.Calculation(name=P1.name, molecule=P1, method=orca, keywords=ade.HessianKeywords(['Freq', 'PBE0', 'def2-SVP', 'def2/J', 'RIJCOSX', 'D4']), n_cores=Cores)

print('Calculations have been carried out', flush=True)

CoIR1.output.filename = R1.name+'_hess_orca.out'
CoIP1.output.filename = P1.name+'_hess_orca.out'

print('calculations have been output to files', flush=True)


R1.calc_thermo(calc=CoIR1, n_cores=Cores)
P1.calc_thermo(calc=CoIP1, n_cores=Cores)

print('thermodynamic calculations have been carried out', flush=True)

GibbsR1 = R1.free_energy
GibbsP1 = P1.free_energy

GibbsR1_kcal = R1.free_energy.to('kcal')
GibbsP1_kcal = P1.free_energy.to('kcal')

print('gibbs free energies acquired', flush=True)

print(f'gibbsE {R1.name} = {GibbsR1} Ha', flush=True)
print(f'gibbsE {P1.name} = {GibbsP1} Ha', flush=True)

print(f'The absolute Gibbs free energy of  {R1.name} = {GibbsR1_kcal} kcal/mol', flush=True)
print(f'The absolute Gibbs free energy of  {P1.name} = {GibbsP1_kcal} kcal/mol', flush=True)

print('gibbs free energies printed', flush=True)
