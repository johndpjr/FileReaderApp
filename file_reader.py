import os


def read_file(filename: str) -> list:
    """Returns a list of lines from the text file"""

    # Only attempt file open if it exists
    if os.path.exists(f'files/{filename}'):
        with open(f'files/{filename}') as f:
            return str(f.readlines())

print(read_file('file4.txt'))