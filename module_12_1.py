# Импортируем класс из файла runner.py и нужный модуль
import runner
import unittest

# Объявим класс тестера класса
class RunnerTest(unittest.TestCase):

    # Тестируем функцию walk
    def test_walk(self):
        # Экземпляр класса Runner
        walker = runner.Runner('name')
        # Функцию запускаем 10 раз
        for __ in range(10):
            walker.walk()
        # Сравниваем с эталоном
        self.assertEquals(walker.distance, 50)

    # Тестируем функцию run
    def test_run(self):
        # Экземпляр класса Runner
        runner_ = runner.Runner('name')
        # Функцию запускаем 10 раз
        for __ in range(10):
            runner_.run()
        # Сравниваем с эталоном
        self.assertEqual(runner_.distance, 100)

    # Тестируем обе функции
    def test_chalenge(self):
        # 2 экземпляра класса Runner
        walker_1 = runner.Runner('name')
        runner_1 = runner.Runner('name')
        # Функцию запускаем 10 раз
        for __ in range(10):
            # Функция прогулки
            walker_1.walk()
            # Функция бегуна
            runner_1.run()
        # Результаты работы двух функций НЕ должны быть равны
        self.assertNotEquals(walker_1.distance, runner_1.distance)

# Входим в процедуру
if __name__ == '__main__':
    unittest.main()

