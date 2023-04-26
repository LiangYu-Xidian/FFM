from rdkit import Chem

suppl = Chem.SDMolSupplier('D:\TASK3\Data\PCQM4Mv2\pcqm4m-v2-train.sdf')
print("hhhhh")
for idx, mol in enumerate(suppl):
    conf = mol.GetConformer()
    atoms = mol.GetAtoms()
    print(idx)
    for s in atoms:
        print(conf.GetAtomPosition(conf,s))