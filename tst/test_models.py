from Models.abstract_references import abstract_referance
from Models.group_nomenclature import nomenclature_group_model
from Models.nomenclature import nomenclature_model
from Models.organization import organization_model
from Models.unit import unit_model
from src.settings_manager import settings_manager
from src.argument_exception import argument_exception
from Models import *
import unittest


class test_models(unittest.TestCase):

    def test_abs(self):
        abc = abstract_referance(name='name')

        assert abc.name == 'name'
        self.assertRaises(argument_exception, abstract_referance, name='1234567890'*10)

    def test_unit(self):
        units = unit_model(name='gramm', num=1000)

        assert units.num == 1000
        assert str(units) == "1000 gramm"

    def test_big_unit(self):
        gramm = unit_model(name='gramm', num=1010)
        kilogramm = unit_model(base=gramm, num=2, coefficient=1000, name='kilogramm')

        gramm_in_kilo = kilogramm.to_base

        assert gramm_in_kilo.name == 'gramm'
        assert gramm_in_kilo.base == None
        assert gramm_in_kilo.num == 2000

    def test_biggest_unit(self):
        bit = unit_model(name='bit')
        byte = unit_model(name='byte', base=bit, coefficient=8)
        kilobyte = unit_model(name='kilobyte', base=byte, coefficient=1024, num=3)

        assert kilobyte.to_base.to_base.name == 'bit'
        assert kilobyte.to_base.to_base.num == 24576

    def test_organizations(self):
        manager = settings_manager()
        manager.open('cfg\settings.json')
        organ = organization_model(settings=manager.settings, name='org')

        assert all(filter(lambda x: x.startswith('_'), dir(organ)))

    def test_nomenclature_group(self):
        group = nomenclature_group_model(name='Group one')

        assert bool(group) == True

    def test_nomenclature(self):
        nom = nomenclature_model(name="nomenclature1", full_name='big_nomenclature_2', group = nomenclature_group_model('Group'), units=unit_model(name='unit'))

        assert bool(nom) == True
