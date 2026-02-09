import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_single_title(self):
        md_path = "./test_md_files/single_title.md"
        title = extract_title(md_path)
        self.assertEqual(title, "single title")

    def test_double_title(self):
        md_path = "./test_md_files/double_title.md"
        title = extract_title(md_path)
        self.assertEqual(title, "single title")

    def test_no_title(self):
        with self.assertRaises(ValueError) as context:
            md_path = "./test_md_files/no_title.md"
            title = extract_title(md_path)
