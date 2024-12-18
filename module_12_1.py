import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walker = runner.Runner('name')
        for __ in range(10):
            walker.walk()
        self.assertEquals(walker.distance, 50)

    def test_run(self):
        runner_ = runner.Runner('name')
        for __ in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    def test_chalenge(self):
        walker_1 = runner.Runner('name')
        runner_1 = runner.Runner('name')
        for __ in range(10):
            walker_1.walk()
            runner_1.run()
        self.assertNotEquals(walker_1.distance, runner_1.distance)

if __name__ == '__main__':
    unittest.main()

