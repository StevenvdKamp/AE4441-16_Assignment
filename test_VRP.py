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

    def test_get_a_dict(self):
        vrp = VRP.VRP("test cases/test_case_1.xlsx")
        a_dict = vrp.get_a_dict()

        self.assertDictEqual(a_dict, {1: 20, 2: 40, 3: 100, 4: 0, 5: 0})

    def test_get_c_dict(self):
        vrp = VRP.VRP("test cases/test_case_1.xlsx")
        c_dict = vrp.get_c_dict()

        self.assertDictEqual(c_dict, {1: 3, 2: 6, 3: 7, 4: 0, 5: 0})

    def test_get_r_dict(self):
        vrp = VRP.VRP("test cases/test_case_1.xlsx")
        r_dict = vrp.get_r_dict()

        self.assertDictEqual(r_dict, {(1, 2): 600, (1, 3): 400, (2, 3): 100, (4, 1): 10, (5, 1): 20,
                                      (2, 1): 600, (3, 1): 400, (3, 2): 100, (1, 4): 10, (1, 5): 20})

    def test_get_d_dict(self):
        vrp = VRP.VRP("test cases/test_case_1.xlsx")
        d_dict = vrp.get_d_dict()

        self.assertDictEqual(d_dict, {(1, 2): 4, (1, 3): 2, (2, 3): 3, (4, 1): 5, (5, 1): 10,
                                      (2, 1): 4, (3, 1): 2, (3, 2): 3, (1, 4): 5, (1, 5): 10})

# Running the tests
if __name__ == "__main__":
    unittest.main()