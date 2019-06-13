"""Module to verify the pdb file format"""
import sys
from pathlib import Path 

def linecount(line):
    space  = 0
    character = 0
    column = 0
    for i in line:
        if i == ' ':
            column += 1
        elif i == '\n':
            space += 1
        else:
            character += 1
    return (column + space + character)


def valid_file(file): 
    """Function to verify the pdb format by calling linecount function"""
    filename = file
    #print(filename)
    with open(filename) as fileIn:
        line = fileIn.readline()
        tag = False
        lineCount= 0
        while line:
            lineCount = linecount(line)
            letter_list = line.split()
            first_letter = letter_list[0]
            if lineCount == 81 and line.endswith('\n') and first_letter in record_type.values():
                tag = True
                
                
            else:
                tag = False
              
            line = fileIn.readline()      
                
        if tag == True:
            #menu_display1(filename)
            return filename
        if tag == False:
            print('File \033[1;31merror\033[1;m not a PDB file')
            return None
            
            
record_type= {1:'HEADER',2:'OBSLTE',3:'TITLE',4:'SPLIT',5:'CAVEAT',6:'COMPND',7:'SOURCE',8:'KEYWDS',9:'EXPDTA',10:'NUMMDL',
              11:'MDLTYP',12:'AUTHOR',13:'REVDAT',14:'SPRSDE',15:'JRNL',16:'REMARK',17:'DBREF',18:'DBREF1',19:'DBREF2',
        
              20:'SEQADV',21:'SEQRES',22:'MODRES',23:'HETNAM',24:'HETSYN',25:'FORMUL',26:'HELIX',27:'SHEET',28:'SSBOND',
              29:'LINK',30:'CISPEP',31:'SITE',32:'CRYST1',33:'ORIGX1',34:'ORIGX2',35:'ORIGX3',36:'SCALE1',37:'SCALE2',
              38:'SCALE3',39:'MTRIX1',40:'MTRIX2',41:'MTRIX3',42:'MODEL',43:'ATOM',44:'ANISOU',45:'TER',46:'HETATM',
              47:'ENDMDL',48:'CONECT',49:'MASTER',50:'END',51:'HET'}
           
   
           
def menu_display1(filename):
    """Displays the menu once the file is loaded, printing the loaded file"""
    file = filename
    x1 = '*' 
    x2 = '*' + " "
    print(x1 * 80)
    print('\033[1;47m* PDB FILE ANALYZER  \033[1;m{0:58s}*'.format(""))
    print(x1 * 80)
    print('*\033[1;30m Select an option from below:\033[1;m{0:49s}*'.format(""))
    print('\033[1;30m*  \033[1;m{0:76s}*'.format(""))
    print('\033[1;30m*     1) \033[1;m Open a PDB File{0:26s}(O){0:25s}*'.format(""))
    print('\033[1;30m*     2) \033[1;m Information{0:29s} (I){0:25s}*'.format(""))
    print('\033[1;30m*     3) \033[1;m Show histogram of amino acids{0:11s} (H){0:25s}*'.format(""))
    print('\033[1;30m*     4) \033[1;m Display Secondary Structure{0:13s} (S){0:25s}*'.format(""))
    print('\033[1;30m*     5) \033[1;m Export PDB File{0:25s} (X){0:25s}*'.format(""))
    print('\033[1;30m*     6) \033[1;m Exit{0:36s} (Q){0:25s}*'.format(""))
    print('\033[1;30m*  \033[1;m{0:76s}*'.format(""))
    print('* {0:54s}Current PDB:\033[1;31m %s \033[1;m *'.format("")%file)
    print(x1 * 80)
    print(':\033[1;31m O\033[1;m')
   
