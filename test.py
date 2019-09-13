import unittest
import GameOfLife

class Test(unittest.TestCase):
	##### Canary Test #####
	def test_canary_1(self):
		self.assertTrue(True)
	
	## Universe Tests ##
	u = GameOfLife.Universe(10, 11)

	def test_universe_init(self):
		self.assertEqual(self.u.width, 10)
		self.assertEqual(self.u.height, 11)

	def test_universe_build_grid(self):
		self.u.build_grid()
		self.assertEqual(self.u.grid, [[col+1 for col in range(10)] for row in range(11)])

if __name__ == '__main__':
	unittest.main()