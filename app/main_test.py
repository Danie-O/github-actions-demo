from main import return_reversed_string,get_mode
import os
import unittest


class TestMain(unittest.TestCase):
    # test route functions in main
    def test_return_reversed_string(self):
        random_string = "This is a test string"
        random_reversed_string = "gnirts tset a si sihT"
        self.assertEqual(random_reversed_string,
                         return_reversed_string(random_string)
        )

    def test_get_mode(self):
        self.assertEqual(os.environ.get("MODE"), get_mode())


if __name__ == "__main__":
    unittest.main()