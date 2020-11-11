print("Hello, world!")


# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7}

#Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed':float}

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



