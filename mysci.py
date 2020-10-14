print("Hello, world!")

#Read the data file
filename = "data/wxobs20170821.txt"

#datafile = open(filename, "r")

#print(datafile.readline())  #read header
#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())
#datafile.close()


#data = datafile.read()
#datafile.close()
#print(data)
#print("data")

with open(filename, "r") as datafile:   #close the file after reading it
    data = datafile.read()




#print(data)
#print("data")
#print(type(data))



