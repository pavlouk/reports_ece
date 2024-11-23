import unittest

from ..data import ImageCollection


class TestData(unittest.TestCase):
    def test_count(self):
        ic = ImageCollection()
        self.assertEqual(len(ic.image_collection), 180)

    def test_id(self):
        ic = ImageCollection(ir_id="IR_2060.jpg")
        single = ic.get_single_image(id="IR_2060.jpg")
        self.assertEqual(single.ir_id, "IR_2060.jpg")
        self.assertEqual(single.csv_id, "CSV_2060.csv")
        self.assertEqual(single.dc_id, "DC_2061.jpg")


if __name__ == "__main__":
    unittest.main()
