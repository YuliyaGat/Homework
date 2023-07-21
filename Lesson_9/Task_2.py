import sys

print(sys.path) #all paths for finding Python modules

sys.path.append('D:/Моя папка') #adding a specific path for the interpreter to search
print(sys.path)

print(sys.path[0]) #first path for the interpreter to search
print(sys.path[-1]) #last path for the interpreter to search

sys.path.insert(0, 'D:/FTP/log/') #add first path for the interpreter to search
print(sys.path)

sys.path.remove('D:/FTP/log/') #delete D:/FTP/log/ as a paths for finding Python modules
print(sys.path)

sys.path.pop(-1) #delete last paths for finding Python modules
print(sys.path)

sys.path.extend(['D:/FTP/log/','D:/Моя папка']) ##adding paths for the interpreter to search
print(sys.path)
