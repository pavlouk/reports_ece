import unittest

from ..detection import RAW_DIR, SRC_DIR, Detection, DetectionCollection


class TestDetection(unittest.TestCase):
    def test_here(self):
        self.assertEqual(SRC_DIR, "Detection")

    def test_raw(self):
        self.assertEqual(RAW_DIR.as_posix, "DetectionCollection")


if __name__ == "__main__":
    unittest.main()
