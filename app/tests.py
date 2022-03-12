from django.test import TestCase

from .customs import generate_unique_key


class CustomsTestCase(TestCase):
    def setUp(self):
        self.test_url_list = [
            "https://www.google.com/search?query=what+is+programming",
            "https://www.google.com/search?query=what+is+high+level+language"
        ]
        self.test_user_list = [
            "Emeka", "Adanna"
        ]
    
    def test_generate_unique_key_function(self):
        key1 = generate_unique_key(
            self.test_url_list[0], self.test_user_list[0])
        key2 = generate_unique_key(
            self.test_url_list[1], self.test_user_list[1])
        
        self.assertTrue(len(key1) == len(key2))
        self.assertTrue(len(key1) == 8)
        self.assertTrue(type(key1) == str)
