from pathlib import Path
def ReturnChain(currentFile):
    """Function to extract chain types from pdb  file"""
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

def seqprint2(seqList): # prints 50 a/a per line
    List = seqList
    seq = [aaCode[b] for b in List]
    return "".join(seq)
       

            
aaCode= {'ALA':'A','CYS':'C','ASP':'D','GLU':'E','PHE':'F','GLY':'G','HIS':'H','ILE':'I','LYS':'K','LEU':'L','MET':'M',
             'ASN':'N','PRO':'P','GLN':'Q','ARG':'R','SER':'S','THR':'T','VAL':'V','TRP':'W','TYR':'Y'}               
            
def patternPrint(sequence,helixInfo,sheetInfo):
    """function to print secondary structure plus the symbols"""
    Seq1 = str(sequence)
    helixInfo = helixInfo
    sheetInfo = sheetInfo
    #print(len(Seq1))
    helixId = '/'
    sheetId = '|'
    helixCodes= []
    sheetCodes = []
    helixCodes_Start= []
    sheetCodes_Start = []
    Codelist= []
    Sec_info= []
    helixIndexes = []
    sheetIndexes = []
    for i in Seq1:
        Codelist.append(' ')
        Sec_info.append('-')
    #print(len(Codelist))
    #print(len(Sec_info))
    for i in helixInfo:
         if len(helixInfo) >= 1:
                for index in range(int(i[1][0]),int(i[1][1]+ 1)):
                    helixIndexes.append(index)
        #else:
            #pass
        
    for i in helixInfo:
        if len(helixInfo) >= 1:
            helixCodes.append(i[0])
            helixCodes_Start.append(i[1][0])
            
        #else:
            #pass

    for i in sheetInfo:
        if len(sheetInfo) >= 1:
            for index in range(int(i[1][0]),int(i[1][1]+ 1)):
                sheetIndexes.append(index)

        #else:
            #pass
    
    for i in sheetInfo:
        if len(sheetInfo) >= 1:
            sheetCodes.append(i[0])
            sheetCodes_Start.append(i[1][0])

        #else:
            #pass

    for i in range(len(helixIndexes)):
        helixId += '/'
    #print(helixId)
    for i in range(len(sheetIndexes)):
        sheetId += '|'
    #print(sheetId)
    for (index,r) in zip(helixIndexes,helixId):
        Sec_info[index-1] = r
    for (index,r) in zip(sheetIndexes,sheetId):
        Sec_info[index-1] = r
    #print(Sec_info)
    l = "".join(Sec_info)
    #print(l)
    #characterPrint(l)
    for (index,r) in zip(helixCodes_Start,helixCodes):
        if len(r) > 1:
            Codelist[index-1:index+len(r)-1]= r
            
        else:
            Codelist[index-1]= r
        
    for (index,r) in zip(sheetCodes_Start,sheetCodes):
        if len(r) > 1:
            Codelist[index-1:index+len(r)-1]= r
        else:
            Codelist[index-1]= r
    #print(Codelist)
    codeString= "".join(Codelist)
    #seqprin(Seq1)
    #print(helixCodes)
    #print(sheetCodes)
    char_per_line = 80
    for char in range(0,len(Seq1),char_per_line):
        print (Seq1[char:char+char_per_line]+ "\n" + l[char:char+char_per_line]+'\n'+codeString[char:char+char_per_line])
        print("\n")
    print('  (%s)'%len(Seq1))
    print("\n")
    

def SecStructure(currentFile):
    """Main function, calls the patterPrint function to display secondary structure plus the symbol representation"""
    Chains = ReturnChain(currentFile)
    print(':\033[1;31mS\033[1;m')
    for chain in Chains:
        with open(currentFile) as fileIn:
                sequence=[]
                helix_status=[]
                sheet_status =[]
                line = fileIn.readline()
                while line:
                    if line.startswith('SEQRES'):
                        words = line.split()
                        chaintype = words[2]
                        if  chaintype == chain:
                            for word in words:
                                if word in aminoacidsCode.values():
                                    sequence.append(word)

                        else:
                            pass


                    if line.startswith('HELIX'):
                            helixInfo = line.split()
                            chaintype = helixInfo[4]
                            helixtype= helixInfo[2]
                            helix_pos = (int(helixInfo[5]) ,int(helixInfo[8]))
                            helixID = (helixtype,helix_pos) 
                            
                            if chaintype == chain:
                                  helix_status.append(helixID)
                            else:
                                pass

                    if line.startswith('SHEET'):
                            sheetInfo = line.split()
                            chaintype = sheetInfo[5]
                            sheettype= sheetInfo[1] + sheetInfo[2]
                            sheet_pos = (int(sheetInfo[6]) ,int(sheetInfo[9]))
                            sheetID = (sheettype,sheet_pos)

                            if chaintype == chain:
                                 sheet_status.append(sheetID)
                            else:
                                pass

                    line = fileIn.readline()
                    
                print('Chain %s:'%chain)
                print('(1)')
                Seq= seqprint2(sequence)
                patternPrint(Seq,helix_status,sheet_status)

                
                
aminoacidsCode= {1:'ALA', 2: 'CYS',3: 'ASP',4:'GLU',5:'PHE',6:'GLY',7:'HIS',8:'ILE',9:'LYS',10:'LEU',11: 'MET',
             12:'ASN',13:'PRO',14: 'GLN',15:'ARG',16:'SER',17:'THR',18:'VAL',19:'TRP',20:'TYR'}

