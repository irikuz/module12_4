import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    def test_wolk(self):
        try:
            r1 = Runner('Boris', -10)
            for i in range(10):
                i = r1.walk()
            self.assertEqual(i, 100)
            logging.info(f'"test_walk" выполнен успешно {r1}')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            r2 = Runner(name=6, speed=10)
            for i in range(10):
                i = r2.run()
            self.assertEqual(i, 200)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            return 0


first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)

t = Tournament(101, first, second)
print(t.start())

logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")
