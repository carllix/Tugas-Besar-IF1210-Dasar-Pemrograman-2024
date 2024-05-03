# READ CSV FILE
def readCSV(path:str):
    data = []
    with open(path,'r') as file:
        for line in file:
            elmt = ''
            row = []
            for char in line:
                if char == ';' or char == '\n':
                    row.append(elmt)
                    elmt = ''
                else:
                    elmt = elmt + char 
            data.append(row)
    return data
