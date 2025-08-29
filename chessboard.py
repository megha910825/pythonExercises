letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
chessboard = []
## Write your code here
for letter in letters:
    row =[letter + str(i) for i in range(1,9)]
    chessboard.append(row)

print(chessboard)

