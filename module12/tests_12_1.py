import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_walker = Runner('Igor')
        for _ in range(0, 10):
            test_walker.walk()

        self.assertEqual(test_walker.distance, 50)

    def test_run(self):
        test_runner = Runner('Igor')
        for _ in range(0, 10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    def test_challenge(self):
        first_runner = Runner('Igor')

        second_runner = Runner('Artem')

        for _ in range(0, 10):
            first_runner.run()

            second_runner.walk()

        self.assertNotEqual(first_runner.distance, second_runner.distance)
