import unittest
import Task_2_Lesson15

class DogTestCase(unittest.TestCase):
   def setUp(self):
       self.my_dog = Task_2_Lesson15.Dog(5)
   def test_humane_age(self):
       self.assertEqual(self.my_dog.human_age, 35)


   #unittest.main()
