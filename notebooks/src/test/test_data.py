import unittest

from ..data import ImageCollection


class TestData(unittest.TestCase):
    def test_count(self):
        ic = ImageCollection("IR_2060.jpg")
        self.assertEqual(len(ic.image_collection), 1)

    def test_id(self):
        ic = ImageCollection("IR_2060.jpg")
        single = ic.get_single_image(id="IR_2060.jpg")
        self.assertEqual(single.ir_id, "IR_2060.jpg")
        self.assertEqual(single.csv_id, "CSV_2060.csv")
        self.assertEqual(single.dc_id, "DC_2061.jpg")

    def test_csv_load(self):
        ic = ImageCollection("all")
        self.assertEqual(len(ic.df), 180)


if __name__ == "__main__":
    unittest.main()
