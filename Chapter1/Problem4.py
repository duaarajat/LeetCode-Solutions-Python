# Write a program to print the contents of a directory using the os module. Search online for the function which does that

# import os

# def print_dir_contents(path='.'):
#     """
#     Prints all entries (files, folders, symlinks, etc.) in the specified directory.
#     Default path is the current directory.
#     """
#     try:
#         entries = os.listdir(path)  # 🔍 lists names in 'path'
#     except FileNotFoundError:
#         print(f"Error: Directory '{path}' not found.")
#         return
#     except NotADirectoryError:
#         print(f"Error: '{path}' is not a directory.")
#         return
#     except PermissionError:
#         print(f"Error: Permission denied for directory '{path}'.")
#         return

#     print(f"Contents of '{path}':")
#     for name in entries:
#         print(' -', name)

# if __name__ == "__main__":
#     # Example: list current directory
#     print_dir_contents()

#     # Example: list a specific directory
#     # print_dir_contents('/path/to/directory')

import os
#Select the directory whose content you want to list
directory = '/'
#use the os module to list the content directory
contents = os.listdir(directory)
# printing the list
print(contents)