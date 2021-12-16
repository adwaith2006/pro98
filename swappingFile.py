import shutil
import os

path='C:/pro98/file1.txt'
path2='C:/pro98/file2.txt'

print(Before:)
print(os.listdir(path))
print(os.listdir(path2))

source='/C:/pro98/file1.txt'
destination='/C:/pro98/file2.txt'

dest=shutil.move(source,destination)
dest() 

source='/C:/pro98/file1.txt'
destination='/C:/pro98/file2.txt'

sour=shutil.move(source,destination)
sour()

print(After:)
print(os.listdir(path)) 
print(os.listdir(path2))


