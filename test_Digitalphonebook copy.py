import unittest
from Digitalphonebook import

class PhonebookTestCase(unittest.TestCase):

    def setUp(self):
        self.phonebook = {}
        
    def test_new_contact(self):
        newcontact("John Doe", "1234567890", self.phonebook)
        self.assertEqual(len(self.phonebook), 1)
        self.assertEqual(self.phonebook["John Doe"], "1234567890")
        
    def test_search_existing_contact(self):
        self.phonebook["Jane Smith"] = "9876543210"
        result = searchexistingcontact("Jane Smith", self.phonebook)
        self.assertEqual(result, None)  # The function prints the number, so we check for None
        
    def test_display_phonebook_empty(self):
        result = DisplayPhoneBoook(self.phonebook)
        self.assertFalse(result)
        
    def test_display_phonebook_non_empty(self):
        self.phonebook["John Doe"] = "1234567890"
        self.phonebook["Jane Smith"] = "9876543210"
        result = DisplayPhoneBoook(self.phonebook)
        self.assertTrue(result)
        
if __name__ == "__main__":
    unittest.main()
