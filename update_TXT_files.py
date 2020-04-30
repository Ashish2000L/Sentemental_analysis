import time
accept=['yes','affermative','ofcorse','sure','y']
success=False

class update:
    #append positive.txt
    def appendpos(letter=None):
        start=time.time()
        try:
            file=open('positive.txt','a')
            file.write('\n1\t')
            file.write(str(input("Write your text here: ")))
        except FileNotFoundError as fnfe:
            print(fnfe)
            inpt = str(input('\n would you like to make new file!!'))
            if inpt.lower() in accept:
                try:
                    file = open('positive.txt', 'x')
                    file.write('\n1\t')
                    file.write(str(input('Enter your text: ')))
                except FileExistsError as fxe:
                    print(fxe, '\n unnable to open file')
                    exit(0)
                else:
                    print("\nFile updated successfully :)")
            else :
                print('Thank you, Have a nice day!!')
        else:
            print('\n Document updated successfully :)')
        finally:
            file.close()

    #append negative.txt
    def appendneg(letter=None):
        try:
            file=open('negative.txt','a')
            file.write('\n0\t')
            file.write(input('write your Text here: '))
        except FileNotFoundError as fnfe:
            print(fnfe)
            inpt = str(input('\n would you like to make new file!!'))
            if inpt.lower() in accept:
                try:
                    file = open('negative.txt', 'x')
                    file.write('\n1\t')
                    file.write(str(input('Enter your text: ')))
                except FileExistsError as fxe:
                    print(fxe, '\n unnable to open file')
        else:
            print("Document updated succesfully")

        finally:
            file.close()

    #add new file
    def newfile(name=None):
        while(success!=True):
            name = str(input("Enter the name of the file: "))
            name = name + '.txt'
            try:
                file = open(name, 'x')
            except FileExistsError as fexe:
                print(fexe)
                print(f"file {name} already exist, try another name !")
                success = False
            else:
                success=True
                print("New file made successfully!!")
                file.close()

    #copy data from one file to another
    def cpyfile(text1=None):
        while(success!=True):
            file_addr=str(input('Enter file address (copy from): '))
            cpy_to=str(input('Enter of file (copy to): '))
            try:
                file1=open(file_addr,'r')
            except FileNotFoundError as fnfe:
                success=False
                print(f'File not found at {file_addr}')
                print('Try to make new file using -> newfile() ')
                inpt=str(input('Would you like to continue: '))
                if inpt not in accept:
                    exit(0)
            else:
                try:
                    file2=open(cpy_to,'w')
                except FileNotFoundError as fnfe:
                    success=False
                    print(f'File not found at {cpy_to}')
                    print('Try to make new file using -> newfile() ')
                    inpt = str(input('Would you like to continue: '))
                    if inpt not in accept:
                        exit(0)
                else:
                    try:
                        print("Data copying in progress...")
                        data=file1.read()
                        for i in data:
                            file2.write(i)
                    except:
                        print('Data transfer unsuccessfull :(')
                        file1.close()
                        file2.close()
                        exit(0)
                    else:
                        print("Data transfer successfull :) ")
                        success=True
                        file1.close()
                        file2.close()









