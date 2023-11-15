"""
Big O(1)
"""
import unittest

from typing import Dict


class HashTable:
    """
    the hash table class.
    """
    def __init__(self):
        self.hash_tale: Dict = {
            "payme": 1,
            "payze": 2,
            "upay": 3,
            "universal_bank": 4,
            "paynet": 5
        }

    def get_hash_table(self):
        """
        get hash table method returns key value pairs.
        """
        return self.hash_tale

    def get_value_by_key(self, key):
        """
        get hash table by key.
        """
        return self.hash_tale.get(key)


class TestHashTable(unittest.TestCase):
    """
    test the has table class.
    """
    def setUp(self):
        """
        setting up the hash table.
        """
        self.hash_table = HashTable()

    def test_get_hash_table(self):
        """
        test the get hash table method.
        """
        expected_hash_table: Dict = {
            "payme": 1,
            "payze": 2,
            "upay": 3,
            "universal_bank": 4,
            "paynet": 5
        }

        self.assertEqual(
            self.hash_table.get_hash_table(),
            expected_hash_table
        )

    def test_get_value_by_key(self):
        """
        test the get value by key.
        """
        self.assertEqual(self.hash_table.get_value_by_key("payme"), 1)
        self.assertEqual(self.hash_table.get_value_by_key("upay"), 3)
        self.assertEqual(self.hash_table.get_value_by_key("paynet"), 5)

        self.assertIsNone(self.hash_table.get_value_by_key("nonexistent_key"))


if __name__ == "__main__":
    unittest.main()
