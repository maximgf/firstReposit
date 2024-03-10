import datetime
from Logics.reports.converter.convertor_basic import convertor_basic
from Logics.reports.converter.convertor_datetime import convertor_datetime
from Logics.reports.converter.convertor_models import convertor_models
from Logics.reports.report import report
from Logics.reports.report_csv import report_csv
from Logics.reports.report_factory import report_factory
from Logics.reports.report_json import report_json
from Logics.reports.report_markdown import report_markdown
from Models.unit import unit_model
from Src.settings_manager import settings_manager
from Src.Logics.start_factory import start_factory
from Storage.Storage import storage
from Src.exceptions import argument_exception

class test_models():

    def test_report(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        self.assertRaises(TypeError, report.__init__, factory.storage)

    def test_report_csv(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        csv = report_csv(factory.storage, manager.settings)

        assert csv.create(storage.unit_key()) != ''
        assert csv.create(storage.nomenculature_key()) != ''
    
    def test_report_markdown(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        csv = report_markdown(factory.storage)

        assert csv.create(storage.unit_key()) != ''
        assert csv.create(storage.nomenculature_key()) != ''

    def test_report_json(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        csv = report_json(factory.storage)

        print(csv.create(storage.recipe_key()))

        with open('something.json', 'w') as f:
            f.write(csv.create(storage.recipe_key()))

        assert csv.create(storage.unit_key()) != ''
        assert csv.create(storage.nomenculature_key()) != ''

    def test_report_factory(self):
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        factory = report_factory()

        result = factory.create(manager.settings.report_format, start.storage)

        assert bool(result) == True
        print(result.create(storage.unit_key()))
        assert len(result.create(storage.unit_key())) > 0

    def test_convertor_basic(self):
        assert convertor_basic.convert(5) == 5
        assert convertor_basic.convert('g') == 'g'
        self.assertRaises(argument_exception,convertor_basic.convert,datetime.datetime.now())

    def test_convertor_datetime(self):
        data = convertor_datetime.convert(datetime.datetime.now())

        assert data is not None
        assert 'Год' in data.keys() and 'Секунды' in data.keys()

    def test_convertor_model(self):
        data = convertor_models.convert(unit_model.create_gramm())

        assert data is not None
        
        kilodata = convertor_models.convert(unit_model.create_kilogramm())

        assert kilodata is not None