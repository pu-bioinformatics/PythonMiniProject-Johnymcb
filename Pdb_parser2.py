"""The program imports functions from different desinged modules to excute its function"""
import sys
from pathlib import Path
import PDB_verify2 as funct1
import SecondaryInfo as funct2
import AminoAcidHist2 as funct3
import SecStructure as funct4
import PdbFileExport2 as funct5

def menu_display():
    """Displays main menu of the programme"""
    x1 = '*' 
    x2 = '*' + " "
    space = ' '
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
    print('*{0:59s}Current PDB:\033[1;31m None \033[1;m *'.format(""))
    print(x1 * 80)
    print(':')
    global choice
    choice = input('Enter "O" for option 1,"I" for option 2,"H" for option 3,"S" for option 4 ,"X" for option 5 or "Q" to Exit:')

def Choice2():
    """Iterates over the menu options"""
    global currentFile
    selection = input('Enter "O" for option 1,"I" for option 2,"H" for option 3,"S" for option 4 ,"X" for option 5 or "Q" to Exit:')
    if selection.upper() in ('O','I','H','S','X','Q'):
        #print(selection)
        if selection.upper() == 'I':
            funct2.TitleInfo(currentFile)
            funct2.InfoPrint(currentFile)
            funct1.menu_display1(currentFile)
            selection = input('Enter "O" for option 1,"I" for option 2,"H" for option 3,"S" for option 4 ,"X" for option 5 or "Q" to Exit:')
           

        if selection.upper() == 'H':
            funct3.AminoAcid_histogram(currentFile)
            funct1.menu_display1(currentFile)
            selection = input('Enter "O" for option 1,"I" for option 2,"H" for option 3,"S" for option 4 ,"X" for option 5 or "Q" to Exit:')
            
        if  selection.upper() == 'S':
            funct4.SecStructure(currentFile)
            funct1.menu_display1(currentFile)
            selection = input('Enter "O" for option 1,"I" for option 2,"H" for option 3,"S" for option 4 ,"X" for option 5 or "Q" to Exit:')
          
        if selection.upper() == 'X':
            funct5.fileExport(currentFile)
            funct1.menu_display1(currentFile)
            selection = input('Enter "O" for option 1,"I" for option 2,"H" for option 3,"S" for option 4 ,"X" for option 5 or "Q" to Exit:')
           
        if selection.upper() == 'Q':
            print(':\033[1;31m%s\033[1;m'%selection.upper())
            choice =input('Do you want to exit "(E)" or do you want go back to the menu "(M)":')
            if choice.upper() in ('(%s)''(%s)'%('M','E')):
                if choice.upper() == 'M':
                    print(':\033[1;31m%s\033[1;m'%choice.upper())
                    main()
                    
                
                elif choice.upper() =='E':
                    print(':\033[1;31m%s\033[1;m'%choice.upper())
                    print('System shutting down')
                    currentFile = None
                    sys.exit
                    
                else:
                    print('Invalid choice')
                    main()

        else:
            if selection.upper() == 'O':
                print('Do you want to replace the current file %s ?'%currentFile)
                selection = input("Please enter 'yes' to replace the file or 'no' to proceed: ")
                if selection in ('yes','no'):
                    if selection.lower() == 'yes':
                        print(selection.lower())
                        main()
                    else:
                        selection.lower() == 'no'
                        print(selection.lower())
                        pass
                
                selection = input('Enter "O" for option 1,"I" for option 2,"H" for option 3,"S" for option 4 ,"X" for option 5 or "Q" to Exit:')
                
    else:
        print('Invalid choice')
        funct1.menu_display1(currentFile)
        Choice2()
        
        
def main():
    """Calls the all function'imported,choice2 and menu_display to run the programm'"""
    global currentFile
    currentFile = None
    global choice
    menu_display()
    if choice.upper() in ('O','I','H','S','X','Q'):
        if currentFile == None and choice.upper() == 'O': 
            filename = Path(input('enter path:'))
            if  filename.exists():
                print('The file %s successfuly loaded'%filename.name)
                currentFile = filename.name
                currentFile =funct1.valid_file(currentFile)
                if currentFile == None:
                    main()
                else:
                    funct1.menu_display1(currentFile)
                    while currentFile != None:
                        Choice2()
                 
            else:
                print('Enter a Valid Path for a PDB file:\033[1;31m%s\033[1;m'%filename.name)
                main()
                
        
        elif currentFile == None and choice.upper() in ('I','H','S','X'): 
            print('Please load the file to proceed')
            main()
            
        else:
            if currentFile == None and choice.upper() == 'Q':
                print(':\033[1;31m%s\033[1;m'%choice.upper())
                choice =input('Do you want to exit "(E)" or do you want go back to the menu "(M)":')
                if choice.upper() in ('(%s)''(%s)'%('M','E')):
                    if choice.upper() == 'M':
                        print(':\033[1;31m%s\033[1;m'%choice.upper())
                        main()
                    
                    
                    elif choice.upper() =='E':
                        print(':\033[1;31m%s\033[1;m'%choice.upper())
                        print('System shutting down')
                        sys.exit
                    else:
                        print('Invalid choice')
                        main()

    else:
        print('Invalid choice, please re-nter your choice')
        main()
                   
        
main()  