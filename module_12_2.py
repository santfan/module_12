# Импортируем модули runner_and_tournament и unittest
import runner_and_tournament
import unittest

# Объявим класс тестирования
class TournamentTest(unittest.TestCase):
    # При первом запуске очистим all_results
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    # Для всех тест-сьютов сформируем экзмепляры бегунов
    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усейн', 10)
        self.andrey = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    # Первый тест
    def test_1(self):
        # Выбор участников забега
        first_round = runner_and_tournament.Tournament(90, self.usain, self.nik)
        # Старт забега
        result = first_round.start()
        list_runner = list(result.values())
        # Проверка корректной работы
        self.assertTrue(list_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    # Второй тест
    def test_2(self):
        # Выбор участников забега
        second_round = runner_and_tournament.Tournament(90, self.andrey, self.nik)
        # Старт забега
        result = second_round.start()
        list_runner = list(result.values())
        # Проверка корректной работы
        self.assertTrue(list_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    # Третий тест
    def test_3(self):
        # Выбор участников забега
        third_round = runner_and_tournament.Tournament(90, self.usain, self.andrey, self.nik)
        # Старт забега
        result = third_round.start()
        list_runner = list(result.values())
        # Проверка корректной работы
        self.assertTrue(list_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    # Декоратор итогов тестирования
    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for key, value in value.items():
                res[key] = str(value)
            # Вывод итогов забега
            print(res)

# Точка входа в процедуру
if __name__ == '__main__':
    unittest.main()