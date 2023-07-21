import sys
def count_lines(text1): #reads an input file and counts the number of lines in it
  text1.seek(0)
  lines_list=text1.readlines()
  return(len(lines_list))

def count_chars(text2): #reads an input file and counts the number of characters in it
  text2.seek(0)
  lines_list = text2.read()
  return(len(lines_list))

def test(name): #calls both counting functions
  text = open(name)
  print(count_lines(text))
  print(count_chars(text))
#test('biography_Kilian_Jornet.txt')
#test('mymod.py')


