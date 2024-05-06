# Your code here
def matrix_builder(integer):
    matrix= []
    rows = []
    columns= 0
    while integer > 0:
        rows.append(1)
        integer -= 1
        columns += 1
    final_row = rows
    while columns > 0:
        matrix.append(final_row)
        columns -= 1
    return matrix

print(matrix_builder(3))
