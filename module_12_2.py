import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усейн', 10)
        self.andrey = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    def test_1(self):
        first_round = runner_and_tournament.Tournament(90, self.usain, self.nik)
        result = first_round.start()
        list_runner = list(result.values())
        self.assertTrue(list_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    def test_2(self):
        second_round = runner_and_tournament.Tournament(90, self.andrey, self.nik)
        result = second_round.start()
        list_runner = list(result.values())
        self.assertTrue(list_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    def test_3(self):
        third_round = runner_and_tournament.Tournament(90, self.usain, self.andrey, self.nik)
        result = third_round.start()
        list_runner = list(result.values())
        self.assertTrue(list_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for key, value in value.items():
                res[key] = str(value)
            print(res)

if __name__ == '__main__':
    unittest.main()