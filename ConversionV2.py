from molfunc import CoreMolecule, CombinedMolecule

aBiCyDNH_atom_to_del = [16, 17, 36, 37, 38, 57, 127, 58, 74, 75, 94, 95, 96, 115, 116, 117]
aBiCyDNH2_atom_to_del = [16, 17, 36, 37, 38, 57, 127, 58, 74, 75, 94, 95, 96, 115, 116, 117]
aI45Me2CyDNH_atom_to_del = [16, 17, 36, 37, 38, 57, 127, 58, 74, 75, 94, 95, 96, 115, 116, 117]
aI45Me2CyDNH2_atom_to_del = [16, 17, 36, 37, 38, 57, 127, 58, 74, 75, 94, 95, 96, 115, 116, 117]
aICyDNH_atom_to_del = [16, 17, 36, 37, 38, 57, 131, 58, 74, 75, 94, 95, 96, 115, 116, 117]
aICyDNH2_atom_to_del = [16, 17, 36, 37, 38, 57, 131, 58, 74, 75, 94, 95, 96, 115, 116, 117]
bBiCyDNH_atom_to_del = [20, 21, 22, 39, 40, 56, 57, 76, 77, 78, 97, 98, 99, 112, 113, 132, 133, 134, 150]
bBiCyDNH2_atom_to_del = [20, 21, 22, 39, 40, 56, 57, 76, 77, 78, 97, 98, 99, 112, 113, 132, 133, 134, 150]
bI45Me2CyDNH_atom_to_del = [20, 21, 22, 39, 40, 56, 57, 76, 77, 78, 97, 98, 99, 112, 113, 132, 133, 134, 156]
bI45Me2CyDNH2_atom_to_del = [20, 21, 22, 41, 42, 43, 59, 60, 79, 80, 81, 100, 101, 102, 117, 118, 137, 138, 139]
bICyDNH_atom_to_del = [20, 21, 22, 41, 42, 43, 59, 60, 79, 80, 81, 100, 101, 102, 117, 118, 137, 138, 139]
bICyDNH2_atom_to_del = [20, 21, 22, 41, 42, 43, 59, 60, 79, 80, 81, 100, 101, 102, 117, 118, 137, 138, 139]

aBiCyDNH_core = CoreMolecule(xyz_filename='aBiCyDNH.xyz', atoms_to_del=aBiCyDNH_atom_to_del)
aBiCyDNH2_core = CoreMolecule(xyz_filename='aBiCyDNH2.xyz', atoms_to_del=aBiCyDNH2_atom_to_del)
aI45Me2CyDNH_core = CoreMolecule(xyz_filename='aI45Me2CyDNH.xyz', atoms_to_del=aI45Me2CyDNH_atom_to_del)
aI45Me2CyDNH2_core = CoreMolecule(xyz_filename='aI45Me2CyDNH2.xyz', atoms_to_del=aI45Me2CyDNH2_atom_to_del)
aICyDNH_core = CoreMolecule(xyz_filename='aICyDNH.xyz', atoms_to_del=aICyDNH_atom_to_del)
aICyDNH2_core = CoreMolecule(xyz_filename='aICyDNH2.xyz', atoms_to_del=aICyDNH2_atom_to_del)
bBiCyDNH_core = CoreMolecule(xyz_filename='bBiCyDNH.xyz', atoms_to_del=bBiCyDNH_atom_to_del)
bBiCyDNH2_core = CoreMolecule(xyz_filename='bBiCyDNH2.xyz', atoms_to_del=bBiCyDNH2_atom_to_del)
bI45Me2CyDNH_core = CoreMolecule(xyz_filename='bI45Me2CyDNH.xyz', atoms_to_del=bI45Me2CyDNH_atom_to_del)
bI45Me2CyDNH2_core = CoreMolecule(xyz_filename='bI45Me2CyDNH2.xyz', atoms_to_del=bI45Me2CyDNH2_atom_to_del)
bICyDNH_core = CoreMolecule(xyz_filename='bICyDNH.xyz', atoms_to_del=bICyDNH_atom_to_del)
bICyDNH2_core = CoreMolecule(xyz_filename='bICyDNH2.xyz', atoms_to_del=bICyDNH2_atom_to_del)

aBiCyDNH_OMe = CombinedMolecule(aBiCyDNH_core, frag_smiles='C[*]', name='aBiCyDNH_New')
aBiCyDNH2_OMe = CombinedMolecule(aBiCyDNH2_core, frag_smiles='C[*]', name='aBiCyDNH2_New')
aI45Me2CyDNH_OMe = CombinedMolecule(aI45Me2CyDNH_core, frag_smiles='C[*]', name='aI45Me2CyDNH_New')
aI45Me2CyDNH2_OMe = CombinedMolecule(aI45Me2CyDNH2_core, frag_smiles='C[*]', name='aI45Me2CyDNH2_New')
aICyDNH_OMe = CombinedMolecule(aICyDNH_core, frag_smiles='C[*]', name='aICyDNH_New')
aICyDNH2_OMe = CombinedMolecule(aICyDNH2_core, frag_smiles='C[*]', name='aICyDNH2_New')
bBiCyDNH_OMe = CombinedMolecule(bBiCyDNH_core, frag_smiles='C[*]', name='aICyDNH_New')
bBiCyDNH2_OMe = CombinedMolecule(bBiCyDNH2_core, frag_smiles='C[*]', name='aICyDNH2_New')
bI45Me2CyDNH_OMe = CombinedMolecule(bI45Me2CyDNH_core, frag_smiles='C[*]', name='bI45Me2CyDNH_New')
bI45Me2CyDNH2_OMe = CombinedMolecule(bI45Me2CyDNH2_core, frag_smiles='C[*]', name='bI45Me2CyDNH2_New')
bICyDNH_OMe = CombinedMolecule(bICyDNH_core, frag_smiles='C[*]', name='bICyDNH_New')
bICyDNH2_OMe = CombinedMolecule(bICyDNH2_core, frag_smiles='C[*]', name='bICyDNH2_New')

aBiCyDNH_OMe.print_xyz_file()
aBiCyDNH2_OMe.print_xyz_file()
aI45Me2CyDNH_OMe.print_xyz_file()
aI45Me2CyDNH2_OMe.print_xyz_file()
aICyDNH_OMe.print_xyz_file()
aICyDNH2_OMe.print_xyz_file()
bBiCyDNH_OMe.print_xyz_file()
bBiCyDNH2_OMe.print_xyz_file()
bI45Me2CyDNH_OMe.print_xyz_file()
bI45Me2CyDNH2_OMe.print_xyz_file()
bICyDNH_OMe.print_xyz_file()
bICyDNH2_OMe.print_xyz_file()