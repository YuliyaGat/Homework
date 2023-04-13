class CustomException(Exception):
   def __init__(self, msg):
       self.msg = msg

   def __str__(self):
       my_file = open("logs.txt", "a+")
       my_file.write(self.msg + '\n')
       my_file.close()

raise CustomException('Ups')




