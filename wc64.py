def read_file():
    file_handler=open("test.txt","w")
    file_handler.writelines("hello!")
    print("printing each lines in text file")
    file_handler=open("test.txt","r")
    print(file_handler.read())
    file_handler.close()
    file_handler.close()
def main():
    read_file()
if(__name__=="__main__"):
    main()
