# -----------------------------------------USING A CLASS--------------------------------------------------

# class Open_File():
#
#     def __init__(self, filename, mode):
#         self.filename =  filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()
#
#
# with Open_File('sample.txt', 'w') as f:
#     f.write('Writing to file using Context Manager')
#
#
# print(f.closed)

# ---------------------------------------------------USING A FUNCTION-------------------------------------------#


from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()

with open_file('sample.txt', 'w') as f:
    f.write('Writing to file using Context Manager another time')

print(f.closed)