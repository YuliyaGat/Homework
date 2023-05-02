import unittest
import Task_1

class My_contTestCase(unittest.TestCase):
    def setUp(self):
        self.file = 'text.txt'
        self.method = 'r'

    def test_enter(self):
        with Task_1.My_cont(self.file, self.method) as f:
            alist = f.read()
            self.assertIsInstance(alist, str)
            self.assertEqual(alist,'Hello!\nIt is a wonderful day!')

    def test_exception(self):
        with self.assertRaises(ZeroDivisionError):
            with Task_1.My_cont(self.file, self.method) as f:
                1/0

    def test_exception_type(self):
        with self.assertRaises(TypeError):
            with Task_1.My_cont(self.file, 2) as f:
                pass

    def test_counter(self):
        with Task_1.My_cont(self.file, self.method) as f:
                pass
        with Task_1.My_cont(self.file, self.method) as f:
            self.assertEqual(Task_1.My_cont.counter,2)

    def test_file_closing(self):
        with Task_1.My_cont(self.file, self.method) as f:
            f.read(self.file)
        self.assertTrue(f.closed)

   #unittest.main()
