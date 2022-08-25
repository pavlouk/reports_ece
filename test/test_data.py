import unittest

from src import data


class DataLoadingTest(unittest.TestCase):
    def test_make_images(self):
        ic = data.ImageCollection()
        ic.make_images()
        self.assertEqual(len(ic.flir_images), 45)


if __name__ == "__main__":
    unittest.main()
