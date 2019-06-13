"""Module to print the Title plus amino acid sequence per chain  for a given pdb file"""
from pathlib import Path

def TitleInfo(currentFile):
    """Function to print title of the pdb file"""
    Title=[]
    with open(currentFile) as fileIn:
        print(':\033[1;31mI\033[1;m')
        print('PDB File:\033[1;31m %s\033[1;m'%currentFile)
        line = fileIn.readline()
        while line:
            if line.startswith('TITLE'):
                Title.append(line)

            line = fileIn.readline()
        if len(Title) == 1:
            Str = "".join(Title)
            x = Str.replace('TITLE', '')
            Str1 = x.lstrip()
            print('Title: %s'%Str1)
        if len(Title) > 1:
            #Str = "".join(l)
            t =(Title[0])
            z = (Title[1])
            t1 = t.replace('TITLE', '')
            z1 = z.replace('TITLE', '')
            z2 = z1.replace('2', '')
            t2 = t1.strip()
            z3 = z2.strip()
            print('Title:%s'%t2+z3)
            #return Title

        

def ReturnChain(currentFile):
    """ Function to extract type of chains from pdb file"""
    with open(currentFile) as fileIn:
            lines = fileIn.readlines()
            Chainlist=[]
            for line in lines:
                if line.startswith('SEQRES'):
                    List = line.split()
                    Chainlist.append(List[2])
            #print(Chainlist)
            Chain = set(Chainlist)
            chain = sorted(list(Chain))
            return chain

    
def seqprint(seqList):
    """Function to print  50 characters per line"""
    List = seqList
    x=' '
    seq = [aaCode[b] for b in List]
    seq2 =" ".join(seq)
    seq3 = seq2.replace(" ","")
    read_length = len(seq3)
    #print(len(seq3))
    if read_length < 50:
        print(x*8+seq3)
    else:
        char_per_line = 50
        for base in range(0,len(seq3),char_per_line):
            print(x*8+seq3[base:base+char_per_line])
            
def InfoPrint(currentFile): 
    """prints No. of amino acid,helix and sheet info. by call seqprint function"""
    Chains = ReturnChain(currentFile)
    chainlist =  ReturnChain(currentFile)
    if len(chainlist) > 1:
        chainlist.insert(len(chainlist)-1,'and')
        print('CHAINS:',' '.join(chainlist))
    else:
        print('CHAIN: %s'%''.join(chainlist))
    x= ' '
    for chain in Chains:
        with open(currentFile) as fileIn:
            sequence=[]
            helix_count = 0
            sheet_count = 0
            line = fileIn.readline()
            while line:
                if line.startswith('SEQRES'):
                    words = line.split()
                    chaintype = words[2]
                    if chaintype == chain:
                        for word in words:
                            if word in aminoacidsCode.values():
                                sequence.append(word)

                    else:
                        pass


                if line.startswith('HELIX'):
                        helixInfo = line.split()
                        chaintype = helixInfo[4]
                        if chaintype == chain:
                            helix_count = helix_count + 1

                        else:
                            pass

                if line.startswith('SHEET'):
                        sheetInfo = line.split()
                        chaintype = sheetInfo[5]
                        if chaintype == chain:
                            sheet_count = sheet_count + 1

                        else:
                            pass

                line = fileIn.readline()

            print('- Chain %s'%chain)
            print('Number of amino acids: %s'%len(sequence))
            print('Number of helix:%s %s'%(x*7,helix_count))
            print('Number of sheet:%s %s'%(x*7,sheet_count))
            print('Sequence:'),seqprint(sequence)

                                            
                                            
aminoacidsCode= {1:'ALA', 2: 'CYS',3: 'ASP',4:'GLU',5:'PHE',6:'GLY',7:'HIS',8:'ILE',9:'LYS',10:'LEU',11: 'MET',
             12:'ASN',13:'PRO',14: 'GLN',15:'ARG',16:'SER',17:'THR',18:'VAL',19:'TRP',20:'TYR'}

aaCode= {'ALA':'A','CYS':'C','ASP':'D','GLU':'E','PHE':'F','GLY':'G','HIS':'H','ILE':'I','LYS':'K','LEU':'L','MET':'M',
             'ASN':'N','PRO':'P','GLN':'Q','ARG':'R','SER':'S','THR':'T','VAL':'V','TRP':'W','TYR':'Y'}
