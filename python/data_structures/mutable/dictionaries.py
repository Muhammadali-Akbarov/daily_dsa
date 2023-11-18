""""
dictionaries in python are a versatile and widely used data structure,
here's an advanced overview of python dictionaries:
    internal working:
        hashing:
            when a key-value pair is added to a dictionary,
            python first applies a hash function to the key,
            this hash function computes an integer value (hash) unique to the key (as much as possible),

        index calculation:
            the hash value is then used to calculate an index in an internal array (or hash table),
            this index determines where the key-value pair is stored in the table.

        collision handling:
            sometimes, two different keys may produce the same hash value (a situation known as a collision).
            python handles collisions using a method called "open addressing," which involves probing for the next available
            slot in the hash table.

        dynamic resizing:
            to maintain efficient operations, python dictionaries dynamically resize,
            when the table becomes too crowded (determined by a factor called the load factor),
            python increases the size of the hash table and rehashes all keys to maintain efficiency.

    how works with big O:
        lookup (my_dict.get(key, None)) O(1)
        rehashing O(n)
        deleting O(n)
"""
import unittest


class TestDictionaryMethods(unittest.TestCase):
    """
    test dictionary methods.
    """

    def test_insertion(self) -> None:
        """
        test insertion to dictionary O(1)
        """
        my_dict = {}
        my_dict['name'] = 'Alice'

        self.assertTrue('name' in my_dict)
        self.assertEqual(my_dict['name'], 'Alice')

    def test_lookup(self) -> None:
        """
        test lookup to dictionary
        """
        my_dict = {
            'name': 'Bob',
            'age': 30
        }

        self.assertEqual(my_dict['name'], 'Bob')
        self.assertEqual(my_dict['age'], 30)

        with self.assertRaises(KeyError):
            _ = my_dict['city']

    def test_deletion(self) -> None:
        """
        test the deletion of an existing element.
        """
        my_dict = {
            'name': 'Charlie',
            'age': 25
        }
        del my_dict['name']

        self.assertFalse('name' in my_dict)

        with self.assertRaises(KeyError):
            del my_dict['city']

    def test_iteration(self) -> None:
        """
        test iteration method.
        """
        my_dict = {'name': 'David', 'age': 35}
        keys = []
        values = []

        for key, value in my_dict.items():
            keys.append(key)
            values.append(value)

        self.assertEqual(keys, ['name', 'age'])
        self.assertEqual(values, ['David', 35])

    def test_default_value(self) -> None:
        """
        test the default value.
        """
        my_dict = {
            'name': 'Eve',
            'age': 40
        }
        city = my_dict.get('city', 'Unknown')
        self.assertEqual(city, 'Unknown')

        name = my_dict.get('name', 'Anonymous')
        self.assertEqual(name, 'Eve')


if __name__ == '__main__':
    unittest.main()
