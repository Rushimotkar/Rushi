# FUNCTION FOR CREATING MATRIX
def create_matrix():
	row = int(input("Enter number of rows: "))
	col = int(input("Enter number of columns: "))
	matrix = []
	for i in range(row): # A for loop for 0row entries
		a = []
		for j in range(col): # A for loop for column entries
			x = int(input("Enter element: "))
			a.append(x)
		matrix.append(a)
	return matrix, row, col
# FUNCTION FOR DISPLAYING MATRIX
def display_mat(matrix, row, col):
	for i in range(row):
		for j in range(col):
			print(matrix[i][j], end=" ")
		print()
 
# DISPLAYING 1ST MATRIX
print("Enter elements of 1st matrix:")
matrix1, row1, col1 = create_matrix()
print("MATRIX-1 IS :")
print("--------------------------------------")
display_mat(matrix1, row1, col1)
print("--------------------------------------")

# DISPLAYING 2ND MATRIX
print("Enter elements of 2nd matrix:")
matrix2, row2, col2 = create_matrix()
print("MATRIX-2 IS :")
print("--------------------------------------")
display_mat(matrix2, row2, col2)
print("--------------------------------------")
# FUNCTION FOR ADDING MATRICES
def add(matrix1, matrix2, row, col):
	result_add = [[0] * col for _ in range(row)]
	if row1 == row2 and col1 == col2:
		for i in range(row):
			for j in range(col):
				result_add[i][j] = matrix1[i][j] + matrix2[i][j]
		print("ADDITION OF MATRIX-1 AND MATRIX-2 IS :")
		print("--------------------------------------")
		display_mat(result_add, row, col)
		print("--------------------------------------")
	else:
		print("Number of rows and columns must be the same for addition.")
 
# FUNCTION FOR SUBTRACTING MATRICES
def sub(matrix1, matrix2, row, col):
	result_sub = [[0] * col for _ in range(row)]
	if row1 == row2 and col1 == col2:
		for i in range(row):
			for j in range(col):
				result_sub[i][j] = matrix1[i][j] - matrix2[i][j]
				
		print("SUBTRACTION OF MATRIX-1 AND MATRIX-2 IS :")
		print("--------------------------------------")
		display_mat(result_sub, row, col)
		print("--------------------------------------")
	else:
		print("Number of rows and columns must be the same for subtraction.")
	
	
# FUNCTION FOR MULTIPLYING MATRICES
def multiplication(matrix1, matrix2, row1, col1, row2, col2):
	if col1==row2: 
		result_mul = [[0] * col2 for _ in range(row1)]
		for i in range(row1):
			for j in range(col2):
				for k in range(col1):
					result_mul[i][j] += matrix1[i][k] * matrix2[k][j]
		print("MULTIPLICATION OF MATRIX-1 AND MATRIX-2 IS :")
		print("--------------------------------------")
		display_mat(result_mul, row1, col2)
		print("--------------------------------------")
	else:
		print("Matrices cannot be multiplied due to incompatible dimensions")
		
# FUNCTION FOR TRANSPOSE OF MATRIX
def transpose(matrix, row, col):
	result_trans = [[matrix[j][i] for j in range(row)] for i in range(col)]
	print("TRANSPOSE OF THE MATRIX IS :")
	print("--------------------------------------")
	display_mat(result_trans, col, row)
	print("--------------------------------------")
#-----MENU-----
print("OPERATION:\n1. Addition of two matrices\n2. Subtraction of two matrices\n3. Multiplication of two matrices\n4. Transpose of a matrix\n5. Exit")

while True:
 
	c = int(input("Enter Operation Number: "))
	if c == 1:
		add(matrix1, matrix2, row1, col1)
	elif c == 2:
		sub(matrix1, matrix2, row1, col1)
	elif c == 3:
		multiplication(matrix1, matrix2, row1, col1, row2, col2)
	elif c == 4:
		print("Transpose of Matrix-1:")
		transpose(matrix1, row1, col1)
		print("Transpose of Matrix-2:")
		transpose(matrix2, row2, col2)
	elif c == 5:
		print("EXIT")
		break
	else:
		print("ENTER VALID OPERATION NUMBER!!!")
