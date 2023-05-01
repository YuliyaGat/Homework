import unittest
import phonebook
from unittest.mock import patch
from io import StringIO

class PhonebookTestCase(unittest.TestCase):

    def test_change_json(self):
        phonebook.change_json('phonebook.json',[{'first name': 'Victor', 'last name': 'Brown', 'telephone number': '+380503254050', 'city': 'Lviv', 'state': 'Ukraine'}])
        book_list = phonebook.open_json('phonebook.json')
        self.assertEqual(book_list, [{'first name': 'Victor', 'last name': 'Brown', 'telephone number': '+380503254050', 'city': 'Lviv', 'state': 'Ukraine'}])

    def test_new_entries(self):
        test_data = "Kate\nDuke\n0505435354\nOslo\nNorway\n"
        with patch('sys.stdin', StringIO(test_data)):
            book_list = phonebook.open_json('phonebook.json')
            phonebook.new_entries(book_list)
            book_list = phonebook.open_json('phonebook.json')
        self.assertIn({"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'}, book_list)

    def test_first_name(self):
        phonebook.change_json('phonebook.json',[{'first name': 'Victor', 'last name': 'Brown', 'telephone number': '+380503254050', 'city': 'Lviv', 'state': 'Ukraine'}, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'}])
        book_list = phonebook.open_json('phonebook.json')
        test_data = "Kate\n"
        with patch('sys.stdin', StringIO(test_data)):
           dict_fn = phonebook.first_name(book_list)
        self.assertEqual(dict_fn, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'})

    def test_last_name(self):
        phonebook.change_json('phonebook.json', [{'first name': 'Victor', 'last name': 'Brown', 'telephone number': '+380503254050', 'city': 'Lviv', 'state': 'Ukraine'}, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'}])
        book_list = phonebook.open_json('phonebook.json')
        test_data = "Duke\n"
        with patch('sys.stdin', StringIO(test_data)):
            dict_ln = phonebook.last_name(book_list)
        self.assertEqual(dict_ln, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'})

    def test_full_name(self):
        phonebook.change_json('phonebook.json', [{'first name': 'Victor', 'last name': 'Brown', 'telephone number': '+380503254050', 'city': 'Lviv', 'state': 'Ukraine'}, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'}])
        book_list = phonebook.open_json('phonebook.json')
        test_data = "Kate\nDuke\n"
        with patch('sys.stdin', StringIO(test_data)):
            dict_fn = phonebook.full_name(book_list)
        self.assertEqual(dict_fn, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'})

    def test_search_by_number(self):
        phonebook.change_json('phonebook.json', [{'first name': 'Victor', 'last name': 'Brown', 'telephone number': '+380503254050', 'city': 'Lviv', 'state': 'Ukraine'}, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'}])
        book_list = phonebook.open_json('phonebook.json')
        test_data = "0505435354\n"
        with patch('sys.stdin', StringIO(test_data)):
            dict_num = phonebook.search_by_number(book_list)
        self.assertEqual(dict_num, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'})

    def test_search_by_place(self):
        phonebook.change_json('phonebook.json', [{'first name': 'Victor', 'last name': 'Brown', 'telephone number': '+380503254050', 'city': 'Lviv', 'state': 'Ukraine'}, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'}])
        book_list = phonebook.open_json('phonebook.json')
        test_data = "Oslo\n"
        with patch('sys.stdin', StringIO(test_data)):
            dict_pl = phonebook.search_by_place(book_list)
        self.assertEqual(dict_pl, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'})

    def test_delete_record(self):
        phonebook.change_json('phonebook.json', [{'first name': 'Victor', 'last name': 'Brown', 'telephone number': '+380503254050', 'city': 'Lviv', 'state': 'Ukraine'}, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'}])
        book_list = phonebook.open_json('phonebook.json')
        test_data = "0505435354\n"
        with patch('sys.stdin', StringIO(test_data)):
            book_list = phonebook.delete_record(book_list)
        self.assertNotIn({"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'}, book_list)

    def test_update_record(self):
        phonebook.change_json('phonebook.json', [{'first name': 'Victor', 'last name': 'Brown', 'telephone number': '+380503254050', 'city': 'Lviv', 'state': 'Ukraine'}, {"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'}])
        book_list = phonebook.open_json('phonebook.json')
        test_data = "0505435354\nKatee\nDukenen\n0505435354\nBergen\nNorway"
        with patch('sys.stdin', StringIO(test_data)):
            book_list = phonebook.update_record(book_list)
        self.assertNotIn({"first name": 'Kate', "last name": 'Duke', "telephone number": '0505435354', "city": 'Oslo', "state": 'Norway'}, book_list)
        self.assertIn({"first name": 'Katee', "last name": 'Dukenen', "telephone number": '0505435354', "city": 'Bergen', "state": 'Norway'}, book_list)

    #unittest.main()