import sys

import pytest
from utils_compare import *

import qcelemental

subject1 = """
3 au

Co 0 0 0
H  2 0 0
h_OTher -2 0 0
"""

ans1_au = """3 au
CoH2
Co                    0.000000000000     0.000000000000     0.000000000000
H                     2.000000000000     0.000000000000     0.000000000000
H                    -2.000000000000     0.000000000000     0.000000000000
"""

ans1_ang = """3
CoH2
Co                    0.000000000000     0.000000000000     0.000000000000
H                     1.058354421340     0.000000000000     0.000000000000
H                    -1.058354421340     0.000000000000     0.000000000000
"""

ans1c_ang = """3
CoH2
59Co                      0.00000000         0.00000000         0.00000000
1H                        1.05835442         0.00000000         0.00000000
1H_other                 -1.05835442         0.00000000         0.00000000
"""

subject2 = """
Co 0 0 0
no_reorient
--
@H  1.05835442134 0 0
h_OTher -1.05835442134 0 0
"""

ans2_au = """3 au
CoH2
Co                    0.000000000000     0.000000000000     0.000000000000
@H                    2.000000000000     0.000000000000     0.000000000000
H                    -2.000000000000     0.000000000000     0.000000000000
"""

ans2_ang = """3
CoH2
Co                    0.000000000000     0.000000000000     0.000000000000
Gh(1)                 1.058354421340     0.000000000000     0.000000000000
H                    -1.058354421340     0.000000000000     0.000000000000
"""

ans2c_ang = """2
CoH2
Co                    0.000000000000     0.000000000000     0.000000000000
H                    -1.058354421340     0.000000000000     0.000000000000
"""


@pytest.mark.parametrize("inp,expected", [
    ((subject1, {'dtype': 'xyz', 'units': 'Bohr'}), ans1_au),
    ((subject1, {'dtype': 'xyz', 'units': 'Angstrom'}), ans1_ang),
    ((subject1, {'dtype': 'xyz', 'prec': 8, 'atom_format': '{elea}{elem}{elbl}'}), ans1c_ang),
    ((subject2, {'dtype': 'xyz', 'units': 'Bohr'}), ans2_au),
    ((subject2, {'dtype': 'xyz', 'units': 'Angstrom', 'ghost_format': 'Gh({elez})'}), ans2_ang),
    ((subject2, {'dtype': 'xyz', 'units': 'Angstrom', 'ghost_format': ''}), ans2c_ang),
])
def test_to_string_xyz(inp, expected):
    molrec = qcelemental.molparse.from_string(inp[0])
    smol = qcelemental.molparse.to_string(molrec['qm'], **inp[1])

    assert compare_strings(expected, smol, sys._getframe().f_code.co_name)
