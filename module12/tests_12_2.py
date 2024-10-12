import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in list(self.participants):
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.useyn = Runner('Усейн', 10)
        self.andrew = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.useyn, self.nik)
        result = tournament.start()
        self.__class__.all_results["Usain_and_Nick"] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_andrew_and_nick(self):
        tournament = Tournament(90, self.andrew, self.nik)
        result = tournament.start()
        self.__class__.all_results["Andrew_and_Nick"] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_usain_andrew_and_nick(self):
        tournament = Tournament(90, self.useyn, self.andrew, self.nik)
        result = tournament.start()
        self.__class__.all_results["Usain_Andrew_and_Nick"] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()
