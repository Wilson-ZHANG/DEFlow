#When we face a new molecular dataset, Atom Type and Max Length are both essential.
#As ZINC250k
#atomic_num_list = [6, 7, 8, 9, 15, 16, 17, 35, 53, 0]  # 0 is for virtual node.
#max_atoms = 38
#import sys
import argparse
import pandas as pd
from rdkit import Chem
parser = argparse.ArgumentParser(description='Process some argv.')
parser.add_argument('input_file', metavar='N', type=str, nargs='+',
                    help='filename')
args = parser.parse_args()
#filename = args.input_file[0]
mol_smiles = pd.read_csv(args.input_file[0])['smiles']
#print(mol_smiles[2])
#print(type(mol_smiles[2]))
#early_mol = Chem.MolFromSmiles(mol_smiles[2])
#print(early_mol)
#atoms = early_mol.GetAtoms()
#for at in atoms:
#    print(at.GetAtomicNum())
#    print(at.GetSymbol())i
#print(pd.read_csv(args.input_file[0]).iloc[0:1])
print(pd.read_csv(args.input_file[0]).columns)
def atomic_num_list_output():
    out = []
    for smi in mol_smiles:
        try:
            mol = Chem.MolFromSmiles(smi)
            atoms = mol.GetAtoms()
            for at in atoms:
                out.append(at.GetAtomicNum())
        except:
            pass
    out.append(0)
    return list(set(out))

def max_atom_cal():
    max_atoms = 0
   # i = 0
    for smi in mol_smiles:
        try:
            mol = Chem.MolFromSmiles(smi)
 #           print(i,mol.GetNumAtoms())
            #print('smiles molecule: ',smi)
   #         i += 1
            if(mol.GetNumAtoms() > max_atoms):
                max_atoms = mol.GetNumAtoms()
        except:
  #          print(i)
            pass
    return max_atoms
#print('max_atoms: ',max_atoms)
print(atomic_num_list_output())
print(max_atom_cal())
