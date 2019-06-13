"""Function to export a pdb file,given the path and file name"""
from pathlib import Path
def fileExport(currentfile):
    file = currentfile
    with open(file) as my_PDB_file:
        print(':\033[1;31mX\033[1;m')
        data =  my_PDB_file.read()
        filename = Path(input('enter file path:'))
        if filename.exists():
            print("The file exist,enter newfile name 'renterpath'")
            filename = Path(input('enter path:'))
            with open(filename, 'w') as newfile:
                newfile.write(data)
        else:
            with open(filename, 'w') as newfile:
                newfile.write(data)