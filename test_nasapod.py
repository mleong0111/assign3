import unittest
import nasapod



class HomeViewTest(unittest.TestCase):

    def setUp(self):
    	self.app = nasapod.app.test_client()
    	self.app.testing = True



if __name__ == "__main__":
    unittest.main()
