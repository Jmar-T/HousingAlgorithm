roomsize = input("What size room would you like? ")
maxin = input("How many spots availble do you need? ")
def removefiles(inputfile, outputfile):
       file1 = open(inputfile, "r")
       file2 = open(outputfile, "w")

       for line in file1:
              if roomsize + " person" in line:
                     if "Female" not in line:
                         print(line.strip(), file = file2)
       file1.close()
       file2.close()
def seperate(inputfile, outputfile):
       alist = []
       file1 = open(inputfile, "r")
       file2 = open(outputfile, "w")
       for line in file1:
              line = line.split("\t")
              alist.append(line)
       file1.close()
       newdict = {}
       for item in alist:
              if len(item) > 2:
                     if item[1][:-1] not in newdict:
                            newdict[item[1][:-1]] = []
                     newdict[item[1][:-1]].append(item[1][-1:])
       open4 = []
       for (key,value) in newdict.items():
              if len(value) == int(maxin):
                     open4.append([key,value])
       for item in open4:
              print(item, file = file2)
       file2.close()

removefiles("HousingList.txt", "FiledDown.txt")
seperate("FiledDown.txt", "NewList")
print("Open NewList File to see results.")