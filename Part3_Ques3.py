def modifyRC(mat, M, N, x, y):

	for j in range(N):
		if mat[x][j]:
			mat[x][j] = -1

	for i in range(M):
		if mat[i][y]:
			mat[i][y] = -1

def changeMatrix(mat):
	(M, N) = (len(mat), len(mat[0]))
	for i in range(M):
		for j in range(N):
			if mat[i][j] == 0:

				modifyRC(mat, M, N, i, j)
	for i in range(M):
		for j in range(N):
			if mat[i][j] == -1:
				mat[i][j] = 0

if __name__ == '__main__':

	mat = [
		[1, 1, 0, 1, 1],
		[1, 1, 1, 1, 1],
		[1, 1, 0, 1, 1],
		[1, 1, 1, 1, 1],
		[0, 1, 1, 1, 1]
	]
	changeMatrix(mat)
	for r in mat:
		print(r)

