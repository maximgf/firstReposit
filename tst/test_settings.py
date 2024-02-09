from src.settings import settings
from src.settings_manager import settings_manager
import unittest, os, random


class test_settings(unittest.TestCase):
    
    
    #
    # Провеиить корректность заполнения поля first_name
    #
    def test_check_first_name(self):
        # Подготовка
        item = settings()
        
        # Действие
        item.first_name = "a  "
        
        # Проверка
        assert item.first_name == "a"

    #
    # Проверить, что settings_manager инстанциируется только один раз
    #
    def test_check_create_manager(self):
        # Подготовка
        manager1 = settings_manager()
        manager2 = settings_manager()
        
        # Действие
        
        # Проверки
        print(str(manager1.number))
        print(str(manager2.number))
    
        assert manager1.number == manager2.number

    
    #
    # Проверить корректность загрузки настроек
    #
    def test_check_open_settings(self):
        # Подготовка
        item = settings_manager()
        
        # Действие
        result = item.open(f"{os.curdir}/./cfg/settings.json")

        # Проверка
        assert result == True


    # 
    # Проверить, что все поля настроек не пусты
    #
    def test_check_settings_fields_nonempty(self):
        # Подготовка
        man = settings_manager()
        settings = None

        # Действие
        man.open(f"{os.curdir}/./cfg/settings.json")
        settings = man.settings
        dict = settings.__dict__

        # Проверка
        for key in dict.keys():
            assert len(str(dict[key])) != 0

    
    #
    #   Проверить, что менеджер настроек может открыть файл
    #       с любым названием и в любой папке
    #
    def test_settings_any_filename(self):
        # Подготовка
        if not os.path.exists("..\\.test_data"):
            os.mkdir("..\\.test_data")
        alp = "abcdefghijklmnopqrstuvwxyz"
        dirname = f"{os.getcwd()}\\..\\.test_data\\"
        dirname += ''.join(random.choice(alp) for _ in range(6))
        filename = f"{dirname}\\"
        filename += ''.join(random.choice(alp) for _ in range(6)) + ".json"
        os.mkdir(dirname)
        print(filename)
        f = open(filename, "w", encoding="UTF-8")
        f2 = open(f"{os.getcwd()}\\cfg\\settings.json", encoding="UTF-8")
        f.write(f2.read())
        f.close()
        f2.close()

        # Действие
        man = settings_manager()
        man.open(filename)

        # Проверка
        assert settings is not None

        # Очистка
        os.remove(filename)
        os.removedirs(dirname)