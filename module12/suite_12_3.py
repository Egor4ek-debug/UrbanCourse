import unittest
import tests_12_1
import tests_12_2

testST = unittest.TestSuite()

testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)

