"""Function to display a histogram of  amino acid sequence for a pdb file"""
from pathlib import Path
def AminoAcid_histogram(currentFile): 
    with open(currentFile) as fileIn:
            line = fileIn.readline()
            sequence_raw=[]
            star = '*'
            while line:
                if line.startswith('SEQRES'):
                    words = line.split()
                    for word in words:
                        if word in aminoacidsCode.values():
                                sequence_raw.append(word)
                line = fileIn.readline()
          
            base_count = dict((base, sequence_raw.count(base)) for base in set(sequence_raw))
            print(': \033[1;31mH\033[1;m')
            print('Choose an option to order by:')
            print('{0:2s}number of amino acids - ascending {0:6s}(an)'.format(""))
            print('{0:2s}number of amino acids - descending {0:5s}(dn)'.format(""))
            print('{0:2s}alphabetically - ascending {0:13s}(aa)'.format(""))
            print('{0:2s}alphabetically - descending {0:12s}(da)'.format(""))
            choice = input('Enter "an" for ascending order by No.,"dn" for descending order by No.,"aa" for ascending order by al.,"da" for descending order by al. or "m" to quit:')
            #print('Order by :%s'%choice.lower())
            while choice !='m':
                if choice.lower() in ('an','dn','aa','da'):
                    if choice.lower() == 'an':
                        print('Order by :\033[1;31m%s\033[1;m'%choice.lower())
                        for key, value in sorted(base_count.items(), key=lambda item: item[1]):
                            print("%s ( %2s)" % (key, value),": %s" %(star*int(value)))

                    elif choice.lower() == 'dn':
                        print('Order by :\033[1;31m%s\033[1;m'%choice.lower())
                        for key, value in sorted(base_count.items(), key=lambda item: item[1], reverse = True):
                            print("%s ( %2s)"  %(key, value),": %s" %(star*int(value)))

                    elif choice.lower() == 'aa':
                        print('Order by :\033[1;31m%s\033[1;m'%choice.lower())
                        for key in sorted(base_count):
                            print('%s ( %2s)' %(key,base_count[key]),": %s"%(star*int(base_count[key])))

                    elif choice.lower() == 'da':
                        print('Order by :\033[1;31m%s\033[1;m'%choice.lower())
                        for key in sorted(base_count,reverse = True):
                            print('%s ( %2s)'%(key,base_count[key]),": %s"%(star*int(base_count[key])))

                else:
                    print('Wrong choice')
                choice = input('Enter "an" for ascending order by No.,"dn" for descending order by No.,"aa" for ascending order by al.,"da" for descending order by al. or "m" to quit:')
                

                        
                              
aminoacidsCode = {1:'ALA', 2: 'CYS',3: 'ASP',4:'GLU',5:'PHE',6:'GLY',7:'HIS',8:'ILE',9:'LYS',10:'LEU',11: 'MET',
             12:'ASN',13:'PRO',14: 'GLN',15:'ARG',16:'SER',17:'THR',18:'VAL',19:'TRP',20:'TYR'}