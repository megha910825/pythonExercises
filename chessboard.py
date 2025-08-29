letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
chessboard = []
## Write your code here
for letter in letters:
    row =[letter + str(i) for i in range(1,9)]
    chessboard.append(row)

print(chessboard)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# row = [ letter + str(i) for letter in letters]
chessboard = [[letter + str(i) for i in range(1,9)] for letter in letters]
print(chessboard)

colors = [ ['Red', 'Green', 'White', 'Black'], ['Green', 'Blue', 'White', 'Yellow'] ,['White', 'Blue', 'Green', 'Red'] ]
print(colors[2][3])

matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix[1][2])









