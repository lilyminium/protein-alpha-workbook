from openff.toolkit import Molecule
import numpy as np
import click


@click.command()
@click.option(
    "--output-filename",
    "-o",
    type=str,
    default="assigned_charges.txt",
    help="Filename to write the assigned charges to.",
)
def main(
    output_filename: str = "assigned_charges.txt",
):
    mapped_smiles = "[H:38][c:9]1[c:10]([c:11]([c:5]([c:6]([c:8]1[H:37])[Cl:7])[C:3](=[O:4])[O:2][C:1]([H:34])([H:35])[H:36])[N:12]2[C:13]([C:14]([C:15]([C:32]([C:33]2([H:60])[H:61])([H:58])[H:59])([H:44])[C:16]([H:45])([H:46])[N:17]([H:47])[C:18](=[O:19])[C:20]3([C:21]([C:22]3([H:50])[H:51])([H:48])[H:49])[N:23]([H:52])[C:24](=[O:25])[C:26]4=[C:27]([N:28]([C:30](=[N:31]4)[H:57])[C:29]([H:54])([H:55])[H:56])[H:53])([H:42])[H:43])([H:40])[H:41])[H:39]"
    offmol = Molecule.from_mapped_smiles(
        mapped_smiles,
        allow_undefined_stereo=True,
    )
    offmol.assign_partial_charges("openff-gnn-am1bcc-1.0.0.pt")
    charges = [q.m for q in offmol.partial_charges]
    np.savetxt(output_filename, charges)



if __name__ == "__main__":
    main()
