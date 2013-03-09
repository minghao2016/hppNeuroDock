# Copyright (C) 2013 by Eka A. Kurniawan
# eka.a.kurniawan(ta)gmail(tod)com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import unittest
from Ligand import *

class LigandAtoms(unittest.TestCase):
    def testRead(self):
        ligand = Ligand()
        ligand.read_pdbqt("./Inputs/ind.pdbqt")

        exp = ['N',
               'C',
               'C',
               'C',
               'OA',
               'N',
               'N',
               'C',
               'C',
               'C',
               'C',
               'C',
               'C',
               'C',
               'C',
               'OA',
               'N',
               'C',
               'C',
               'C',
               'A',
               'A',
               'A',
               'A',
               'A',
               'A',
               'HD',
               'HD',
               'OA',
               'HD',
               'A',
               'A',
               'A',
               'A',
               'A',
               'A',
               'C',
               'A',
               'A',
               'NA',
               'A',
               'A',
               'A',
               'C',
               'C',
               'C',
               'C',
               'OA',
               'HD']
        for i, atom in enumerate(ligand.atoms):
            self.assertEquals(atom.type, exp[i])

        exp = ['Axis3: -3.8840, -2.4210, -3.9000',
               'Axis3: -3.6460, -0.9580, -4.0310',
               'Axis3: -3.2320, -0.3420, -5.3520',
               'Axis3: -3.0130, 1.1320, -5.1400',
               'Axis3: -2.0700, 1.5250, -4.4640',
               'Axis3: -3.8810, 1.9530, -5.6980',
               'Axis3: -1.9620, -1.0900, -5.6540',
               'Axis3: -1.9050, -2.5470, -5.3780',
               'Axis3: -2.6800, -3.0650, -4.1840',
               'Axis3: -1.3110, -0.8220, -6.9200',
               'Axis3: 0.1790, -0.4990, -6.8030',
               'Axis3: 0.7400, 0.9070, -6.5230',
               'Axis3: 2.2520, 1.1350, -6.3910',
               'Axis3: 2.5990, 2.6090, -6.1250',
               'Axis3: 2.8660, 0.2770, -5.2910',
               'Axis3: 2.3500, 0.2330, -4.1640',
               'Axis3: 4.0270, -0.2960, -5.5960',
               'Axis3: 4.8900, -0.8600, -4.5710',
               'Axis3: 6.3610, -0.6770, -4.9020',
               'Axis3: 7.0790, -1.7600, -4.1290',
               'Axis3: 6.2030, -2.9780, -3.9830',
               'Axis3: 6.3700, -4.3170, -3.7160',
               'Axis3: 5.2370, -5.1380, -3.7120',
               'Axis3: 3.9630, -4.6090, -3.9720',
               'Axis3: 3.7660, -3.2640, -4.2540',
               'Axis3: 4.8000, -2.3820, -4.2870',
               'Axis3: -4.6640, 1.4910, -6.1820',
               'Axis3: 4.3220, -0.3400, -6.5820',
               'Axis3: 0.4840, -0.8300, -8.1240',
               'Axis3: 0.5170, 0.0270, -8.6940',
               'Axis3: 4.0610, 2.8330, -5.9890',
               'Axis3: 4.9780, 2.4140, -6.9530',
               'Axis3: 6.3390, 2.6110, -6.7670',
               'Axis3: 6.7740, 3.2360, -5.5960',
               'Axis3: 5.8560, 3.6650, -4.6300',
               'Axis3: 4.4900, 3.4600, -4.8320',
               'Axis3: -4.5580, -2.8860, -2.6820',
               'Axis3: -5.9930, -2.4600, -2.3510',
               'Axis3: -7.1180, -2.9970, -2.9930',
               'Axis3: -8.4590, -2.6730, -2.7310',
               'Axis3: -8.5480, -1.7190, -1.7190',
               'Axis3: -7.4700, -1.1430, -1.0390',
               'Axis3: -6.1680, -1.5200, -1.3590',
               'Axis3: -3.9080, 3.3800, -5.7390',
               'Axis3: -5.2730, 3.7850, -6.3260',
               'Axis3: -2.8790, 3.9270, -6.4870',
               'Axis3: -3.8780, 4.0050, -4.4130',
               'Axis3: 6.5610, -0.7430, -6.3060',
               'Axis3: 6.5100, 0.2050, -6.7060']
        for i, atom in enumerate(ligand.atoms):
            self.assertEquals(str(atom.tcoord), exp[i])

        exp = [0.096,
               0.307,
               0.2,
               0.242,
               -0.271,
               -0.351,
               -0.395,
               0.148,
               0.292,
               0.149,
               0.136,
               0.047,
               0.084,
               0.052,
               0.222,
               -0.273,
               -0.35,
               0.147,
               0.149,
               0.073,
               -0.047,
               0.008,
               0.001,
               0.001,
               0.01,
               -0.027,
               0.163,
               0.163,
               -0.394,
               0.21,
               -0.057,
               0.007,
               0.001,
               0.0,
               0.001,
               0.007,
               0.312,
               -0.013,
               0.125,
               -0.273,
               0.116,
               0.02,
               0.012,
               0.022,
               0.037,
               0.037,
               0.037,
               -0.393,
               0.21]
        for i, atom in enumerate(ligand.atoms):
            self.assertEquals(atom.charge, exp[i])

        exp = [0.096,
               0.307,
               0.2,
               0.242,
               0.271,
               0.351,
               0.395,
               0.148,
               0.292,
               0.149,
               0.136,
               0.047,
               0.084,
               0.052,
               0.222,
               0.273,
               0.35,
               0.147,
               0.149,
               0.073,
               0.047,
               0.008,
               0.001,
               0.001,
               0.01,
               0.027,
               0.163,
               0.163,
               0.394,
               0.21,
               0.057,
               0.007,
               0.001,
               0.0,
               0.001,
               0.007,
               0.312,
               0.013,
               0.125,
               0.273,
               0.116,
               0.02,
               0.012,
               0.022,
               0.037,
               0.037,
               0.037,
               0.393,
               0.21]
        for i, atom in enumerate(ligand.atoms):
            self.assertEquals(atom.abs_charge, exp[i])

    def testUpdateTcoordFromModel(self):
        ligand = Ligand()
        ligand.read_pdbqt("./Inputs/ind.pdbqt")
        ligand.update_tcoord_model("./Results/ind_1.model")

        exp = ['Axis3: 0.2650, 6.2150, -11.8050',
               'Axis3: 1.6440, 6.5520, -11.3580',
               'Axis3: 2.5770, 5.4910, -10.8120',
               'Axis3: 3.8610, 6.1570, -10.3960',
               'Axis3: 3.8790, 6.9140, -9.4330',
               'Axis3: 4.9330, 5.8950, -11.1170',
               'Axis3: 1.7850, 4.9560, -9.6490',
               'Axis3: 0.3230, 4.7560, -9.8090',
               'Axis3: -0.4250, 5.7310, -10.6940',
               'Axis3: 2.3400, 3.8350, -8.9190',
               'Axis3: 2.3890, 4.0350, -7.4040',
               'Axis3: 3.5380, 4.7410, -6.6620',
               'Axis3: 3.4900, 4.9260, -5.1390',
               'Axis3: 4.7390, 5.6420, -4.5980',
               'Axis3: 2.2500, 5.6920, -4.6940',
               'Axis3: 1.9290, 6.7510, -5.2540',
               'Axis3: 1.6390, 5.2110, -3.6150',
               'Axis3: 0.6620, 5.9970, -2.8790',
               'Axis3: 0.7240, 5.7290, -1.3860',
               'Axis3: -0.6400, 6.1130, -0.8570',
               'Axis3: -1.7010, 5.8730, -1.9010',
               'Axis3: -3.0650, 5.7010, -1.9350',
               'Axis3: -3.6710, 5.4540, -3.1710',
               'Axis3: -2.9080, 5.3860, -4.3470',
               'Axis3: -1.5290, 5.5470, -4.3420',
               'Axis3: -0.8420, 5.7860, -3.1940',
               'Axis3: 4.7660, 5.2960, -11.9390',
               'Axis3: 1.8650, 4.2600, -3.2920',
               'Axis3: 2.4490, 2.6750, -7.0990',
               'Axis3: 2.0460, 2.1300, -7.8750',
               'Axis3: 4.6930, 5.8290, -3.1250',
               'Axis3: 4.9250, 7.0630, -2.5180',
               'Axis3: 4.9090, 7.1840, -1.1350',
               'Axis3: 4.6580, 6.0480, -0.3630',
               'Axis3: 4.4170, 4.8090, -0.9700',
               'Axis3: 4.4350, 4.7040, -2.3620',
               'Axis3: -0.4560, 7.2290, -12.5830',
               'Axis3: 0.1500, 7.8440, -13.8500',
               'Axis3: 0.7060, 9.1300, -13.8860',
               'Axis3: 1.2960, 9.7510, -14.9980',
               'Axis3: 1.2650, 8.9090, -16.1080',
               'Axis3: 0.7270, 7.6180, -16.1420',
               'Axis3: 0.1600, 7.0740, -14.9930',
               'Axis3: 6.2880, 6.3080, -10.9420',
               'Axis3: 6.6440, 6.0580, -9.4640',
               'Axis3: 6.5040, 7.6350, -11.2720',
               'Axis3: 7.2500, 5.4970, -11.6940',
               'Axis3: 1.0740, 4.3740, -1.1440',
               'Axis3: 0.2230, 3.7950, -1.1340']
        for i, atom in enumerate(ligand.atoms):
            self.assertEquals(str(atom.tcoord), exp[i])

def suite():
    suite1 = unittest.makeSuite(LigandAtoms)
    return unittest.TestSuite((suite1, ))

if __name__ == '__main__':
    unittest.main()