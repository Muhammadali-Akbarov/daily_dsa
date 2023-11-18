"""
strings in python are sequences of characters,
and they play a crucial role in text processing and data manipulation,
let's dive into more advanced information about strings,
including how they work internally and their associated big o complexities.

internal representation of strings:
    unicode:
        python strings are represented using unicode,
        which is a character encoding standard that
        covers a vast range of characters from various writing systems and symbols,
        this allows python strings to handle text in different languages and characters
        from different scripts.

    immutable:
        strings in python are immutable,
        meaning their contents cannot be modified after creation,
        when you perform operations that seem to modify a string,
        you are actually creating a new string with the desired changes.

    character encoding:
        each character in a string is typically represented as a fixed-size
        unit (e.g., 1 to 4 bytes per character, depending on the encoding),
        common encodings include utf-8 and utf-16. utf-8 is variable-length,
        meaning it uses a different number of bytes for different characters,
        making it memory-efficient for ascii characters.

    how works with bif O principles:
        concatenation:
            combining two strings using the + operator or str.join() is generally an
            o(n) operation, where n is the total length of the resulting string, this
            is because a new string will be created with all characters.

        indexing:
            accessing a character by its index (eg., my_string[3]) is an O(1) because
            python internally maintains an array-like structure for strings, allows for
            direct access to characters.

        slicing:
            creating a substring from a string using slicing (eg., my_string[2:5]) is an O(K)
            operation, where K is the length of the resulting substring, this is because a new
            string is created with a copy of the selection characters.

        string methods:
            many string methods, such as str.split(), str.strip() and str.replace(),
            typically run in O(n) time, where n is the length of the string, some methods
            may have slightly different complexities bases on specific operation.

        searching and replacing:
            searching for a substring (e.g., str.find(), str.index()) or replacing
            substring (e.g, str.replace()) is generally an O(n) operation because it may
            require iterating through the entire string.

        string formatting:
            string formatting operations (e.g, f-strings str.format()) are efficient and
            typically have an O(n) complexity, where n is the length of the resulting string.

        string comparison:
            comparing two strings for equality (e.g, str1 == str2) is typically an O(n)
            operation, where n is the length of the longer string, however, python optimizes
            this for some cases and can return early if the strings are not equal.

        in summary, python strings are internally represented as unicode sequences
        and are designed to handle text from various languages and scripts,
        understanding the big o complexities of string operations is essential
        for optimizing code that involves string manipulation,
        especially when working with large strings or performing operations within loops.
"""
import unittest


class TestStringMethods(unittest.TestCase):
    """
    test string methods.
    """
    def test_concatenation(self) -> None:
        """
        test concatenation method.
        """
        str1 = "hello, "
        str2 = "world!"
        result = str1 + str2
        self.assertEqual(result, "hello, world!")

    def test_indexing(self) -> None:
        """
        test indexing method.
        """
        my_string = "python"
        self.assertEqual(my_string[0], 'p')
        self.assertEqual(my_string[3], 'h')
        self.assertEqual(my_string[-1], 'n')

    def test_slicing(self) -> None:
        """
        test slicing method.
        """
        my_string = "python"
        substr = my_string[1:4]
        self.assertEqual(substr, "yth")
        substr2 = my_string[:3]
        self.assertEqual(substr2, "pyt")
        substr3 = my_string[3:]
        self.assertEqual(substr3, "hon")

    def test_string_methods(self) -> None:
        """
        test string methods.
        """
        my_string = "  python  "
        self.assertEqual(my_string.strip(), "python")
        self.assertEqual(my_string.split(), ["python"])
        self.assertEqual(my_string.replace('p', 'c'), "  cython  ")

    def test_searching_and_replacing(self) -> None:
        """
        test searching and replacement.
        """
        my_string = "Python is fun and Python is powerful"
        self.assertEqual(my_string.find('is'), 7)
        self.assertEqual(my_string.replace('Python', 'Java'), "Java is fun and Java is powerful")

    def test_string_formatting(self) -> None:
        """
        test sting formatting.
        """
        name = "Alice"
        age = 30
        formatted_str = f"My name is {name} and I am {age} years old."
        self.assertEqual(formatted_str, "My name is Alice and I am 30 years old.")

    def test_string_comparison(self) -> None:
        """
        test string comparison.
        """
        str1 = "Python"
        str2 = "python"
        self.assertTrue(str1 == str1)
        self.assertFalse(str1 == str2)

    def test_string_interpolation(self) -> None:
        """
        test string interpolation.
        """
        name = "Bob"
        age = 25
        # pylint: disable=C0209
        interpolated_str = "My name is {} and I am {} years old.".format(name, age)
        self.assertEqual(interpolated_str, "My name is Bob and I am 25 years old.")


if __name__ == '__main__':
    unittest.main()
