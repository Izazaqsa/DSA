rows = int (input ("enter the rows numbers"))
columns = int (input("enter the columns numbers : "))
def board ():
    matrix = []
    for i in range (rows):
        rows = []
        for j in range (columns):
            numbers = int(input("enter the numbers : "))
            rows.append (numbers)
        matrix.append(rows)

    # for i in range (len(matrix))
