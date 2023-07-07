from Digitalphonebook import newcontact, searchexistingcontact, DisplayPhoneBoook

import unittest

class PhonebookTestCase(unittest.TestCase):

    def test_new_contact(self):
        test_dict = {}
        result = newcontact("John Doe", "1234567890", test_dict)
        self.assertTrue(result)

    def test_search_existing_contact_found(self):
        test_dict = {}
        newcontact("Saranya", "1234567890", test_dict)
        result = searchexistingcontact("Saranya", test_dict) 
        self.assertTrue(result)

    def test_search_existing_contact_not_found(self):
        test_dict = {}
        newcontact("Saranya", "1234567890", test_dict)
        result = searchexistingcontact("Lavanya", test_dict) 
        self.assertFalse(result)

    def test_display_phonebook_empty(self):
        test_dict = {}
        result= DisplayPhoneBoook(test_dict)
        self.assertFalse(result)

    def test_display_phonebook_non_empty(self):
        test_dict = {"Saranya" : 1234556}
        result= DisplayPhoneBoook(test_dict)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()

