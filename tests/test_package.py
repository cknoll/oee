import pyirk as p
import unittest
from pathlib import Path
from os.path import join as pjoin


PACKAGE_ROOT_PATH = Path(__file__).parent.parent.absolute().as_posix()
oee = p.irkloader.load_mod_from_path(pjoin(PACKAGE_ROOT_PATH, "oee.py"), prefix="oee")


class TestPackage01(unittest.TestCase):

    def test_001_subclass_relationship(self):

        # check that `ampere` is an instance of `SI unit` (however it is a `SI base unit`)
        self.assertTrue(p.is_instance_of(oee.I1204["ampere"], oee.I1103["SI unit"]))
