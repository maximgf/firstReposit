from Models.nomen import nomen_model
from Models.nomen_grope import nomen_group_model
from Models.organization import organization_model
from Models.recipe import recipe_model, recipe_row_model
from Models.unit import unit_model
from Src.settings_manager import settings_manager
from Src.Models import *


class test_models():

    def test_unit(self):
        units = unit_model(name='gram')

        assert units.name == 'gram'

    def test_big_unit(self):
        gram = unit_model(name='gram')
        kilogram = unit_model(base=gram, coef=1000, name='kilogram')

        gram_in_kilo = kilogram.to_base

        assert gram_in_kilo.name == 'gram'
        assert gram_in_kilo.base == None


    def test_biggest_unit(self):
        bit = unit_model(name='bit')
        bite = unit_model(name='bite', base=bit, coef=8)
        kilobite = unit_model(name='kilobite', base=bite, coef=1024)

        assert kilobite.to_base.to_base.name == 'bit'

    def test_organizations(self):
        manager = settings_manager()
        manager.open('settings.json')
        organ = organization_model(settings=manager.settings, name='org')

        assert all(filter(lambda x: x.startswith('_'), dir(organ)))

    def test_nomen_group(self):
        group = nomen_group_model(name='Group one')

        assert bool(group) == True

    def test_nomen(self):
        nom = nomen_model(name="nomen1", group = nomen_group_model('Group'), units=unit_model(name='unit'))

        assert bool(nom) == True

    def test_recipe_row(self):
        row = recipe_row_model(nomenculature=nomen_model(name="nomen1", group = nomen_group_model('Group'), units=unit_model(name='unit')),
        size=200, unit=unit_model.create_gramm())

        assert bool(row) == True

    def test_recipe(self):
        recept = recipe_model(
                name='ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ',
                rows=[recipe_row_model(
                nomenculature = nomen_model(name='Пшеничная мука', group=nomen_group_model.create_group(), units=unit_model.create_kilogramm()),
                unit=unit_model.create_gramm(),
                size=100
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Сахар', group=nomen_group_model.create_group(), units=unit_model.create_kilogramm()),
                unit=unit_model.create_gramm(),
                size=80
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Сливочное масло', group=nomen_group_model.create_group(), units=unit_model.create_gramm()),
                unit=unit_model.create_gramm(),
                size=70
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Яйца', group=nomen_group_model.create_group(), units=unit_model.create_count()),
                unit=unit_model.create_count(),
                size=1
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Ванилин', group=nomen_group_model.create_group(), units=unit_model.create_gramm()),
                unit=unit_model.create_gramm(),
                size=5
                )],)
        assert bool(recept) == True