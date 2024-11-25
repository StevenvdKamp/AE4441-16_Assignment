import unittest
import VRP

class test_VRP(unittest.TestCase):

    def test_get_s_dict(self):
        vrp = VRP.VRP("test cases/test_case_1.xlsx")
        s_dict = vrp.get_s_dict()

        self.assertDictEqual(s_dict, {1: 4, 2: 5})

    def test_get_z_dict(self):
        vrp = VRP.VRP("test cases/test_case_1.xlsx")
        z_dict = vrp.get_z_dict()

        self.assertDictEqual(z_dict, {1: 5, 2: 4})

# Running the tests
if __name__ == "__main__":
    unittest.main()