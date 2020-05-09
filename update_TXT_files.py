from nltk.tokenize import word_tokenize

accept=['yes','affermative','ofcorse','sure','y']
def File_read():
    try:
        file_red=open('User_data.txt','r')
        file_red.seek(0)
    except FileNotFoundError:
        print(FileNotFoundError)
    else:
        for i in file_red:
            yield (i)


class update:
    #append positive.txt
    def User_appnd(Text):
        try:
            file=open('User_data.txt','a')
            file.write(Text)
            file.write('\n')
        except FileNotFoundError as fnfe:
            print(fnfe)
        else:
            print('Document updated successfully :)')
            file.close()

    #add new file
    def newfile(File_name):
        success=False
        while(not success):
            name=File_name
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
    def cpyfile(text=None):
        success=False
        while(not success):
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

    def userdata(Text):
        success=False

        line=File_read()
        while(not success):
            try:
                lne=next(line)
                if word_tokenize(str(Text))==word_tokenize(lne):
                    print('Already Exist!!')

                    return True
            except StopIteration :

                return False


