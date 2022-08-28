import unittest

from src import data

class DataLoadingTest(unittest.TestCase):
    def test_image_all_images_count(self):
        # too much overhead for this test 
        # image collection should be constructed with arguments
        # and then filtered by accessors 
        ic = data.ImageCollection()
        self.assertEqual(len(ic.image_collection), 180)

    def test_load_by_single_id(self):
        ic = data.ImageCollection()
        ic.get_by_id("IR_2060.jpg")
        ic.image_collection
        self.assertEqual(len(ic.image_collection), 1) 
        self.assertEqual(ic.image_collection[0], "IR_2060.jpg")

if __name__ == "__main__":
    unittest.main()
