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


if __name__ == "__main__":
    unittest.main()
