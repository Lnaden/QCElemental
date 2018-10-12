# QCElemental

[![Build Status](https://travis-ci.org/MolSSI/QCElemental.svg?branch=master)](https://travis-ci.org/MolSSI/QCElemental)
[![codecov](https://codecov.io/gh/MolSSI/QCElemental/branch/master/graph/badge.svg)](https://codecov.io/gh/MolSSI/QCElemental)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MolSSI/QCElemental.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/QCElemental/context:python)
[![Documentation Status](https://readthedocs.org/projects/qcelemental/badge/?version=latest)](https://qcelemental.readthedocs.io/en/latest/?badge=latest)
[![Chat on Slack](https://img.shields.io/badge/chat-on_slack-green.svg?longCache=true&style=flat&logo=slack)](https://join.slack.com/t/qcdb/shared_invite/enQtNDIzNTQ2OTExODk0LWM3OTgxN2ExYTlkMTlkZjA0OTExZDlmNGRlY2M4NWJlNDlkZGQyYWUxOTJmMzc3M2VlYzZjMjgxMDRkYzFmOTE)

A Python interface to Periodic Table and Physical Constants data from
a reliable source (NIST srd144 and srd121, respectively;
[details](nist_data/README.md)) in a renewable
manner (class around NIST-published JSON file).

<!--# <img src="https://github.com/psi4/psi4media/blob/master/logos-psi4/psi4square.png" height=150>-->
# QCElemental

| **Status** | [![Travis build](https://img.shields.io/travis/MolSSI/QCElemental/master.svg)](https://travis-ci.org/MolSSI/QCElemental)  [![Codecov coverage](https://codecov.io/gh/MolSSI/QCElemental/branch/master/graph/badge.svg)](https://codecov.io/gh/MolSSI/QCElemental) [![LGTM analysis](https://img.shields.io/lgtm/grade/python/g/MolSSI/QCElemental.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/QCElemental/context:python) |
| :------ | :------- |
| **Latest Release** | [![Last release tag](https://img.shields.io/github/release/MolSSI/QCElemental.svg)](https://github.com/MolSSI/QCElemental/releases) [![Commits since release](https://img.shields.io/github/commits-since/MolSSI/QCElemental/latest.svg)](https://github.com/MolSSI/QCElemental/releases/tag) |
| **Communication** | [![docs latest](https://img.shields.io/badge/docs-latest-5077AB.svg?logo=read%20the%20docs)](https://readthedocs.org/projects/qcelemental/badge/?version=latest) [![dev chat on slack](https://img.shields.io/badge/chat-on_slack-808493.svg?logo=slack)](https://join.slack.com/t/qcdb/shared_invite/enQtNDIzNTQ2OTExODk0LWM3OTgxN2ExYTlkMTlkZjA0OTExZDlmNGRlY2M4NWJlNDlkZGQyYWUxOTJmMzc3M2VlYzZjMjgxMDRkYzFmOTE) |
| **Foundation** | [![license](https://img.shields.io/github/license/MolSSI/QCElemental.svg)](https://opensource.org/licenses/LGPL-3.0)  [![python](https://img.shields.io/badge/python-3.5+-blue.svg)](http://psicode.org/psi4manual/master/introduction.html#supported-systems) |
| **Installation** | [![Conda](https://img.shields.io/conda/v/psi4/qcelemental.svg)](https://anaconda.org/psi4/qcelemental) [![Anaconda-Server Badge](https://anaconda.org/psi4/qcelemental/badges/latest_release_relative_date.svg)](https://anaconda.org/psi4/qcelemental) |

<!--# <img src="https://github.com/psi4/psi4media/blob/master/logos-psi4/psi4square.png" height=150>-->
# QCElemental

[![Travis build](https://img.shields.io/travis/MolSSI/QCElemental/master.svg)](https://travis-ci.org/MolSSI/QCElemental) 
[![Codecov coverage](https://codecov.io/gh/MolSSI/QCElemental/branch/master/graph/badge.svg)](https://codecov.io/gh/MolSSI/QCElemental) 
[![LGTM analysis](https://img.shields.io/lgtm/grade/python/g/MolSSI/QCElemental.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/QCElemental/context:python)
[![docs latest](https://img.shields.io/badge/docs-latest-5077AB.svg?logo=read%20the%20docs)](https://readthedocs.org/projects/qcelemental/badge/?version=latest) 
[![chat on slack](https://img.shields.io/badge/chat-on_slack-808493.svg?logo=slack)](https://join.slack.com/t/qcdb/shared_invite/enQtNDIzNTQ2OTExODk0LWM3OTgxN2ExYTlkMTlkZjA0OTExZDlmNGRlY2M4NWJlNDlkZGQyYWUxOTJmMzc3M2VlYzZjMjgxMDRkYzFmOTE) 
<br>
[![Conda](https://img.shields.io/conda/v/psi4/qcelemental.svg)](https://anaconda.org/psi4/qcelemental)
[![Commits since release](https://img.shields.io/github/commits-since/MolSSI/QCElemental/latest.svg)](https://github.com/MolSSI/QCElemental/releases/tag)
[![python](https://img.shields.io/badge/python-3.5+-blue.svg)](http://python3statement.org/)

## Demo

### periodic table
```python
>>> import qcelemental as qcel
>>> qcel.periodictable.to_E('KRYPTON')
'Kr'
>>> qcel.periodictable.to_element(36)
'Krypton'
>>> qcel.periodictable.to_Z('kr84')
36
>>> qcel.periodictable.to_A('Kr')
84
>>> qcel.periodictable.to_A('D')
2
>>> qcel.periodictable.to_mass('kr', return_decimal=True)
Decimal('83.9114977282')
>>> qcel.periodictable.to_mass('kr84')
83.9114977282
>>> qcel.periodictable.to_mass('Kr86')
85.9106106269
```

### physical constants ([available](https://physics.nist.gov/cuu/Constants/Table/allascii.txt))
```python
>>> import qcelemental as qcel
>>> qcel.constants.Hartree_energy_in_eV
27.21138602
>>> qcel.constants.get('hartree ENERGY in ev')
27.21138602
>>> pc = qcel.constants.get('hartree ENERGY in ev', return_tuple=True)
>>> pc.lbl
'Hartree energy in eV'
>>> pc.data
Decimal('27.21138602')
>>> pc.units
'eV'
>>> pc.comment
'uncertainty=0.000 000 17'
```

