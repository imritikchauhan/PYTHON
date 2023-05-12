print("Welcome to the Treasure map")
row1 = ['0', 'O', 'O']
row2 = ['O', 'O', 'O']
row3 = ['O', 'O', 'O']
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
row = int(input('Enter the row number: '))
column = int(input('Enter the column number: '))

position = treasure_map[row-1][column-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
