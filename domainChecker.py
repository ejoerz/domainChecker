import enchant




def main():
    dict = enchant.Dict("en_US")
    inputFileName = input("Please input the absolute path of the input file\n")
    outputFileName = input("Please input the absolute path of the output file\n")
    inputFile = open(inputFileName, 'r')
    
    outputFile = open(outputFileName, 'w')

    Lines = inputFile.readlines()
    
    for line in Lines:
        print(line.strip()[-4:])
        if line.strip()[-4:] == '.com':
            print("This first thing is workinbg")
            outputFile.write(line)
        else:
            print("Try again")

    outputFile.close()
    inputFile.close()

"""def checkWord(string):
    word = string[-5:].strin
    check = True
    if string[-5:].strip != ".com":
        check = False
   """ 

if __name__ == "__main__":
    main()


